#!/usr/bin/env python3
"""Validates profiles.json: its JSON schema (the one named by "$schema", or --schema), then what
the schema cannot express: extends targets and their variants, inheritance cycles, variants of
the items, the same file (sha256) installed in two places, and the workflows of this repository
(present, size up to date).

Usage: validate_profiles.py [profiles.json] [--schema PATH_OR_URL]
Exit code 1 on error; a stale workflow size is only a warning (run `comfy_profiles.py sizes`)."""
import argparse
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

import jsonschema

PROFILE_REF = re.compile(r"([\w.-]+)(?:\[([\w.,\s-]*)\])?")
SECTIONS = ("custom_nodes", "pip", "models", "workflows")
GITHUB = os.environ.get("GITHUB_ACTIONS") == "true"
errors = []


def error(where, message):
    errors.append(f"{where}: {message}")
    print(f"::error file=profiles.json::{where}: {message}" if GITHUB else f"!! {where}: {message}")


def warning(where, message):
    print(f"::warning file=profiles.json::{where}: {message}" if GITHUB else f"?? {where}: {message}")


def load_schema(source):
    if re.match(r"https?://", source):
        with urllib.request.urlopen(source, timeout=30) as response:
            return json.load(response)
    return json.loads(Path(source).read_text())


def item_variants(item):
    tags = item.get("variant")
    return [tags] if isinstance(tags, str) else list(tags or [])


def this_repo(root):
    """owner/repo of this repository: GITHUB_REPOSITORY in CI, otherwise the origin remote."""
    if os.environ.get("GITHUB_REPOSITORY"):
        return os.environ["GITHUB_REPOSITORY"].lower()
    config = root / ".git" / "config"
    match = config.is_file() and re.search(r"github\.com[:/]([\w.-]+/[\w.-]+?)(?:\.git)?\s", config.read_text())
    return match.group(1).lower() if match else None


def repo_of(source):
    match = re.fullmatch(r"(?:https://github\.com/)?([\w.-]+/[\w.-]+?)(?:\.git)?/?", source.strip())
    return match.group(1).lower() if match else None


def parse_ref(ref):
    """(profile name, variants between brackets, or None without brackets)."""
    match = PROFILE_REF.fullmatch(ref.strip())
    if not match or match.group(2) is None:
        return (match.group(1) if match else ref), None
    return match.group(1), [v.strip() for v in match.group(2).split(",") if v.strip()]


def check_extends(profiles):
    for name, profile in profiles.items():
        for ref in profile.get("extends", []):
            parent, asked = parse_ref(ref)
            if parent not in profiles:
                error(f"{name}.extends", f"unknown profile '{parent}'")
                continue
            if asked is not None:
                declared = profiles[parent].get("variants", [])
                unknown = [v for v in asked if v not in declared]
                if unknown:
                    error(f"{name}.extends", f"'{ref}': unknown variant(s) {', '.join(unknown)} "
                                             f"(declared: {', '.join(declared) or '-'})")

    state = {}  # name -> "visiting" | "done"

    def visit(name, path):
        if state.get(name) == "done" or name not in profiles:
            return
        if state.get(name) == "visiting":
            error(f"{name}.extends", "cycle: " + " -> ".join(path[path.index(name):] + [name]))
            return
        state[name] = "visiting"
        for ref in profiles[name].get("extends", []):
            visit(parse_ref(ref)[0], path + [name])
        state[name] = "done"

    for name in profiles:
        visit(name, [])


def check_variants(profiles):
    for name, profile in profiles.items():
        variants = profile.get("variants", [])
        default = profile.get("default_variant")
        if default is not None and default not in variants:
            error(f"{name}.default_variant", f"'{default}' is not in 'variants'")
        for section in SECTIONS:
            for i, item in enumerate(profile.get(section, [])):
                unknown = [v for v in item_variants(item) if v not in variants] if isinstance(item, dict) else []
                if unknown:
                    error(f"{name}.{section}[{i}]", f"unknown variant(s) {', '.join(unknown)} "
                                                    f"(declared: {', '.join(variants) or '-'})")
        sizes = profile.get("size")
        if isinstance(sizes, dict):
            extra = [v for v in sizes if v not in variants]
            if extra:
                error(f"{name}.size", f"size of undeclared variant(s) {', '.join(extra)}")


def check_same_files(profiles):
    """The same file (same sha256) must be installed in a single place: a shared profile that
    the families extend (qwen3vl-4b, flux2-vae...), or the same type in each profile."""
    places = {}
    for name, profile in profiles.items():
        for i, item in enumerate(profile.get("models", [])):
            if not isinstance(item, dict) or not item.get("sha256"):
                continue
            local = item.get("name") or str(item.get("file", "")).rsplit("/", 1)[-1]
            dest = f"{str(item.get('type', '')).strip('/')}/{local}"
            places.setdefault(item["sha256"], {}).setdefault(dest, []).append(f"{name}.models[{i}]")
    for sha, dests in places.items():
        if len(dests) > 1:
            where = "; ".join(f"{dest} ({', '.join(items)})" for dest, items in dests.items())
            error(next(iter(dests.values()))[0], f"same file (sha256 {sha[:12]}) installed in "
                                                  f"{len(dests)} places: {where}")


def check_workflows(profiles, root):
    repo = this_repo(root)
    if not repo:
        warning("workflows", "repository unknown (no GITHUB_REPOSITORY nor github origin): not checked")
        return
    for name, profile in profiles.items():
        for i, item in enumerate(profile.get("workflows", [])):
            if not isinstance(item, dict) or repo_of(str(item.get("github", ""))) != repo or "revision" in item:
                continue
            where, path = f"{name}.workflows[{i}]", root / str(item.get("file", ""))
            if not path.is_file():
                error(where, f"'{item.get('file')}' missing from the repository")
                continue
            try:
                json.loads(path.read_text())
            except (json.JSONDecodeError, UnicodeDecodeError) as e:
                error(where, f"'{item['file']}': invalid JSON ({e})")
            if "size" in item and item["size"] != path.stat().st_size:
                warning(where, f"'{item['file']}': size {item['size']} declared, {path.stat().st_size} "
                               "actual (comfy_profiles.py sizes)")


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("profiles", nargs="?", default="profiles.json")
    parser.add_argument("--schema", help="schema path or URL (default: the file's $schema)")
    args = parser.parse_args()

    path = Path(args.profiles)
    try:
        data = json.loads(path.read_text())
    except json.JSONDecodeError as e:
        error(str(path), f"invalid JSON ({e})")
        return 1

    source = args.schema or data.get("$schema")
    if not source:
        error(str(path), "no $schema and no --schema")
        return 1
    validator = jsonschema.Draft202012Validator(load_schema(source))
    for e in sorted(validator.iter_errors(data), key=lambda e: list(map(str, e.absolute_path))):
        error(".".join(map(str, e.absolute_path)) or "(root)", e.message)
    if errors:  # the checks below assume a file matching the schema
        return 1

    profiles = data["profiles"]
    check_extends(profiles)
    check_variants(profiles)
    check_same_files(profiles)
    check_workflows(profiles, path.resolve().parent)
    if errors:
        return 1
    print(f">> {path}: {len(profiles)} profiles OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())

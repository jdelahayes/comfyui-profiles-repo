# comfyui-profiles-repo

Profiles file and workflows for [comfyui-profiles](https://github.com/jdelahayes/comfyui-profiles),
the **Profiles** panel for ComfyUI. A profile lists everything a use case needs (models, custom
nodes, workflows) and installs it in one go.

- `profiles.json`: the profiles (format: see the
  [comfyui-profiles README](https://github.com/jdelahayes/comfyui-profiles#format) and its JSON
  schema);
- one folder per model family for the workflows the profiles install (see [Workflows](#workflows)).

## Usage

In ComfyUI, with comfyui-profiles installed: **Profiles** tab → **From a URL…**, then paste

```
https://github.com/jdelahayes/comfyui-profiles-repo/raw/refs/heads/main/profiles.json
```

The workflows of this repository carry a **Workflow profiles** node that declares the profile
they need, with this URL as source: opening one is enough to find out what to install.

Models are installed in a subfolder named after their family (`diffusion_models/krea2/`,
`text_encoders/flux3-klein/`, `vae/moss-image/`...), so that families sharing file names
(`flux2-vae.safetensors`, Qwen text encoders) don't collide. A file that is identical (same
sha256) in several families is installed once, in a shared folder:
- `text_encoders/qwen3vl/` (`qwen3vl-4b`): the Qwen3-VL-4B text encoder of Krea 2, FLUX.3 [klein]
  (int8) and Fibo 2.0;
- `vae/flux2/` (`flux2-vae`): the FLUX.2 VAE of FLUX.2 [klein], FLUX.3 [klein], MOSS-Image and
  Fibo 2.0;
- `vae/qwen-image/` (`qwen-image-vae`): the Qwen Image VAE of Krea 2 and Qwen Image Edit 2511;
- `text_encoders/qwen3-4b/`: the bf16 Qwen3-4B text encoder of FLUX.2 [klein] 4B and Z-Image
  Turbo, declared in both profiles (it is not used by all their variants).

The models carry their `sha256` (written by `comfy_profiles.py sizes`): the validation of this
repository refuses the same file installed in two different places.

### Variants

Most profiles come in several precisions: `int8`, `fp8`, `nvfp4` (Blackwell GPUs only),
`w4a8`, `bf16`. Choose one with brackets (`krea2-turbo[bf16]`); without them, the profile's
default variant is used (the first one listed below). Workflows are provided for the default
variant only: for another one, change it in the workflow's **Workflow profiles** node and use
**Check the workflow's models…** (comfyui-profiles ≥ 0.10).

### Access

- **FLUX.2 [klein] 9B, FLUX.3 [klein]**: gated Hugging Face repositories, accept the license
  on Hugging Face and set `HF_TOKEN` (the FLUX.2 [klein] 4B is not gated).
- **CivitAI** models (`krea2-heretic`, `krea2-loras-purplelady`): set `CIVITAI_TOKEN`.

## Profiles

Sizes include the inherited profiles (`extends`). The `*-common` profiles are only building
blocks for the others.

| Profile | Contents | Variants (size) |
|---|---|---|
| `comfyui-common` | Common custom nodes (KJNodes, rgthree, RES4LYF, VideoHelperSuite...), inherited by every profile | – |
| `minimax-h3-fl2va` | MiniMax H3 FL2VA | int8 (52.2 GB), bf16 (124.3 GB) |
| `minimax-h3-ref2va` | MiniMax H3 Ref2VA | int8 (52.2 GB), bf16 (124.3 GB) |
| `minimax-h3-all` | `minimax-h3-fl2va` + `minimax-h3-ref2va` | int8 (73.2 GB), bf16 (190.6 GB) |
| `minimax-h3-hybrid-int8` | MiniMax H3 Hybrid (smhfacct) | 52.2 GB |
| `minimax-h3-obvpm-r2v` | MiniMax H3 OBVPM Timeline R2V, with its workflows | 50.5 GB |
| `flux2-vae` | FLUX.2 VAE shared by FLUX.2 [klein], FLUX.3 [klein], MOSS-Image and Fibo 2.0, in `vae/flux2/` | 336 MB |
| `qwen-image-vae` | Qwen Image VAE shared by Krea 2 and Qwen Image Edit 2511, in `vae/qwen-image/` | 254 MB |
| `qwen3vl-4b` | Qwen3-VL-4B text encoder shared by Krea 2, FLUX.3 [klein] (int8) and Fibo 2.0, in `text_encoders/qwen3vl/` | int8 (4.9 GB), fp8 (5.2 GB), bf16 (8.9 GB) |
| `krea2-turbo` | Krea 2 Turbo | int8 (18.9 GB), fp8 (18.9 GB), bf16 (35.7 GB) |
| `krea2-raw` | Krea 2 Raw + turbo LoRA | int8 (19.3 GB), fp8 (19.4 GB), bf16 (36.1 GB) |
| `krea2-styles` | Krea 2 Turbo + 10 official style LoRAs | int8 (23.5 GB), fp8 (23.6 GB), bf16 (40.3 GB) |
| `krea2-heretic` | Krea 2 Turbo + uncensored text encoders and LoRAs | int8 (33.7 GB), fp8 (23.8 GB), bf16 (40.6 GB) |
| `krea2-loras-purplelady` | Krea 2 Turbo + [purplelady](https://civitai.com/user/purplelady)'s LoRAs | int8 (20.2 GB), fp8 (20.3 GB), bf16 (37.0 GB) |
| `flux2-klein-9b` | FLUX.2 [klein] 9B distilled: text to image, multi-reference edit | fp8 (18.7 GB), kv-fp8 (19.1 GB), nvfp4 (13.1 GB), bf16 (35.1 GB) |
| `flux2-klein-base-9b` | FLUX.2 [klein] Base 9B, not distilled | fp8 (18.8 GB), nvfp4 (13.2 GB), bf16 (35.1 GB) |
| `flux2-klein-4b` | FLUX.2 [klein] 4B distilled (Apache 2.0): text to image, multi-reference edit | fp8 (12.7 GB), nvfp4 (6.9 GB), bf16 (16.4 GB) |
| `flux2-klein-base-4b` | FLUX.2 [klein] Base 4B, not distilled | fp8 (12.7 GB), nvfp4 (6.9 GB), bf16 (16.4 GB), gguf (7.9 GB, for 6–8 GB GPUs) |
| `flux2-klein-4b-all` | `flux2-klein-4b` + `flux2-klein-base-4b` in bf16, with the text to image template comparing them | 24.1 GB |
| `flux3-klein` | FLUX.3 [klein] distilled: text to image, edit with up to 10 references | int8 (17.7 GB), nvfp4 (17.2 GB), bf16 (39.1 GB) |
| `flux3-klein-base` | FLUX.3 [klein] Base, not distilled | int8 (17.7 GB), nvfp4 (17.2 GB), bf16 (39.1 GB) |
| `moss-image` | MOSS-Image SFT: text to image, with bounding boxes | w4a8 (13.3 GB), int8 (15.7 GB), bf16 (30.1 GB) |
| `moss-image-base` | MOSS-Image Base | w4a8 (13.3 GB), int8 (15.7 GB), bf16 (30.1 GB) |
| `ausboss-moss-image` | MOSS-Image workflow by AusBoss: speed LoRAs, SeedVR2, AusBoss nodes, without the base model (with `moss-image[int8]`) | 6.3 GB |
| `seedvr2` | SeedVR2 3B int8 and its VAE: 2x upscale of the AusBoss workflows | 4.0 GB |
| `sam3.1` | SAM 3.1: segmentation of a named or clicked thing, for the masks of the AusBoss workflows | 1.7 GB |
| `z-image-turbo` | Z-Image Turbo: text to image in 8 steps, 2K upscale | int8 (12.2 GB), nvfp4 (8.4 GB), bf16 (20.8 GB) |
| `z-image-turbo-controlnet` | Z-Image Turbo + Fun ControlNets (Union, Union 2.1 lite, Tile 2.1 lite) | int8 (19.4 GB), nvfp4 (15.5 GB), bf16 (27.9 GB) |
| `fibo2-dev` | Fibo 2.0 (BRIA AI) Dev: text to image, with the turbo LoRA; non-commercial license (CC BY-NC 4.0) | int8 (15.6 GB), bf16 (27.7 GB) |
| `fibo2-edit-turbo` | Fibo 2.0 Edit Turbo: image edit in 4 steps; non-commercial license (CC BY-NC 4.0) | int8 (13.6 GB), bf16 (25.7 GB) |
| `ausboss-fibo2` | FIBO 2.0 Generate + Edit workflow by AusBoss: Qwen3-VL 8B (auto prompt), SeedVR2, AusBoss nodes, without the base model (with `fibo2-edit-turbo[int8]`) | 13.3 GB |
| `qwen_image_2.1-turbo` | Qwen Image 2.1 Turbo | int8 (26.8 GB), bf16 (41.9 GB) |
| `qwen_image_2.1` | Qwen Image 2.1 | int8 (26.8 GB), bf16 (41.9 GB) |
| `ausboss-qwen_image_2.1` | The 12 Qwen Image 2.1 workflows by AusBoss, with everything they need: full and turbo int8 models, AusBoss, Viggle, Pruna T8 and BFS LoRAs, AusBoss nodes (Inpaint and Cut Out + Remove also need `sam3.1`) | 36.3 GB |
| `alissonerdx-bfs` | [BFS: Best Face Swap](https://huggingface.co/Alissonerdx/BFS-Best-Face-Swap) LoRAs and workflows, without the base model (see below) | qwen_2.1 (1.3 GB), krea2 (1.8 GB), flux2-klein-4b (1.8 GB), flux2-klein-9b (994 MB) |
| `qwen_image_edit_2511-turbo` | Qwen Image Edit 2511 + Lightning 4 steps and edit LoRAs | int8 (31.6 GB) |
| `yue2-3b` | YuE2 3B, music generation | int8 (5.3 GB) |

`comfy_profiles.py list` (or the panel) shows the full, up-to-date list with descriptions.

`alissonerdx-bfs` gathers the BFS LoRAs and workflows, with one variant per base model
(`qwen_2.1`, `krea2`, `flux2-klein-4b`, `flux2-klein-9b`; Qwen Image Edit... to come). It does
not install the base model: install it with the profile of its family, e.g.
`qwen_image_2.1[int8],alissonerdx-bfs[qwen_2.1]` or `krea2-turbo[int8],alissonerdx-bfs[krea2]`,
which is what the workflows declare.

## Workflows

| Folder | Profiles | Origin |
|---|---|---|
| [`flux2/klein/`](flux2/klein/) | `flux2-klein-9b`, `flux2-klein-base-9b`, `flux2-klein-4b`, `flux2-klein-base-4b`, `flux2-klein-4b-all` | Official ComfyUI templates (MIT) |
| [`flux3/klein/`](flux3/klein/) | `flux3-klein`, `flux3-klein-base` | Official Black Forest Labs workflows (MIT) |
| [`moss/`](moss/) | `moss-image`, `moss-image-base` | Official ComfyUI templates (MIT) |
| [`moss/ausboss/`](moss/ausboss/) | `ausboss-moss-image` (with `moss-image[int8]`) | MOSS-Image text to image by AusBoss (4/8/50 steps, img2img, SeedVR2 2x) |
| [`z-image/`](z-image/) | `z-image-turbo`, `z-image-turbo-controlnet` | Official ComfyUI templates (MIT) |
| [`fibo2/`](fibo2/) | `fibo2-dev`, `fibo2-edit-turbo` | Written for this repository (no official template yet) |
| [`fibo2/ausboss/`](fibo2/ausboss/) | `ausboss-fibo2` (with `fibo2-edit-turbo[int8]`) | FIBO 2.0 edit or text to image by AusBoss (4 steps, auto prompt, SeedVR2 2x) |
| [`h3/obvpm/`](h3/obvpm/) | `minimax-h3-obvpm-r2v` | OBVPM Timeline R2V |
| [`qwen_image_2.1/ausboss/`](qwen_image_2.1/ausboss/) | `ausboss-qwen_image_2.1` (and `sam3.1` for Inpaint, Cut Out + Remove) | Qwen Image 2.1 workflows by AusBoss (generate + edit, outpaint, inpaint, swaps, upscale) |
| [`qwen_image_2.1/alissonerdx_bfs/`](qwen_image_2.1/alissonerdx_bfs/) | `alissonerdx-bfs[qwen_2.1]` (with `qwen_image_2.1[int8]`) | BFS workflows by Alissonerdx (MIT) |
| [`flux2/klein/alissonerdx_bfs/`](flux2/klein/alissonerdx_bfs/) | `alissonerdx-bfs[flux2-klein-4b]`, `alissonerdx-bfs[flux2-klein-9b]` (with `flux2-klein-4b[fp8]`, `flux2-klein-9b[fp8]`) | BFS workflows by Alissonerdx (MIT) |
| [`krea2/alissonerdx_bfs/`](krea2/alissonerdx_bfs/) | `alissonerdx-bfs[krea2]` (with `krea2-turbo[int8]`) | BFS workflows by Alissonerdx (MIT) |
| [`krea2/`](krea2/) | `krea2-heretic` (declared in the workflow, not installed by the profile) | Krea 2 text to image (ThinkingLLM + ClownSharkSampler) |

In the copies of official workflows, the models are referenced in their family subfolder; each
folder's README lists the changes, and the upstream license is kept in `LICENSE.upstream`.

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
(`flux2-vae.safetensors`, Qwen text encoders) don't collide.

### Variants

Most profiles come in several precisions: `int8`, `fp8`, `nvfp4` (Blackwell GPUs only),
`w4a8`, `bf16`. Choose one with brackets (`krea2-turbo[bf16]`); without them, the profile's
default variant is used (the first one listed below). Workflows are provided for the default
variant only: for another one, change it in the workflow's **Workflow profiles** node and use
**Check the workflow's models…** (comfyui-profiles ≥ 0.10).

### Access

- **FLUX.2 / FLUX.3 [klein]**: gated Hugging Face repositories, accept the license on Hugging
  Face and set `HF_TOKEN`.
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
| `krea2-turbo` | Krea 2 Turbo | int8 (18.9 GB), fp8 (18.9 GB), bf16 (35.7 GB) |
| `krea2-raw` | Krea 2 Raw + turbo LoRA | int8 (19.3 GB), fp8 (19.4 GB), bf16 (36.1 GB) |
| `krea2-styles` | Krea 2 Turbo + 10 official style LoRAs | int8 (23.5 GB), fp8 (23.6 GB), bf16 (40.3 GB) |
| `krea2-heretic` | Krea 2 Turbo + uncensored text encoders and LoRAs | int8 (33.7 GB), fp8 (23.8 GB), bf16 (40.6 GB) |
| `krea2-loras-purplelady` | Krea 2 Turbo + [purplelady](https://civitai.com/user/purplelady)'s LoRAs | int8 (20.2 GB), fp8 (20.3 GB), bf16 (37.0 GB) |
| `flux2-klein-9b` | FLUX.2 [klein] 9B distilled: text to image, multi-reference edit | fp8 (18.7 GB), kv-fp8 (19.1 GB), nvfp4 (13.1 GB), bf16 (35.1 GB) |
| `flux2-klein-base-9b` | FLUX.2 [klein] Base 9B, not distilled | fp8 (18.8 GB), nvfp4 (13.2 GB), bf16 (35.1 GB) |
| `flux3-klein` | FLUX.3 [klein] distilled: text to image, edit with up to 10 references | int8 (17.7 GB), nvfp4 (17.2 GB), bf16 (39.1 GB) |
| `flux3-klein-base` | FLUX.3 [klein] Base, not distilled | int8 (17.7 GB), nvfp4 (17.2 GB), bf16 (39.1 GB) |
| `moss-image` | MOSS-Image SFT: text to image, with bounding boxes | w4a8 (13.3 GB), int8 (15.7 GB), bf16 (30.1 GB) |
| `moss-image-base` | MOSS-Image Base | w4a8 (13.3 GB), int8 (15.7 GB), bf16 (30.1 GB) |
| `qwen_image_2.1-turbo` | Qwen Image 2.1 Turbo | int8 (26.8 GB), bf16 (41.9 GB) |
| `qwen_image_2.1` | Qwen Image 2.1 | int8 (26.8 GB), bf16 (41.9 GB) |
| `qwen_image_edit_2511-turbo` | Qwen Image Edit 2511 + Lightning 4 steps and edit LoRAs | int8 (31.6 GB) |
| `yue2-3b` | YuE2 3B, music generation | int8 (5.3 GB) |

`comfy_profiles.py list` (or the panel) shows the full, up-to-date list with descriptions.

## Workflows

| Folder | Profiles | Origin |
|---|---|---|
| [`flux2/klein/`](flux2/klein/) | `flux2-klein-9b`, `flux2-klein-base-9b` | Official ComfyUI templates (MIT) |
| [`flux3/klein/`](flux3/klein/) | `flux3-klein`, `flux3-klein-base` | Official Black Forest Labs workflows (MIT) |
| [`moss/`](moss/) | `moss-image`, `moss-image-base` | Official ComfyUI templates (MIT) |
| [`h3/obvpm/`](h3/obvpm/) | `minimax-h3-obvpm-r2v` | OBVPM Timeline R2V |
| [`krea2/`](krea2/) | `krea2-heretic` (declared in the workflow, not installed by the profile) | Krea 2 text to image (ThinkingLLM + ClownSharkSampler) |

In the copies of official workflows, the models are referenced in their family subfolder; each
folder's README lists the changes, and the upstream license is kept in `LICENSE.upstream`.

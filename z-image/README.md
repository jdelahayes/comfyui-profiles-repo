# Z-Image Turbo workflows

Copies of the official ComfyUI templates
([Comfy-Org/workflow_templates](https://github.com/Comfy-Org/workflow_templates), `templates/`),
MIT license (see `LICENSE.upstream`).

| Workflow | Profile |
|---|---|
| `image_z_image_turbo_int8.json` | `z-image-turbo[int8]` |
| `utility_z_image_turbo_2k_upscaler.app.json` (app mode, 2K upscale) | `z-image-turbo[bf16]` |
| `image_z_image_turbo_fun_union_controlnet.json` | `z-image-turbo-controlnet[bf16]` |

Changes:
- the bf16 Qwen3-4B text encoder, the same file as FLUX.2 [klein] 4B, is in the shared
  `text_encoders/qwen3-4b/` folder;
- the models are referenced in their `z-image/` subfolder (`diffusion_models/z-image/`,
  `text_encoders/z-image/`, `vae/z-image/`, `model_patches/z-image/`, `upscale_models/z-image/`),
  where the profiles install them;
- a "Workflow profiles" node (comfyui-profiles) declares the profile the workflow needs (see
  the table), with this repository's `profiles.json` as source.

The bf16 text to image template is not kept: the int8 one serves every variant. For another
variant, change it in the workflow's "Workflow profiles" node (e.g. `z-image-turbo[nvfp4]`) and
use **Check the workflow's models…** (comfyui-profiles ≥ 0.10). The upscaler and ControlNet
templates only exist in bf16.

`z-image-turbo-controlnet` also installs the Union 2.1 lite and Tile 2.1 lite ControlNets: pick
them in the workflow's model patch loader instead of the original Union.

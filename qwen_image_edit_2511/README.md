# Qwen Image Edit 2511 workflows

Copies of the official ComfyUI templates
([Comfy-Org/workflow_templates](https://github.com/Comfy-Org/workflow_templates), `templates/`),
MIT license (see `LICENSE.upstream`). All need the `qwen_image_edit_2511-turbo[int8]` profile.

| Workflow | Use |
|---|---|
| `image_qwen_image_edit_2511_int8.json` | image edit, 4 steps with the Lightning LoRA |
| `template_qwen_multiangle.app.json` (app mode) | new camera angle of a picture, with the Multiple Angles LoRA (fal) |
| `template_qwen_image_edit_2511_systms_action.json` | dynamic action pose, with the SYSTMS Action LoRA |

Changes:
- the models are referenced in their `qwen_image_edit_2511/` subfolder
  (`diffusion_models/qwen_image_edit_2511/`, `text_encoders/qwen_image_edit_2511/`,
  `loras/qwen_image_edit_2511/<author>/`) and the VAE in the shared `vae/qwen-image/` folder,
  where the profiles install them;
- the SYSTMS Action template uses the int8 model instead of bf16 (38 GB), like the two others;
- a "Workflow profiles" node (comfyui-profiles) declares the profile the workflow needs, with
  this repository's `profiles.json` as source.

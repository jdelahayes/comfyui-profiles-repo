# MiniMax H3 Image workflows

Copies of the official ComfyUI templates of
[Comfy-Org/workflow_templates](https://github.com/Comfy-Org/workflow_templates/tree/main/templates)
(`image_minimax_h3_image_*`), MIT license (see `LICENSE.upstream`):
- `image_minimax_h3_image_t2i.json`: text to image;
- `image_minimax_h3_image_edit.json`: image edit.

Both use the Qwen3.5-9B w4a8 text encoder as prompt enhancer (switchable in the workflow). The
`api_minimax_h3_image_*` templates (MiniMax API nodes, cloud) are not copied: they need no local
model.

Changes:
- the models are referenced in their `h3/` subfolder (`diffusion_models/h3/`,
  `text_encoders/h3/`, `vae/h3/`), where the `minimax-h3-image` profile installs them; the MiniMax
  H3 text encoder is the same file, in the same place, as the one of `minimax-h3-common[int8]`;
- the Qwen3.5-9B prompt enhancer, the same file as MOSS-Image's, is in the shared
  `text_encoders/qwen3.5/` folder (`qwen3.5-9b` profile);
- the "Model Storage Location" of the notes shows these subfolders, and the text to image note
  names the Qwen3.5 repository and file it links to (it said Qwen3.8-27B);
- a "Workflow profiles" node (comfyui-profiles) declares the profile the workflow needs:
  `minimax-h3-image[int8]`, with this repository's `profiles.json` as source.

The workflows use the files of the default variant `int8` (int8 diffusion model, int8 text
encoder). For `w4a8` (smaller diffusion model, same int8 text encoder) or `bf16` (bf16 diffusion
model and text encoder), change it in the workflow's "Workflow profiles" node
(`minimax-h3-image[bf16]`) and use **Check the workflow's models…** (comfyui-profiles ≥ 0.10).
The prompt enhancer stays Qwen3.5-9B w4a8 for every variant.

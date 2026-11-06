# MiniMax H3 Pika H3 Flex workflows

Copies of the official ComfyUI templates of
[Comfy-Org/workflow_templates](https://github.com/Comfy-Org/workflow_templates/tree/main/templates)
(`video_pika_h3_flex_*`), MIT license (see `LICENSE.upstream`):
- `video_pika_h3_flex_t2v.json`: text to video (FL2VA model + `pika_h3_flex_fl2va` LoRA);
- `video_pika_h3_flex_fl2va.json`: first/last frame to video (FL2VA model + `pika_h3_flex_fl2va` LoRA);
- `video_pika_h3_flex_ref2va.json`: references to video (Ref2VA model + `pika_h3_flex_ref2va` LoRA).

The `api_pika_h3_flex_t2v` template (Pika API node, cloud) is not copied: it needs no local model.

Changes:
- the models are referenced in their `h3/` subfolder (`diffusion_models/h3/`,
  `text_encoders/h3/`, `vae/h3/`) and the LoRAs in `loras/h3/pika/`, where the
  `minimax-h3-pika-flex` profile installs them;
- the text encoder is the int8 one (`qwen3vl_32b_minimax_h3_int8_convrot.safetensors`, installed by
  `minimax-h3-common[int8]`) instead of the nvfp4 one (`qwen3vl_32b_minimax_h3_nvfp4_awq`) of the
  upstream templates, in the loaders, the download links and the notes;
- a "Workflow profiles" node (comfyui-profiles) declares the profile the workflow needs:
  `minimax-h3-pika-flex[int8]`, with this repository's `profiles.json` as source.

The workflows use the files of the default variant `int8` (int8 diffusion models, int8 text
encoder, int8 video VAE). For `bf16`, change it in the workflow's "Workflow profiles" node
(`minimax-h3-pika-flex[bf16]`) and use **Check the workflow's models…** (comfyui-profiles ≥ 0.10).

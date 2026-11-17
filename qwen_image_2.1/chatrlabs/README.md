# Qwen Image 2.1 Uncensored Omni (ChatR Labs), GGUF workflow

`chatrlabs_qwen_image_2.1_uncensored_gguf.json` is a copy of the
[ChatR Labs](https://huggingface.co/chatrlabs/Qwen-Image-2.1-Uncensored-Omni-Quantized)
text to image example workflow (`workflow_example.json`: BF16 transformer, INT8 text encoder,
BF16 VAE, verified by ChatR Labs with ComfyUI 0.39.0), for the GGUF builds of the
`chatrlabs-qwen_image_2.1-uncensored` profile. The original workflow is installed by every
variant of the profile, unchanged, as `chatrlabs_qwen_image_2.1_uncensored_t2i.json`.

Changes:
- `UNETLoader` replaced by `Unet Loader (GGUF)` ([ComfyUI-GGUF](https://github.com/city96/ComfyUI-GGUF),
  installed by the `gguf-q4` and `gguf-q5` variants), on the Q4_K_M build
  (`qwen-image-2.1-step90000-Q4_K_M.gguf`, for 6 GB GPUs); pick the Q5_K_M one in the loader for
  `gguf-q5`;
- the models are referenced in their family subfolder, where the profiles install them:
  `diffusion_models/qwen_image_2.1/chatrlabs/`, `text_encoders/qwen_image_2.1/`,
  `vae/qwen_image_2.1/` (`qwen_image_2.1-common[int8]`);
- 768×1152 instead of 1728×1728 (one of the starting resolutions ChatR Labs recommends; 1728×1728
  needs much more memory), resolution 1024 in `TextEncodeQwenImage21`;
- the explicit example prompt replaced by the neutral one of the ChatR Labs README, seed 42
  (randomize), output prefix `chatrlabs_qwen_image_2.1`;
- a "Workflow profiles" node (comfyui-profiles) declares the profile the workflow needs:
  `chatrlabs-qwen_image_2.1-uncensored[gguf-q4]`, with this repository's `profiles.json` as
  source.

`chatrlabs_qwen_image_2.1_uncensored_gguf_edit.json` is the image edit version of that GGUF
workflow, following the ChatR Labs README ("encode the reference image with the Qwen Image text
encoder in edit mode; the latent comes from that node"): `EmptyLatentImage` removed, a
`LoadImage` (image_1) and the VAE plugged into `TextEncodeQwenImage21`, whose `latent` output
feeds the `KSampler`; resolution 1024 (pixel budget, image_1's aspect ratio is kept), an edit
prompt using `<image1>`, and a note on extra references (image_2 to image_10). Same models and
settings as the text to image workflow.

Settings kept: 35 steps, CFG 5, `er_sde` / `simple`, negative prompt `" "` (a single space: an
empty one disables true CFG), `QwenImage21Cache`.

The weights and the workflow are under the Qwen Research License Agreement (non-commercial
research and evaluation), copied in `LICENSE.upstream`.

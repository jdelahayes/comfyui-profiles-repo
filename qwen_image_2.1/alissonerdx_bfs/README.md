# BFS workflows for Qwen Image 2.1

Copies of the Qwen Image 2.1 workflows of
[Alissonerdx/BFS-Best-Face-Swap](https://huggingface.co/Alissonerdx/BFS-Best-Face-Swap)
(`Head Swap V1 Qwen 2.1 Workflow.json`, `Body Swap Qwen Image 2.1 - V1.json`), MIT license.

Changes:
- the models are referenced in their family subfolder, where the profiles install them:
  `qwen_image_2.1/` for the base model (`qwen_image_2.1` profile),
  `loras/qwen_image_2.1/alissonerdx/` for the BFS LoRAs and `loras/qwen_image_2.1/ameno-tech/`
  for the optional Pruna 8-step LoRA ([ameno-tech/Pruna-Qwen-Image-2.1](https://huggingface.co/ameno-tech/Pruna-Qwen-Image-2.1))
  (`alissonerdx-bfs[qwen_2.1]` profile); BiRefNet (body swap) stays in `background_removal/`;
- a "Workflow profiles" node (comfyui-profiles) declares the profiles the workflow needs:
  `qwen_image_2.1[int8], alissonerdx-bfs[qwen_2.1]`, with this repository's `profiles.json` as
  source.

# BFS workflows for FLUX.2 [klein]

Copies of the FLUX.2 [klein] workflow of
[Alissonerdx/BFS-Best-Face-Swap](https://huggingface.co/Alissonerdx/BFS-Best-Face-Swap)
(`Head Swap V1 Flux 2 Klein 4b_9b (base_distill).json`), MIT license, one per size. Guide:
[docs/flux-2-klein.md](https://huggingface.co/Alissonerdx/BFS-Best-Face-Swap/blob/main/docs/flux-2-klein.md)
(image 1: target body, image 2: reference head; do not reverse them).

Changes:
- `head_swap_flux2_klein_9b.json` / `head_swap_flux2_klein_4b.json`: the models are the fp8 files
  of `flux2-klein-9b` / `flux2-klein-4b` in their `flux2-klein/` subfolder (the original pointed
  to the bf16 9B diffusion model at the root), and the BFS LoRA is
  `bfs_head_v1_flux-klein_9b_step3750_rank64` / `bfs_head_v1_flux-klein_4b` in
  `loras/flux2-klein/alissonerdx/`. `alissonerdx-bfs` also installs the other LoRA of each size
  (`…_9b_step3500_rank128`, `bfs_head_v1.1_optional_flux-klein_4b`) and the custom nodes of the
  workflow: ComfyUI-RMBG (background removal, downloads its RMBG-2.0 model on first use),
  ComfyUI-QwenVL and ComfyUI-Custom-Scripts (optional expression caption, bypassed);
- a "Workflow profiles" node (comfyui-profiles) declares the profiles the workflow needs:
  `flux2-klein-9b[fp8], alissonerdx-bfs[flux2-klein-9b]` or
  `flux2-klein-4b[fp8], alissonerdx-bfs[flux2-klein-4b]`, with this repository's
  `profiles.json` as source.

The sampler is set for the distilled models (cfg 1, 4 steps). With a Base model
(`flux2-klein-base-9b`, `flux2-klein-base-4b`): cfg 5, 20 steps or more.

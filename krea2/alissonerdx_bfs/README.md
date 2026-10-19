# BFS workflows for Krea 2

Copies of the Krea 2 workflows of
[Alissonerdx/BFS-Best-Face-Swap](https://huggingface.co/Alissonerdx/BFS-Best-Face-Swap)
(`Head Swap Krea 2 - V1 Simple Workflow.json`, `Body Swap Krea 2 - V1 Simple Workflow.json`),
MIT license. Guide: [docs/krea-2.md](https://huggingface.co/Alissonerdx/BFS-Best-Face-Swap/blob/main/docs/krea-2.md).

Changes:
- the models are referenced in their family subfolder, where the profiles install them: the
  int8 files of `krea2-turbo` in `krea2/` (the originals pointed to the fp8 text encoder and to
  `Downloads/` for the diffusion model), the BFS LoRAs in `loras/krea2/alissonerdx/`
  (`alissonerdx-bfs[krea2]`, which also installs the
  [comfyui-krea2edit](https://github.com/lbouaraba/comfyui-krea2edit) nodes);
- a "Workflow profiles" node (comfyui-profiles) declares the profiles the workflow needs:
  `krea2-turbo[int8], alissonerdx-bfs[krea2]`, with this repository's `profiles.json` as source.

With `krea2-raw` instead of the turbo model: 40 steps, cfg 3-4 (see the workflows' notes).

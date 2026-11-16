# MiniMax H3 Image workflow by AusBoss

Copy of AusBoss' [MiniMax H3 Image Generate + Edit](https://civitai.com/models/3046048) workflow
(v1.1, `minimaxH3ImageGenerateEdit_v11.json`, published as
`MiniMax-H3-Image Generate + Edit (AusBoss).json`), made with the
[ComfyUI-AusBoss](https://github.com/ausboss/ComfyUI-AusBoss) nodes (2.22.0 or newer; it ran on
2.23.0). Text to image or edit at 4 or 16 MP, up to 7 extra reference pictures, Auto prompt
(Qwen3.5-9B), Fast (2 steps with akhaliq's pDMD LoRA), 2x upscale with SeedVR2. It needs a
ComfyUI newer than 0.44.0 (MiniMax-H3-Image support was added on 2026-11-10).

Changes:
- the MiniMax H3 text encoder is the int8 one (`qwen3vl_32b_minimax_h3_int8_convrot.safetensors`,
  the same file as `minimax-h3-image[int8]` and `minimax-h3-common[int8]`) instead of the nvfp4
  one (`qwen3vl_32b_minimax_h3_nvfp4_awq`, Blackwell GPUs only), in the loader, its download link
  and the "Guide + models" note;
- the models are referenced in their family subfolder, where the profiles install them: the
  MiniMax H3 Image files in `h3/` (`minimax-h3-image`), the Qwen3.5-9B prompt writer in the shared
  `qwen3.5/` folder (`qwen3.5-9b`), the pDMD LoRA in `loras/h3/akhaliq/` and the SeedVR2 files in
  `diffusion_models/seedvr2/` and `vae/seedvr2/` (`ausboss-minimax-h3-image`, which extends
  `seedvr2` and also installs the AusBoss nodes);
- a "Workflow profiles" node (comfyui-profiles) declares the profiles the workflow needs:
  `minimax-h3-image[int8], ausboss-minimax-h3-image`, with this repository's `profiles.json` as
  source.

The workflow opens on **High VRAM** (int8 diffusion model). **Low VRAM** loads the w4a8 one: add
`w4a8` to the profile in the "Workflow profiles" node (`minimax-h3-image[int8,w4a8]`) or install
`minimax-h3-image[w4a8]`.

MiniMax-H3-Image is under the MiniMax-H3-Image Community License.

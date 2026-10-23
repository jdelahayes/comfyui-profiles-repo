# MOSS-Image workflow by AusBoss

Copy of AusBoss' MOSS-Image Text to Image workflow (`mossImageTextToImage4Step_v14.json`, v1.4),
made with the [ComfyUI-AusBoss](https://github.com/ausboss/ComfyUI-AusBoss) nodes (2.16.1 or
newer). Video: [youtu.be/CF8pIIlV9-0](https://youtu.be/CF8pIIlV9-0).

Changes:
- the models are referenced in their family subfolder, where the profiles install them: the int8
  files of `moss-image` in `moss-image/` (diffusion model, text encoder, VAE), the speed LoRAs
  in `loras/moss-image/lodestones/` (8 steps) and `loras/moss-image/akhaliq/` (4 steps), the
  SeedVR2 files in `diffusion_models/seedvr2/` and `vae/seedvr2/` (`ausboss-moss-image`, which
  also installs the AusBoss nodes);
- the 4-step LoRA keeps its original name, `lora.safetensors` (the original workflow had it
  renamed `MOSS-Image-SFT-4-steps.safetensors`): the LoRA Loader rows, the Steps switches and
  the notes were changed to match;
- a "Workflow profiles" node (comfyui-profiles) declares the profiles the workflow needs:
  `moss-image[int8], ausboss-moss-image`, with this repository's `profiles.json` as source.

The optional abliterated text encoder named in the "Uncensored" note is not installed by the
profiles.

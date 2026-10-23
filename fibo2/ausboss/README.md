# FIBO 2.0 workflow by AusBoss

Copy of AusBoss' [FIBO 2.0 Generate + Edit](https://civitai.com/models/3013987) workflow
(`fibo20GenerateEdit4Step_v10.json`, v1.0), made with the
[ComfyUI-AusBoss](https://github.com/ausboss/ComfyUI-AusBoss) nodes (2.13.0 or newer). It edits
a picture from a plain-words change in 4 steps, or makes a new picture with "Edit a picture"
off; Auto prompt (Qwen3-VL 8B) writes the detailed prompt, SeedVR2 makes the result 2x.

Changes:
- the models are referenced in their family subfolder, where the profiles install them: the int8
  files of `fibo2-edit-turbo` in `fibo2/` (diffusion model, text encoder, VAE), the Auto prompt
  text encoder in `text_encoders/qwen_image_2.1/` (the file of `qwen_image_2.1[int8]`, not
  downloaded twice), the SeedVR2 files in `diffusion_models/seedvr2/` and `vae/seedvr2/`
  (`ausboss-fibo2`, which extends `seedvr2` and also installs the AusBoss nodes);
- a "Workflow profiles" node (comfyui-profiles) declares the profiles the workflow needs:
  `fibo2-edit-turbo[int8], ausboss-fibo2`, with this repository's `profiles.json` as source.

Needs ComfyUI with Fibo 2.0 support (merged on master on 2026-10-20, not in a release yet). The
optional "Heretic" text encoders named in the workflow's note are not installed by the profiles.
The FIBO 2.0 weights are under the CC BY-NC 4.0 license (BRIA AI): non-commercial use only.

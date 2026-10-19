# MOSS-Image workflows

Copies of the official ComfyUI templates of
[Comfy-Org/workflow_templates](https://github.com/Comfy-Org/workflow_templates/tree/main/templates)
(`image_moss_image_*`), MIT license (see `LICENSE.upstream`).

Changes:
- the models are referenced in their `moss-image/` subfolder (`diffusion_models/moss-image/`,
  `text_encoders/moss-image/`, `vae/moss-image/`), where the `moss-image` and `moss-image-base`
  profiles install them;
- `image_moss_image_t2i_bboxes.json`: the download link of the diffusion model pointed to the
  Base model, it now points to the SFT model;
- a "Workflow profiles" node (comfyui-profiles) declares the profile the workflow needs:
  `moss-image[w4a8]` or `moss-image-base[w4a8]`, with this repository's `profiles.json` as source.

The workflows use the files of the default variant `w4a8` (int8 diffusion model, w4a8 text
encoder, small VAE), for every variant of the profiles. For another one, change it in the
workflow's "Workflow profiles" node (e.g. `moss-image[bf16]`) and use **Check the workflow's
models…** (comfyui-profiles ≥ 0.10): the model fields are turned to the files of that variant.

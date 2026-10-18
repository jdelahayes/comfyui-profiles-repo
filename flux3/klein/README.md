# FLUX.3 [klein] workflows

Copies of the official workflows of
[black-forest-labs/flux-3-image-klein-comfy](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy/tree/main/workflows),
MIT license (see `LICENSE.upstream`).

Only change: the models are referenced in their `flux3-klein/` subfolder
(`diffusion_models/flux3-klein/`, `text_encoders/flux3-klein/`, `vae/flux3-klein/`), where the
`flux3-klein` and `flux3-klein-base` profiles install them.

Only the int8 workflows are kept (the default variant), for every variant of the profiles. For
another one, declare it in the workflow's "Workflow profiles" node (e.g. `flux3-klein[bf16]`)
and use **Check the workflow's models…** (comfyui-profiles ≥ 0.10): the model fields are turned
to the files of that variant.

The image to image workflows load sample images (`klein_ref_*.jpg`) from the original repository:
download them into `ComfyUI/input/`, or load your own images.

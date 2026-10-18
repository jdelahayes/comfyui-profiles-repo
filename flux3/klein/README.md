# FLUX.3 [klein] workflows

Copies of the official workflows of
[black-forest-labs/flux-3-image-klein-comfy](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy/tree/main/workflows),
MIT license (see `LICENSE.upstream`).

Only change: the models are referenced in their `flux3-klein/` subfolder
(`diffusion_models/flux3-klein/`, `text_encoders/flux3-klein/`, `vae/flux3-klein/`), where the
`flux3-klein` and `flux3-klein-base` profiles install them.

The image to image workflows load sample images (`klein_ref_*.jpg`) from the original repository:
download them into `ComfyUI/input/`, or load your own images.

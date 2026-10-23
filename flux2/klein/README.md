# FLUX.2 [klein] workflows

Copies of the official ComfyUI templates
([Comfy-Org/workflow_templates](https://github.com/Comfy-Org/workflow_templates), `templates/`),
MIT license (see `LICENSE.upstream`).

| Workflow | Profile |
|---|---|
| `image_flux2_klein_image_edit_9b_distilled.json` | `flux2-klein-9b[fp8]` |
| `image_flux2_klein_9b_kv_image_edit.json` | `flux2-klein-9b[kv-fp8]` |
| `image_flux2_klein_image_edit_9b_base.json` | `flux2-klein-base-9b[fp8]` |
| `image_flux2_klein_image_edit_4b_distilled.json` | `flux2-klein-4b[fp8]` |
| `image_flux2_klein_image_edit_4b_base.json` | `flux2-klein-base-4b[fp8]` |
| `image_flux2_klein_text_to_image.json` (4B distilled and Base side by side, bf16) | `flux2-klein-4b-all` |

Changes:
- the FLUX.2 VAE (shared with FLUX.3 [klein], MOSS-Image, Fibo 2.0) is in `vae/flux2/` (`flux2-vae`
  profile), the bf16 Qwen3-4B text encoder of the 4B (shared with Z-Image) in
  `text_encoders/qwen3-4b/`;
- the models are referenced in their `flux2-klein/` subfolder (`diffusion_models/flux2-klein/`,
  `text_encoders/flux2-klein/`, `vae/flux2-klein/`), where the profiles install them; the 4B and
  9B profiles share the VAE files there;
- a "Workflow profiles" node (comfyui-profiles) declares the profile the workflow needs (see
  the table), with this repository's `profiles.json` as source.

The fp8 workflows serve every variant: for another one, change it in the workflow's "Workflow
profiles" node (e.g. `flux2-klein-9b[bf16]`) and use **Check the workflow's models…**
(comfyui-profiles ≥ 0.10). The KV edit workflow needs the `kv-fp8` model. The 4B has no fp8
text encoder: its fp8 and bf16 variants both use `qwen_3_4b` in bf16.

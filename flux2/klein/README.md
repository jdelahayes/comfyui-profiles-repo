# FLUX.2 [klein] 9B workflows

Copies of the official ComfyUI templates
([Comfy-Org/workflow_templates](https://github.com/Comfy-Org/workflow_templates), `templates/`),
MIT license (see `LICENSE.upstream`).

Only change: the models are referenced in their `flux2-klein/` subfolder
(`diffusion_models/flux2-klein/`, `text_encoders/flux2-klein/`, `vae/flux2-klein/`), where the
`flux2-klein-9b` and `flux2-klein-base-9b` profiles install them.

The fp8 workflows serve every variant: for another one, declare it in the workflow's "Workflow
profiles" node (e.g. `flux2-klein-9b[bf16]`) and use **Check the workflow's models…**
(comfyui-profiles ≥ 0.10). The KV edit workflow needs the `kv-fp8` model.

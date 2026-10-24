# FLUX.2 [klein] workflows

Copies of the official ComfyUI templates
([Comfy-Org/workflow_templates](https://github.com/Comfy-Org/workflow_templates), `templates/`),
MIT license (see `LICENSE.upstream`).

| Workflow | Profile |
|---|---|
| `image_flux2_klein_image_edit_9b_distilled.json` | `flux2-klein-9b[fp8]` |
| `image_flux2_klein_image_edit_9b_distilled_gguf.json` (GGUF loaders) | `flux2-klein-9b[gguf]` |
| `image_flux2_klein_9b_kv_image_edit.json` | `flux2-klein-9b[kv-fp8]` |
| `image_flux2_klein_image_edit_9b_base.json` | `flux2-klein-base-9b[fp8]` |
| `image_flux2_klein_image_edit_4b_distilled.json` | `flux2-klein-4b[fp8]` |
| `image_flux2_klein_image_edit_4b_distilled_gguf.json` (GGUF loaders) | `flux2-klein-4b[gguf]` |
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

The `gguf` variant of `flux2-klein-4b` is for GPUs with little VRAM (6–8 GB, e.g. a laptop RTX
3060): [unsloth](https://huggingface.co/unsloth/FLUX.2-klein-4B-GGUF) Q5_K_M model (3.1 GB) and
[Q8_0 Qwen3-4B](https://huggingface.co/unsloth/Qwen3-4B-GGUF) text encoder (4.3 GB, same weights
as `qwen_3_4b`, in `text_encoders/qwen3-4b/`), loaded by
[ComfyUI-GGUF](https://github.com/city96/ComfyUI-GGUF). Its workflow is the 4B distilled template
with `UnetLoaderGGUF` and `CLIPLoaderGGUF` in place of `UNETLoader` and `CLIPLoader`: the GGUF files
cannot be switched in with **Check the workflow's models…**, hence a workflow of its own. Other
quantizations (Q4_K_M, Q6_K, Q8_0…) of the same repositories can be picked in the loaders.

`flux2-klein-9b` has a `gguf` variant too, for GPUs of 8 GB and more:
[unsloth](https://huggingface.co/unsloth/FLUX.2-klein-9B-GGUF) Q4_K_M model (5.9 GB) and
[Q5_K_M Qwen3-8B](https://huggingface.co/unsloth/Qwen3-8B-GGUF) text encoder (5.9 GB, same weights as
`qwen_3_8b`), not gated; same GGUF loaders in its workflow. On 6 GB, prefer `flux2-klein-4b[gguf]`:
the 9B only fits in Q3_K_M, with a visible loss of quality.

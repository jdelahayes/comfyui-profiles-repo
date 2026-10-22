# Fibo 2.0 workflows

There is no official ComfyUI template for the local Fibo 2.0 models yet (only the Bria API one):
these workflows are written for this repository, from the settings of the ComfyUI pull request
that added Fibo 2.0 ([#17240](https://github.com/Comfy-Org/ComfyUI/pull/17240)).

| Workflow | Profile | Settings |
|---|---|---|
| `fibo2_dev_t2i.json` | `fibo2-dev[int8]` | Dev, text to image: 30 steps, CFG 5 |
| `fibo2_dev_turbo_t2i.json` | `fibo2-dev[int8]` | Dev + turbo LoRA, text to image: 4 steps, CFG 1 |
| `fibo2_edit_turbo.json` | `fibo2-edit-turbo[int8]` | Edit Turbo, image edit: 4 steps, CFG 1 |

All use euler / simple and the `TextEncodeFibo2` node, which needs ComfyUI with Fibo 2.0
support (merged on master on 2026-10-20, not in v0.42.4 yet).

The turbo LoRA of [Comfy-Org/Fibo-2.0](https://huggingface.co/Comfy-Org/Fibo-2.0) is extracted
from the difference between two checkpoints (`diff_b` keys, dynamic rank from 512): Edit
Turbo − Dev. It goes on Dev, to sample it in 4 steps without CFG.

The workflows use the files of the default variant `int8`. For bf16, change it in the
workflow's "Workflow profiles" node (e.g. `fibo2-dev[bf16]`) and use **Check the workflow's
models…** (comfyui-profiles ≥ 0.10).

The weights are under the CC BY-NC 4.0 license (BRIA AI): non-commercial use only.

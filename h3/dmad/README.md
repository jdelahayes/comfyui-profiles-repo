# MiniMax H3 DMAD workflows

Copies of the [DMAD](https://huggingface.co/ZhengmingYu/DMAD) ComfyUI workflows by Zhengming Yu
([paper](https://arxiv.org/abs/2610.02188), [code](https://github.com/Yzmblog/DMAD)), from
[`minimax_h3/workflows`](https://huggingface.co/ZhengmingYu/DMAD/tree/main/minimax_h3/workflows): text to
video with stereo audio, 1344x768 at 24 fps, MiniMax H3 FL2VA with a `full_critic` DMAD LoRA
(`lcm` sampler, `simple` scheduler, shift 12 / audio shift 2, no CFG):
- `dmad_h3_4step_15s_podcast.json`: 15 s in 4 steps (16 GB GPU or larger);
- `dmad_h3_8step_15s_wok.json`: 15 s in 8 steps with the 8-step student (`8step_full_critic`), better
  audio-video quality (16 GB GPU or larger);
- `dmad_h3_4step_5s_8gb_guitar.json`: 5 s in 4 steps for 8 GB GPUs (`H3 Memory Optimization` in its
  lowest-memory setting and `H3 AIMDO Residency Limiter` at 0 blocks).

They need the [H3-Optimizations](https://github.com/Zironic/H3-Optimizations) nodes (installed by
`minimax-h3-common`) and about 64 GB of system memory on 8 to 24 GB GPUs.

Changes:
- the text encoder is the int8 one (`qwen3vl_32b_minimax_h3_int8_convrot.safetensors`) instead of the
  nvfp4 one (`qwen3vl_32b_minimax_h3_nvfp4_awq`, Blackwell GPUs only), and the video VAE is the int8 one
  (`minimax_h3_video_vae_int8_convrot.safetensors`) instead of the fp16 one, the files of
  `minimax-h3-common[int8]`, in the loaders, their download links and the notes; the videos are therefore
  not bit-identical to the upstream examples;
- the models are referenced in their `h3/` subfolder and the LoRAs in `loras/h3/zhengmingyu/`, where the
  `dmad-minimax-h3` profile installs them;
- a "Workflow profiles" node (comfyui-profiles) declares the profile the workflow needs:
  `dmad-minimax-h3[int8]`, with this repository's `profiles.json` as source.

The 4-step workflows use `dmad_minimax_h3_4step_full_critic_comfyui.safetensors`. The 8-step workflow
uses `dmad_minimax_h3_8step_full_critic_comfyui.safetensors` instead of the 4-step LoRA of the upstream
workflow, as the DMAD model card recommends for the 8-step student; the 4-step LoRA also runs at 8 steps
(pick it in `LoraLoaderModelOnly`). Both LoRAs are installed in `loras/h3/zhengmingyu/`.

The DMAD LoRAs are Model Derivatives of MiniMax H3, under the MiniMax H3 Community License Agreement
(`LICENSE.upstream`, `NOTICE.upstream`), which excludes the European Union, the United Kingdom, the
Republic of Korea and the United States of America.

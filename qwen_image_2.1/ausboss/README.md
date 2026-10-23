# Qwen Image 2.1 workflows by AusBoss

Copies of AusBoss' Qwen Image 2.1 workflows from [Civitai](https://civitai.com/user/AusBoss),
made with the [ComfyUI-AusBoss](https://github.com/ausboss/ComfyUI-AusBoss) nodes:

| Workflow | Civitai | What it does |
|---|---|---|
| `qwenImage21GenerateEdit_v20.json` | [2962616](https://civitai.com/models/2962616) | Edit a picture in plain words or make a new one, full model, Auto prompt, 8 MP upscale |
| `qwenImage21TurboGenerate_v12.json` | [2994247](https://civitai.com/models/2994247) | The same with the Turbo checkpoint, 8 steps |
| `qwenImage21TurboMulti_v12.json` | [3000002](https://civitai.com/models/3000002) | Edit with up to five more pictures to take from (clothes...), Turbo, 8 steps |
| `qwenImage21EditRealign_v11.json` | [2969862](https://civitai.com/models/2969862) | Edit without shifting the picture |
| `qwenImage21Outpaint_v12.json` | [2964810](https://civitai.com/models/2964810) | Extend a picture on any side, Auto prompt |
| `qwenImage21Rotate_v11.json` | [2966883](https://civitai.com/models/2966883) | Turn, crop and pad, then outpaint |
| `qwenImage21Inpaint_v10.json` | [3000390](https://civitai.com/models/3000390) | Click a thing (SAM 3.1) and say what to change |
| `qwenImage21CutOutRemove_v10.json` | [2987326](https://civitai.com/models/2987326) | Name a thing: transparent PNG of it, and the picture without it |
| `qwenImage21OutfitSwap_v11.json` | [2983126](https://civitai.com/models/2983126) | Dress the person in the outfit of a second picture |
| `qwenImage21PersonSwap_v10.json` | [2980685](https://civitai.com/models/2980685) | Head or full body swap (BFS LoRAs by Alissonerdx) |
| `qwenImage21TiledUpscale_v11.json` | [2988629](https://civitai.com/models/2988629) | Redraw a picture sharp in tiles, to 4 or 8 MP |
| `qwenImage21TextToImage_v10.json` | [2962641](https://civitai.com/models/2962641) | Plain text to image, with a LoRA stack |

Changes:
- the models are referenced in their family subfolder, where the profiles install them: the int8
  files of `qwen_image_2.1` and `qwen_image_2.1-turbo` in `qwen_image_2.1/`, the LoRAs in
  `loras/qwen_image_2.1/{ausboss,viggle,t8star,alissonerdx}/` (in the LoRA Loader rows and the
  workflow switches too) (`ausboss-qwen_image_2.1`, which also installs the AusBoss nodes), SAM 3.1
  in `checkpoints/sam3.1/` (`sam3.1`);
- a "Workflow profiles" node (comfyui-profiles) declares the profiles the workflow needs:
  `ausboss-qwen_image_2.1`, plus `sam3.1` for Inpaint and Cut Out + Remove, with this
  repository's `profiles.json` as source.

The Viggle turbo and Pruna T8 speed LoRAs are under the Qwen Research License (research use).

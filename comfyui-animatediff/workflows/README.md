# ComfyUI Workflows

This directory contains workflow configurations for ComfyUI AnimateDiff.

## Available Workflows

### `animatediff_workflow.json`
Complete workflow for generating animated videos using AnimateDiff.

**Configuration:**
- **Checkpoint**: Stable Diffusion v1.5
- **Resolution**: 512x512
- **Frames**: 16 frames
- **Frame Rate**: 8 FPS
- **Sampler**: Euler
- **Steps**: 20
- **CFG Scale**: 7.5

**Default Prompts:**
- **Positive**: "stunning cinematic landscape, mountains, sunrise, 8k, masterpiece"
- **Negative**: "low quality, worst quality, blurry, watermark"

## How to Use

1. Start ComfyUI server:
   ```bash
   python run_comfyui.py
   ```

2. Open ComfyUI in browser: http://localhost:8188

3. Load the workflow:
   - Click "Load" button
   - Select `workflows/animatediff_workflow.json`
   - Or drag and drop the JSON file onto the canvas

4. Customize parameters:
   - Edit prompts
   - Adjust resolution, steps, CFG
   - Change seed for different results

5. Click "Queue Prompt" to generate video

## Customization Tips

### Prompts
Edit the positive and negative prompts in nodes 2 and 3 to control the output.

### Video Settings
In node 9 (Video Combine):
- `frame_rate`: Control playback speed (default: 8 FPS)
- `filename_prefix`: Change output filename
- `crf`: Video quality (lower = higher quality, 19 is recommended)

### Generation Settings
In node 5 (KSampler):
- `seed`: Change for different variations
- `steps`: More steps = better quality (but slower)
- `cfg`: How closely to follow prompt (7-8 recommended)

### Resolution
In node 6 (Empty Latent):
- `width`/`height`: Must be multiples of 8
- `batch_size`: Number of frames (16 recommended for AnimateDiff)

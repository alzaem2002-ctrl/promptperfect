# ComfyUI + AnimateDiff Setup Guide

This repository contains scripts to set up **ComfyUI** with **AnimateDiff** for AI-powered video generation using Stable Diffusion.

## ?? What is This?

- **ComfyUI**: A powerful node-based interface for Stable Diffusion
- **AnimateDiff**: Extension that enables video/animation generation
- **Combined**: Create animated videos from text prompts!

## ?? Prerequisites

### Required
- **Python 3.10+**
- **Git**
- **10GB+ free disk space** (for models)
- **Internet connection** (for downloading models)

### Recommended
- **NVIDIA GPU** with 8GB+ VRAM (RTX 3060 or better)
- **CUDA 11.8+** installed
- **16GB+ system RAM**

> ?? **Note**: ComfyUI can run on CPU but will be very slow. GPU is highly recommended.

## ?? Quick Start

### 1. Run Setup Script

```bash
# Make scripts executable
chmod +x setup_comfyui.sh start_comfyui.sh download_additional_models.sh

# Run the setup (this will take 10-30 minutes)
./setup_comfyui.sh
```

This script will:
- ? Check for GPU availability
- ? Clone ComfyUI repository
- ? Install all Python dependencies
- ? Download required models:
  - Stable Diffusion v1.5 (~4GB)
  - VAE model (~335MB)
  - AnimateDiff model (~1.8GB)

### 2. Start ComfyUI

```bash
./start_comfyui.sh
```

Or manually:
```bash
cd ComfyUI
python main.py --listen
```

### 3. Open Web Interface

Open your browser and navigate to:
- **Local**: http://localhost:8188
- **Network**: http://YOUR_IP:8188

## ?? What Gets Downloaded

### Core Models (Required)
| Model | Size | Purpose |
|-------|------|---------|
| Stable Diffusion v1.5 | ~4GB | Base image generation model |
| VAE (ft-mse) | ~335MB | Image encoding/decoding |
| AnimateDiff mm_sd_v15_v2 | ~1.8GB | Animation/motion module |

### Optional Models
Run `./download_additional_models.sh` to get:
- Realistic Vision (photorealistic images)
- DreamShaper (artistic/fantasy)
- ControlNet (pose/edge control)
- ESRGAN Upscaler (4x upscaling)

## ?? Using ComfyUI

### Basic Workflow

1. **Open the Web UI** (http://localhost:8188)
2. **Load a workflow**:
   - Click "Load" in the menu
   - Browse example workflows
   - Or create your own!
3. **Configure nodes**:
   - Set your text prompt
   - Adjust generation settings
   - Configure AnimateDiff parameters
4. **Queue Prompt** to generate!

### Creating Animations with AnimateDiff

1. Use the AnimateDiff Loader node
2. Connect it to your Stable Diffusion workflow
3. Set frame count (typically 16-32 frames)
4. Generate your animation!
5. Export as GIF or video

## ??? Interactive Terminal UI

For a terminal-based interface:

```bash
python interactive_ui.py
```

Features:
- Check server status
- View queue status
- Monitor system resources
- Quick access to web UI
- Help and documentation

## ?? Directory Structure

```
ComfyUI/
??? models/
?   ??? checkpoints/          # Stable Diffusion models
?   ??? vae/                  # VAE models
?   ??? animatediff_models/   # AnimateDiff models
?   ??? loras/                # LoRA models
?   ??? controlnet/           # ControlNet models
?   ??? upscale_models/       # Upscaling models
??? input/                    # Input images
??? output/                   # Generated outputs
??? custom_nodes/             # Extensions/plugins
```

## ?? Configuration Options

### ComfyUI Command Line Options

```bash
# Low VRAM mode (for GPUs with <8GB VRAM)
python main.py --lowvram

# CPU mode (no GPU)
python main.py --cpu

# Different port
python main.py --port 8080

# High quality mode
python main.py --highvram

# Preview method
python main.py --preview-method auto
```

### Memory Management

| GPU VRAM | Recommended Mode |
|----------|------------------|
| 4GB | `--lowvram --preview-method none` |
| 6GB | `--lowvram` |
| 8GB | Default |
| 12GB+ | `--highvram` |

## ?? Troubleshooting

### Issue: "CUDA out of memory"
**Solution**: 
- Use `--lowvram` flag
- Reduce batch size
- Generate smaller images (512x512 instead of 1024x1024)

### Issue: "Models not loading"
**Solution**:
- Check models are in correct directories
- Verify model files are not corrupted
- Re-download using the setup script

### Issue: "Server won't start"
**Solution**:
- Check if port 8188 is already in use
- Verify Python dependencies are installed
- Check Python version (must be 3.10+)

### Issue: "Animations are slow"
**Solution**:
- Reduce frame count
- Use smaller resolution
- Enable xformers (faster attention)
- Use `--preview-method none`

## ?? Additional Resources

### Official Documentation
- [ComfyUI GitHub](https://github.com/comfyanonymous/ComfyUI)
- [AnimateDiff GitHub](https://github.com/guoyww/AnimateDiff)
- [ComfyUI Examples](https://comfyanonymous.github.io/ComfyUI_examples/)

### Community Resources
- [ComfyUI Reddit](https://reddit.com/r/comfyui)
- [Civitai Models](https://civitai.com) - Download more models
- [OpenArt ComfyUI Workflows](https://openart.ai/workflows)

### Video Tutorials
- Search "ComfyUI tutorial" on YouTube
- Search "AnimateDiff ComfyUI" for animation guides

## ?? Example Use Cases

1. **Text-to-Animation**: Generate animated videos from text prompts
2. **Image-to-Animation**: Animate static images
3. **Style Transfer**: Apply artistic styles with motion
4. **Character Animation**: Animate characters with pose control
5. **Loop Generation**: Create seamless looping animations

## ?? Security Notes

- ComfyUI runs a local web server
- By default, it's accessible only from your machine
- Use `--listen` flag to allow network access
- Be cautious when exposing to internet
- No authentication by default

## ?? License

- ComfyUI: GPL-3.0 License
- AnimateDiff: See respective repository
- Models: Check individual model licenses on Hugging Face

## ?? Contributing

Found a bug or want to improve the scripts?
- Create an issue
- Submit a pull request
- Share your workflows!

## ?? Known Limitations

- AnimateDiff works best with SD 1.5 models
- SDXL support is experimental
- Long videos (>32 frames) require significant VRAM
- Quality depends on base model and prompts

## ?? Tips for Best Results

1. **Use descriptive prompts**: Be specific about what you want
2. **Negative prompts**: Specify what you don't want
3. **Frame count**: 16-24 frames for smooth short animations
4. **Resolution**: 512x512 is standard, higher needs more VRAM
5. **Motion scale**: Higher = more movement, can cause artifacts
6. **Seed control**: Use same seed for consistent results
7. **Experiment**: Try different models and settings!

## ?? Support

Having issues? Check:
1. This README troubleshooting section
2. ComfyUI GitHub issues
3. ComfyUI community forums
4. Run the interactive UI for diagnostics

---

**Last Updated**: 2025-10-31

**Version**: 1.0

Happy animating! ???

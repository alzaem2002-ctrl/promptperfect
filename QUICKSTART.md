# ComfyUI + AnimateDiff - Quick Start Guide

## ?? 5-Minute Setup

### Option 1: Bash Scripts (Recommended for Linux/Mac)

```bash
# 1. Make scripts executable
chmod +x *.sh

# 2. Run setup (downloads ~6GB of models)
./setup_comfyui.sh

# 3. Start ComfyUI
./start_comfyui.sh
```

**Done!** Open http://localhost:8188 in your browser.

### Option 2: Jupyter Notebook

```bash
# 1. Install Jupyter
pip install jupyter ipywidgets

# 2. Start Jupyter
jupyter notebook

# 3. Open comfyui_setup.ipynb and run all cells
```

### Option 3: Manual Setup

```bash
# 1. Clone ComfyUI
git clone https://github.com/comfyanonymous/ComfyUI
cd ComfyUI

# 2. Install dependencies
pip install -r requirements.txt

# 3. Download models (create directories first)
mkdir -p models/checkpoints models/vae models/animatediff_models

# Download SD 1.5
wget -P models/checkpoints https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned-emaonly.safetensors

# Download VAE
wget -P models/vae https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.safetensors

# Download AnimateDiff
wget -P models/animatediff_models https://huggingface.co/guoyww/animatediff/resolve/main/mm_sd_v15_v2.ckpt

# 4. Start server
python main.py --listen
```

## ?? What You Get

? **ComfyUI** - Node-based Stable Diffusion interface  
? **AnimateDiff** - AI video/animation generation  
? **Models** - SD 1.5, VAE, AnimateDiff (~6GB)  
? **Scripts** - Easy setup and management  
? **Interactive UI** - Terminal-based control panel  
? **Documentation** - Comprehensive guides  

## ?? First Animation

1. **Open ComfyUI**: http://localhost:8188
2. **Load default workflow** or create new
3. **Add nodes**:
   - Load Checkpoint (SD 1.5)
   - CLIP Text Encode (your prompt)
   - AnimateDiff Loader
   - KSampler
   - Save Image/Video
4. **Set parameters**:
   - Prompt: "a cat walking, realistic, high quality"
   - Frames: 16
   - Steps: 20
   - CFG: 7.5
5. **Click "Queue Prompt"**
6. **Wait for generation** (1-5 minutes depending on GPU)
7. **Find output** in `ComfyUI/output/`

## ?? Quick Tips

- **Low VRAM?** Use `./start_comfyui.sh` then edit to add `--lowvram`
- **Slow?** Reduce resolution to 512x512
- **Experiments?** Try different models from Civitai
- **Learn more?** Check `COMFYUI_README.md`

## ??? Useful Tools

```bash
# Interactive terminal UI
python interactive_ui.py

# Download more models
./download_additional_models.sh

# Check GPU usage
watch -n 1 nvidia-smi

# View outputs
ls -lh ComfyUI/output/
```

## ?? Common Issues

| Issue | Solution |
|-------|----------|
| CUDA out of memory | Add `--lowvram` flag |
| Models not loading | Check paths in `models/` folder |
| Port 8188 in use | Use `--port 8080` |
| Slow on CPU | Need GPU for practical use |

## ?? Full Documentation

- **Detailed setup**: `COMFYUI_README.md`
- **All scripts**: Documented with inline comments
- **Notebook guide**: `comfyui_setup.ipynb`

## ?? System Requirements

**Minimum:**
- Python 3.10+
- 8GB RAM
- 10GB disk space

**Recommended:**
- NVIDIA GPU (8GB+ VRAM)
- 16GB RAM
- CUDA 11.8+

## ?? Next Steps

1. ? Complete setup
2. ?? Create your first animation
3. ?? Learn ComfyUI workflows
4. ?? Customize and experiment
5. ?? Share your creations!

---

**Need help?** Check the full README or open an issue!

**Ready to create?** Start ComfyUI and let your imagination flow! ???

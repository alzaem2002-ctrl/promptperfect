#!/bin/bash
set -e

echo "=========================================="
echo "ComfyUI + AnimateDiff Setup Script"
echo "=========================================="
echo ""

# Check for GPU
echo "Checking for NVIDIA GPU..."
if command -v nvidia-smi &> /dev/null; then
    nvidia-smi
    echo "? GPU ????! (GPU Available!)"
else
    echo "? No NVIDIA GPU detected. ComfyUI will run on CPU (very slow)"
fi
echo ""

# Set up project directory
HOME_DIR="${HOME}"
PROJECT_DIR="${HOME_DIR}/comfyui-animatediff"
echo "Project directory: ${PROJECT_DIR}"
echo ""

# Clone ComfyUI repository
echo "Cloning ComfyUI from GitHub..."
if [ -d "ComfyUI" ]; then
    echo "ComfyUI directory already exists. Skipping clone."
    cd ComfyUI
    git pull
else
    git clone https://github.com/comfyanonymous/ComfyUI
    cd ComfyUI
fi
echo "? ComfyUI repository ready"
echo ""

# Install dependencies
echo "Installing Python dependencies..."
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
    echo "? Dependencies installed"
else
    echo "? requirements.txt not found"
fi
echo ""

# Create model directories
echo "Creating model directories..."
CHECKPOINT_DIR="./models/checkpoints"
VAE_DIR="./models/vae"
ANIMATEDIFF_DIR="./models/animatediff_models"

mkdir -p "${CHECKPOINT_DIR}"
mkdir -p "${VAE_DIR}"
mkdir -p "${ANIMATEDIFF_DIR}"
echo "? Model directories created"
echo ""

# Download models
echo "=========================================="
echo "Downloading AI Models (this may take a while)..."
echo "=========================================="
echo ""

# Stable Diffusion v1.5
if [ ! -f "${CHECKPOINT_DIR}/v1-5-pruned-emaonly.safetensors" ]; then
    echo "Downloading Stable Diffusion v1.5..."
    wget -P "${CHECKPOINT_DIR}" https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned-emaonly.safetensors
    echo "? Stable Diffusion v1.5 downloaded"
else
    echo "? Stable Diffusion v1.5 already exists"
fi
echo ""

# VAE model
if [ ! -f "${VAE_DIR}/vae-ft-mse-840000-ema-pruned.safetensors" ]; then
    echo "Downloading VAE model..."
    wget -P "${VAE_DIR}" https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.safetensors
    echo "? VAE model downloaded"
else
    echo "? VAE model already exists"
fi
echo ""

# AnimateDiff model
if [ ! -f "${ANIMATEDIFF_DIR}/mm_sd_v15_v2.ckpt" ]; then
    echo "Downloading AnimateDiff model..."
    wget -P "${ANIMATEDIFF_DIR}" https://huggingface.co/guoyww/animatediff/resolve/main/mm_sd_v15_v2.ckpt
    echo "? AnimateDiff model downloaded"
else
    echo "? AnimateDiff model already exists"
fi
echo ""

echo "=========================================="
echo "? Setup Complete!"
echo "=========================================="
echo ""
echo "To start ComfyUI, run:"
echo "  cd ComfyUI"
echo "  python main.py --listen"
echo ""
echo "Or use the start script:"
echo "  ./start_comfyui.sh"
echo ""
echo "Then open your browser to:"
echo "  http://localhost:8188"
echo ""

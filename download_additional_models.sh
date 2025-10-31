#!/bin/bash
set -e

echo "=========================================="
echo "Download Additional Models for ComfyUI"
echo "=========================================="
echo ""

if [ ! -d "ComfyUI" ]; then
    echo "? ComfyUI directory not found!"
    echo "Please run setup_comfyui.sh first"
    exit 1
fi

cd ComfyUI

# Create directories
CHECKPOINT_DIR="./models/checkpoints"
LORA_DIR="./models/loras"
CONTROLNET_DIR="./models/controlnet"
UPSCALE_DIR="./models/upscale_models"

mkdir -p "${CHECKPOINT_DIR}"
mkdir -p "${LORA_DIR}"
mkdir -p "${CONTROLNET_DIR}"
mkdir -p "${UPSCALE_DIR}"

echo "Choose models to download:"
echo "1. Realistic Vision (Realistic images)"
echo "2. DreamShaper (Artistic/Fantasy)"
echo "3. ControlNet (Pose control)"
echo "4. ESRGAN Upscaler (4x upscaling)"
echo "5. All of the above"
echo "6. Skip additional models"
echo ""
read -p "Enter your choice (1-6): " choice

case $choice in
    1|5)
        echo ""
        echo "Downloading Realistic Vision v5.1..."
        wget -P "${CHECKPOINT_DIR}" https://huggingface.co/SG161222/Realistic_Vision_V5.1_noVAE/resolve/main/Realistic_Vision_V5.1_fp16-no-ema.safetensors
        echo "? Realistic Vision downloaded"
        ;&
esac

case $choice in
    2|5)
        echo ""
        echo "Downloading DreamShaper 8..."
        wget -P "${CHECKPOINT_DIR}" https://huggingface.co/Lykon/DreamShaper-8/resolve/main/DreamShaper_8_pruned.safetensors
        echo "? DreamShaper downloaded"
        ;&
esac

case $choice in
    3|5)
        echo ""
        echo "Downloading ControlNet OpenPose..."
        wget -P "${CONTROLNET_DIR}" https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_openpose.pth
        echo "? ControlNet downloaded"
        ;&
esac

case $choice in
    4|5)
        echo ""
        echo "Downloading ESRGAN 4x Upscaler..."
        wget -P "${UPSCALE_DIR}" https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth
        echo "? ESRGAN downloaded"
        ;;
    6)
        echo "Skipping additional models"
        ;;
    *)
        echo "Invalid choice"
        exit 1
        ;;
esac

echo ""
echo "=========================================="
echo "? Additional models download complete!"
echo "=========================================="

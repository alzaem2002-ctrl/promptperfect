#!/bin/bash

echo "=========================================="
echo "Starting ComfyUI Server"
echo "=========================================="
echo ""

# Check if ComfyUI directory exists
if [ ! -d "ComfyUI" ]; then
    echo "? ComfyUI directory not found!"
    echo "Please run setup_comfyui.sh first"
    exit 1
fi

cd ComfyUI

echo "Starting ComfyUI with external listening enabled..."
echo ""
echo "Access the UI at:"
echo "  Local:   http://localhost:8188"
echo "  Network: http://$(hostname -I | awk '{print $1}'):8188"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Start ComfyUI with external listening
python main.py --listen

# Alternative options you can add:
# --port 8188              : Change port
# --dont-upcast-attention  : Disable upcasting of attention (faster on some GPUs)
# --use-split-cross-attention : Use split cross attention (saves memory)
# --use-pytorch-cross-attention : Use PyTorch cross attention
# --fp16-vae               : Run VAE in fp16 (faster but may reduce quality)
# --bf16-vae               : Run VAE in bf16
# --cpu                    : Run on CPU instead of GPU
# --normalvram             : Normal VRAM mode
# --lowvram                : Low VRAM mode
# --novram                 : No VRAM mode (runs on CPU RAM)

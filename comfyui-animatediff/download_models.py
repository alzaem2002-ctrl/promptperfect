#!/usr/bin/env python3
"""
Model Download Script for ComfyUI AnimateDiff
Downloads required models from HuggingFace
"""

import os
import sys
import subprocess
from pathlib import Path
from urllib.request import urlretrieve
from tqdm import tqdm

class DownloadProgressBar(tqdm):
    """Progress bar for downloads"""
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)

def download_file(url, output_path):
    """Download a file with progress bar"""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    if output_path.exists():
        print(f"? File already exists: {output_path.name}")
        return True
    
    print(f"\n?? Downloading: {output_path.name}")
    print(f"   From: {url}")
    
    try:
        with DownloadProgressBar(unit='B', unit_scale=True, miniters=1, desc=output_path.name) as t:
            urlretrieve(url, output_path, reporthook=t.update_to)
        print(f"? Downloaded: {output_path.name}")
        return True
    except Exception as e:
        print(f"? Error downloading {output_path.name}: {e}")
        return False

def download_models(comfyui_path):
    """Download all required models"""
    comfyui_path = Path(comfyui_path)
    
    # Define model directories
    checkpoints_dir = comfyui_path / "models" / "checkpoints"
    vae_dir = comfyui_path / "models" / "vae"
    animatediff_dir = comfyui_path / "models" / "animatediff"
    
    # Create directories
    for directory in [checkpoints_dir, vae_dir, animatediff_dir]:
        directory.mkdir(parents=True, exist_ok=True)
    
    print("=" * 60)
    print("?? Downloading Models for ComfyUI AnimateDiff")
    print("=" * 60)
    
    # Models to download
    models = [
        {
            "name": "Stable Diffusion v1.5",
            "url": "https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned-emaonly.safetensors",
            "path": checkpoints_dir / "v1-5-pruned-emaonly.safetensors"
        },
        {
            "name": "VAE (ft-mse)",
            "url": "https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.safetensors",
            "path": vae_dir / "vae-ft-mse-840000-ema-pruned.safetensors"
        },
        {
            "name": "AnimateDiff Motion Module",
            "url": "https://huggingface.co/guoyww/animatediff/resolve/main/mm_sd_v15_v2.ckpt",
            "path": animatediff_dir / "mm_sd_v15_v2.ckpt"
        }
    ]
    
    # Download each model
    success_count = 0
    for model in models:
        print(f"\n{'=' * 60}")
        print(f"Model: {model['name']}")
        print(f"{'=' * 60}")
        if download_file(model['url'], model['path']):
            success_count += 1
    
    print(f"\n{'=' * 60}")
    print(f"? Download Complete: {success_count}/{len(models)} models")
    print(f"{'=' * 60}")
    
    if success_count == len(models):
        print("\n?? All models downloaded successfully!")
        print("\nNext step: Run ComfyUI server")
        print("  python run_comfyui.py")
    else:
        print("\n? Some models failed to download. Please retry or download manually.")
    
    return success_count == len(models)

if __name__ == "__main__":
    HOME = os.path.expanduser("~")
    PROJECT_DIR = os.getenv("COMFYUI_PROJECT_DIR", f"{HOME}/comfyui-animatediff")
    COMFYUI_PATH = Path(PROJECT_DIR) / "ComfyUI"
    
    if not COMFYUI_PATH.exists():
        print("? ComfyUI not found!")
        print(f"Expected location: {COMFYUI_PATH}")
        print("\nPlease run setup first:")
        print("  python setup_comfyui.py")
        sys.exit(1)
    
    download_models(COMFYUI_PATH)

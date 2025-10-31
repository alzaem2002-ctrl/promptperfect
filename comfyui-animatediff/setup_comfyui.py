#!/usr/bin/env python3
"""
ComfyUI Setup Script
This script clones and sets up ComfyUI for AnimateDiff video generation
"""

import os
import subprocess
import sys
from pathlib import Path

def run_command(cmd, cwd=None, check=True):
    """Run a shell command and handle errors"""
    print(f"Running: {cmd}")
    try:
        result = subprocess.run(
            cmd, 
            shell=True, 
            check=check, 
            cwd=cwd,
            capture_output=True,
            text=True
        )
        if result.stdout:
            print(result.stdout)
        return result
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print(f"Stderr: {e.stderr}")
        if check:
            sys.exit(1)
        return e

def check_gpu():
    """Check if GPU is available"""
    print("\n?? Checking GPU availability...")
    result = run_command("nvidia-smi", check=False)
    if result.returncode == 0:
        print("? GPU ????! (GPU available!)")
        return True
    else:
        print("? No GPU detected. ComfyUI will run on CPU (slower)")
        return False

def setup_comfyui(project_dir):
    """Clone and setup ComfyUI"""
    project_path = Path(project_dir).expanduser()
    project_path.mkdir(parents=True, exist_ok=True)
    
    comfyui_path = project_path / "ComfyUI"
    
    print(f"\n?? Setting up ComfyUI in: {comfyui_path}")
    
    # Clone ComfyUI if not already cloned
    if comfyui_path.exists():
        print("? ComfyUI directory already exists, updating...")
        run_command("git pull", cwd=comfyui_path)
    else:
        print("Cloning ComfyUI repository...")
        run_command(
            "git clone https://github.com/comfyanonymous/ComfyUI",
            cwd=project_path
        )
    
    # Install requirements
    print("\n?? Installing ComfyUI requirements...")
    requirements_file = comfyui_path / "requirements.txt"
    if requirements_file.exists():
        run_command(
            f"{sys.executable} -m pip install -r requirements.txt",
            cwd=comfyui_path
        )
    else:
        print("? requirements.txt not found, skipping...")
    
    # Create necessary directories
    print("\n?? Creating model directories...")
    dirs = [
        comfyui_path / "models" / "checkpoints",
        comfyui_path / "models" / "vae",
        comfyui_path / "models" / "animatediff",
        comfyui_path / "output",
    ]
    for directory in dirs:
        directory.mkdir(parents=True, exist_ok=True)
        print(f"  ? {directory}")
    
    print("\n? ComfyUI setup completed!")
    print(f"\nComfyUI installed at: {comfyui_path}")
    print("\nNext steps:")
    print("  1. Run: python download_models.py")
    print("  2. Run: python run_comfyui.py")
    
    return comfyui_path

if __name__ == "__main__":
    HOME = os.path.expanduser("~")
    PROJECT_DIR = os.getenv("COMFYUI_PROJECT_DIR", f"{HOME}/comfyui-animatediff")
    
    print("=" * 60)
    print("?? ComfyUI AnimateDiff Setup")
    print("=" * 60)
    
    check_gpu()
    setup_comfyui(PROJECT_DIR)

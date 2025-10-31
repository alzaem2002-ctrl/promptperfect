#!/usr/bin/env python3
"""
ComfyUI Server Launcher
Starts the ComfyUI server for AnimateDiff video generation
"""

import os
import sys
import subprocess
from pathlib import Path

def run_comfyui(comfyui_path, listen=True, port=8188):
    """Start ComfyUI server"""
    comfyui_path = Path(comfyui_path)
    
    if not comfyui_path.exists():
        print(f"? ComfyUI not found at: {comfyui_path}")
        print("\nPlease run setup first:")
        print("  python setup_comfyui.py")
        sys.exit(1)
    
    main_py = comfyui_path / "main.py"
    if not main_py.exists():
        print(f"? main.py not found at: {main_py}")
        sys.exit(1)
    
    print("=" * 60)
    print("?? Starting ComfyUI Server")
    print("=" * 60)
    print(f"ComfyUI Path: {comfyui_path}")
    print(f"Port: {port}")
    print(f"Listen on all interfaces: {listen}")
    print("=" * 60)
    
    # Build command
    cmd = [sys.executable, "main.py"]
    if listen:
        cmd.append("--listen")
    if port != 8188:
        cmd.extend(["--port", str(port)])
    
    print(f"\nCommand: {' '.join(cmd)}")
    print("\n?? Access ComfyUI at:")
    if listen:
        print("   http://localhost:8188")
        print("   http://127.0.0.1:8188")
        print("   http://<your-ip>:8188")
    else:
        print("   http://localhost:8188")
    
    print("\n?? Press Ctrl+C to stop the server\n")
    print("=" * 60)
    
    try:
        subprocess.run(cmd, cwd=comfyui_path, check=True)
    except KeyboardInterrupt:
        print("\n\n?? Server stopped by user")
    except subprocess.CalledProcessError as e:
        print(f"\n? Error running ComfyUI: {e}")
        sys.exit(1)

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Run ComfyUI Server")
    parser.add_argument("--no-listen", action="store_true", help="Don't listen on all interfaces")
    parser.add_argument("--port", type=int, default=8188, help="Port to run server on (default: 8188)")
    args = parser.parse_args()
    
    HOME = os.path.expanduser("~")
    PROJECT_DIR = os.getenv("COMFYUI_PROJECT_DIR", f"{HOME}/comfyui-animatediff")
    COMFYUI_PATH = Path(PROJECT_DIR) / "ComfyUI"
    
    run_comfyui(COMFYUI_PATH, listen=not args.no_listen, port=args.port)

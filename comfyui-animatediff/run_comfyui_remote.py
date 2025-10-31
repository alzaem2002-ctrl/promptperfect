#!/usr/bin/env python3
"""
ComfyUI Remote Server Launcher
Starts ComfyUI optimized for remote access with multiple tunneling options
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path

def check_port_available(port):
    """Check if port is available"""
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('localhost', port))
    sock.close()
    return result != 0

def start_comfyui(comfyui_path, host="0.0.0.0", port=8188, enable_auth=False):
    """Start ComfyUI server"""
    comfyui_path = Path(comfyui_path)
    
    if not comfyui_path.exists():
        print(f"? ComfyUI not found at: {comfyui_path}")
        sys.exit(1)
    
    main_py = comfyui_path / "main.py"
    if not main_py.exists():
        print(f"? main.py not found at: {main_py}")
        sys.exit(1)
    
    # Check if port is available
    if not check_port_available(port):
        print(f"??  Port {port} is already in use!")
        print(f"   Try another port with: --port XXXX")
        sys.exit(1)
    
    print("=" * 60)
    print("?? Starting ComfyUI Remote Server")
    print("=" * 60)
    print(f"ComfyUI Path: {comfyui_path}")
    print(f"Host: {host}")
    print(f"Port: {port}")
    print(f"Authentication: {'Enabled' if enable_auth else 'Disabled'}")
    print("=" * 60)
    
    # Build command
    cmd = [sys.executable, "main.py", "--listen", host, "--port", str(port)]
    
    print(f"\nCommand: {' '.join(cmd)}")
    print("\n?? Access ComfyUI at:")
    
    if host == "0.0.0.0":
        import socket
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        print(f"   http://localhost:{port}")
        print(f"   http://127.0.0.1:{port}")
        print(f"   http://{local_ip}:{port}")
        print(f"   http://{hostname}:{port}")
    else:
        print(f"   http://{host}:{port}")
    
    print("\n?? Press Ctrl+C to stop the server")
    
    # Security warning
    if host == "0.0.0.0" and not enable_auth:
        print("\n" + "=" * 60)
        print("??  SECURITY WARNING")
        print("=" * 60)
        print("Server is accessible from ANY IP address without authentication!")
        print("This is NOT recommended for production use.")
        print("\nTo add authentication, use nginx reverse proxy or")
        print("restrict access with firewall rules.")
        print("=" * 60)
    
    print()
    
    try:
        subprocess.run(cmd, cwd=comfyui_path, check=True)
    except KeyboardInterrupt:
        print("\n\n?? Server stopped by user")
    except subprocess.CalledProcessError as e:
        print(f"\n? Error running ComfyUI: {e}")
        sys.exit(1)

def start_with_ngrok(comfyui_path, port=8188):
    """Start ComfyUI with ngrok tunnel"""
    import threading
    import time
    
    print("?? Starting ComfyUI with Ngrok tunnel...")
    
    # Check if ngrok is installed
    if subprocess.run(["which", "ngrok"], capture_output=True).returncode != 0:
        print("? Ngrok not found!")
        print("\nInstall ngrok:")
        print("  wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz")
        print("  tar xvzf ngrok-v3-stable-linux-amd64.tgz")
        print("  sudo mv ngrok /usr/local/bin/")
        sys.exit(1)
    
    # Start ComfyUI in background thread
    def run_comfyui():
        cmd = [sys.executable, "main.py", "--listen", "127.0.0.1", "--port", str(port)]
        subprocess.run(cmd, cwd=Path(comfyui_path), check=True)
    
    comfyui_thread = threading.Thread(target=run_comfyui, daemon=True)
    comfyui_thread.start()
    
    # Wait for ComfyUI to start
    print("? Waiting for ComfyUI to start...")
    time.sleep(5)
    
    # Start ngrok
    print("?? Starting Ngrok tunnel...")
    ngrok_cmd = ["ngrok", "http", str(port)]
    
    try:
        subprocess.run(ngrok_cmd, check=True)
    except KeyboardInterrupt:
        print("\n?? Stopped")

def start_with_cloudflare(comfyui_path, port=8188):
    """Start ComfyUI with Cloudflare tunnel"""
    import threading
    import time
    import re
    
    print("??  Starting ComfyUI with Cloudflare tunnel...")
    
    # Check if cloudflared is installed
    if subprocess.run(["which", "cloudflared"], capture_output=True).returncode != 0:
        print("? Cloudflared not found!")
        print("\nInstall cloudflared:")
        print("  wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb")
        print("  sudo dpkg -i cloudflared-linux-amd64.deb")
        sys.exit(1)
    
    # Start ComfyUI in background thread
    def run_comfyui():
        cmd = [sys.executable, "main.py", "--listen", "127.0.0.1", "--port", str(port)]
        subprocess.run(cmd, cwd=Path(comfyui_path))
    
    comfyui_thread = threading.Thread(target=run_comfyui, daemon=True)
    comfyui_thread.start()
    
    # Wait for ComfyUI to start
    print("? Waiting for ComfyUI to start...")
    time.sleep(5)
    
    # Start cloudflare tunnel
    print("?? Starting Cloudflare tunnel...")
    print("=" * 60)
    
    process = subprocess.Popen(
        ["cloudflared", "tunnel", "--url", f"http://localhost:{port}"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True
    )
    
    # Print URL when found
    for line in process.stderr:
        print(line, end='')
        if 'trycloudflare.com' in line:
            url = re.search(r'https://[^\s]+trycloudflare.com', line)
            if url:
                print("\n" + "=" * 60)
                print("?? Access ComfyUI at:")
                print(f"?? {url.group(0)}")
                print("=" * 60 + "\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run ComfyUI Server for Remote Access",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic remote access
  python run_comfyui_remote.py
  
  # Custom port
  python run_comfyui_remote.py --port 8080
  
  # Localhost only (use with SSH tunnel)
  python run_comfyui_remote.py --host 127.0.0.1
  
  # With Ngrok
  python run_comfyui_remote.py --ngrok
  
  # With Cloudflare Tunnel
  python run_comfyui_remote.py --cloudflare
        """
    )
    
    parser.add_argument(
        "--host",
        type=str,
        default="0.0.0.0",
        help="Host to bind to (default: 0.0.0.0 for all interfaces)"
    )
    
    parser.add_argument(
        "--port",
        type=int,
        default=8188,
        help="Port to run server on (default: 8188)"
    )
    
    parser.add_argument(
        "--ngrok",
        action="store_true",
        help="Use Ngrok tunnel (requires ngrok installed)"
    )
    
    parser.add_argument(
        "--cloudflare",
        action="store_true",
        help="Use Cloudflare tunnel (requires cloudflared installed)"
    )
    
    args = parser.parse_args()
    
    HOME = os.path.expanduser("~")
    PROJECT_DIR = os.getenv("COMFYUI_PROJECT_DIR", f"{HOME}/comfyui-animatediff")
    COMFYUI_PATH = Path(PROJECT_DIR) / "ComfyUI"
    
    if not COMFYUI_PATH.exists():
        print("? ComfyUI not found!")
        print(f"Expected location: {COMFYUI_PATH}")
        print("\nPlease run setup first:")
        print("  python setup_comfyui.py")
        sys.exit(1)
    
    # Choose method
    if args.ngrok:
        start_with_ngrok(COMFYUI_PATH, args.port)
    elif args.cloudflare:
        start_with_cloudflare(COMFYUI_PATH, args.port)
    else:
        start_comfyui(COMFYUI_PATH, args.host, args.port)

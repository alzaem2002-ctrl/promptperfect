#!/usr/bin/env python3
"""
Interactive UI for ComfyUI - Terminal-based interface
This script provides a simple text-based interface to interact with ComfyUI
"""

import os
import sys
import json
import requests
from typing import Optional
import time


class ComfyUIClient:
    """Simple client to interact with ComfyUI API"""
    
    def __init__(self, host: str = "127.0.0.1", port: int = 8188):
        self.host = host
        self.port = port
        self.base_url = f"http://{host}:{port}"
        
    def is_server_running(self) -> bool:
        """Check if ComfyUI server is running"""
        try:
            response = requests.get(f"{self.base_url}/system_stats", timeout=2)
            return response.status_code == 200
        except:
            return False
    
    def get_queue_status(self):
        """Get current queue status"""
        try:
            response = requests.get(f"{self.base_url}/queue")
            return response.json()
        except Exception as e:
            return {"error": str(e)}
    
    def get_system_stats(self):
        """Get system statistics"""
        try:
            response = requests.get(f"{self.base_url}/system_stats")
            return response.json()
        except Exception as e:
            return {"error": str(e)}
    
    def get_models(self):
        """Get available models"""
        try:
            response = requests.get(f"{self.base_url}/object_info")
            return response.json()
        except Exception as e:
            return {"error": str(e)}


def print_header():
    """Print application header"""
    print("\n" + "="*60)
    print("       ComfyUI Interactive Terminal Interface")
    print("="*60)
    print()


def print_menu():
    """Print main menu"""
    print("\nAvailable Commands:")
    print("  1. Check Server Status")
    print("  2. View Queue Status")
    print("  3. View System Stats")
    print("  4. List Available Models")
    print("  5. Open Web UI")
    print("  6. Help")
    print("  0. Exit")
    print()


def check_server_status(client: ComfyUIClient):
    """Check and display server status"""
    print("\n?? Checking server status...")
    if client.is_server_running():
        print("? ComfyUI server is running!")
        print(f"  URL: {client.base_url}")
    else:
        print("? ComfyUI server is not running")
        print("\nTo start the server, run:")
        print("  cd ComfyUI && python main.py --listen")
        print("  or use: ./start_comfyui.sh")


def view_queue_status(client: ComfyUIClient):
    """Display queue status"""
    print("\n?? Queue Status:")
    status = client.get_queue_status()
    if "error" in status:
        print(f"? Error: {status['error']}")
    else:
        queue_running = status.get("queue_running", [])
        queue_pending = status.get("queue_pending", [])
        print(f"  Running tasks: {len(queue_running)}")
        print(f"  Pending tasks: {len(queue_pending)}")


def view_system_stats(client: ComfyUIClient):
    """Display system statistics"""
    print("\n?? System Statistics:")
    stats = client.get_system_stats()
    if "error" in stats:
        print(f"? Error: {stats['error']}")
    else:
        if "system" in stats:
            sys_info = stats["system"]
            print(f"  OS: {sys_info.get('os', 'Unknown')}")
            print(f"  Python: {sys_info.get('python_version', 'Unknown')}")
        if "devices" in stats:
            for device in stats["devices"]:
                print(f"  GPU: {device.get('name', 'Unknown')}")
                vram_total = device.get('vram_total', 0) / (1024**3)
                vram_free = device.get('vram_free', 0) / (1024**3)
                print(f"       VRAM: {vram_free:.2f}GB free / {vram_total:.2f}GB total")


def list_models(client: ComfyUIClient):
    """List available models"""
    print("\n?? Fetching available models...")
    models = client.get_models()
    if "error" in models:
        print(f"? Error: {models['error']}")
    else:
        print("? ComfyUI is ready with loaded models")
        print("  (Full model list available in web UI)")


def open_web_ui(client: ComfyUIClient):
    """Open web UI in browser"""
    print("\n?? Opening ComfyUI Web Interface...")
    url = client.base_url
    print(f"  URL: {url}")
    
    # Try to open in default browser
    try:
        import webbrowser
        webbrowser.open(url)
        print("? Browser opened")
    except:
        print("  Please open this URL in your browser manually")


def print_help():
    """Print help information"""
    print("\n" + "="*60)
    print("HELP - ComfyUI Interactive Interface")
    print("="*60)
    print("""
ComfyUI is a powerful node-based interface for Stable Diffusion.

Getting Started:
1. Make sure ComfyUI server is running (use option 1 to check)
2. Open the web interface (option 5) to create workflows
3. Use AnimateDiff nodes to create animated videos

Key Features:
- Node-based workflow editor
- AnimateDiff integration for video generation
- Multiple model support (SD 1.5, SDXL, etc.)
- ControlNet support
- Custom workflows with JSON

For more information:
- GitHub: https://github.com/comfyanonymous/ComfyUI
- Documentation: Check the GitHub wiki
- AnimateDiff: https://github.com/guoyww/AnimateDiff

Tips:
- Start with example workflows from the community
- Use the queue to batch process multiple generations
- Save your workflows for reuse
""")


def main():
    """Main application loop"""
    client = ComfyUIClient()
    
    print_header()
    
    # Initial server check
    if not client.is_server_running():
        print("??  ComfyUI server is not detected!")
        print("\nMake sure ComfyUI is running before using this interface.")
        print("To start the server:")
        print("  ./start_comfyui.sh")
        print("\nOr manually:")
        print("  cd ComfyUI && python main.py --listen")
        print("\nYou can still use this interface to check status and get help.")
    
    while True:
        print_menu()
        try:
            choice = input("Enter your choice (0-6): ").strip()
            
            if choice == "0":
                print("\n?? Goodbye!")
                break
            elif choice == "1":
                check_server_status(client)
            elif choice == "2":
                view_queue_status(client)
            elif choice == "3":
                view_system_stats(client)
            elif choice == "4":
                list_models(client)
            elif choice == "5":
                open_web_ui(client)
            elif choice == "6":
                print_help()
            else:
                print("? Invalid choice. Please try again.")
                
        except KeyboardInterrupt:
            print("\n\n?? Goodbye!")
            break
        except Exception as e:
            print(f"\n? Error: {e}")


if __name__ == "__main__":
    main()

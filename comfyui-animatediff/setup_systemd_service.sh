#!/bin/bash
# Script to setup ComfyUI as a systemd service

set -e

echo "======================================"
echo "?? ComfyUI Systemd Service Setup"
echo "======================================"

# Get current user
CURRENT_USER=$(whoami)
CURRENT_DIR=$(pwd)
COMFYUI_DIR="$CURRENT_DIR/ComfyUI"

# Check if ComfyUI exists
if [ ! -d "$COMFYUI_DIR" ]; then
    echo "? ComfyUI directory not found at: $COMFYUI_DIR"
    echo "Please run this script from the comfyui-animatediff directory"
    exit 1
fi

# Check if running as root for systemd
if [ "$EUID" -ne 0 ]; then 
    echo "??  This script needs sudo privileges to create systemd service"
    echo "Re-running with sudo..."
    sudo bash "$0" "$@"
    exit $?
fi

# Get the actual user (not root if using sudo)
if [ -n "$SUDO_USER" ]; then
    ACTUAL_USER=$SUDO_USER
else
    ACTUAL_USER=$CURRENT_USER
fi

ACTUAL_HOME=$(eval echo ~$ACTUAL_USER)

echo ""
echo "User: $ACTUAL_USER"
echo "Home: $ACTUAL_HOME"
echo "ComfyUI Dir: $COMFYUI_DIR"
echo ""

# Create service file
SERVICE_FILE="/etc/systemd/system/comfyui.service"

echo "?? Creating service file: $SERVICE_FILE"

cat > $SERVICE_FILE << EOF
[Unit]
Description=ComfyUI AnimateDiff Service
After=network.target

[Service]
Type=simple
User=$ACTUAL_USER
WorkingDirectory=$COMFYUI_DIR
ExecStart=/usr/bin/python3 main.py --listen 0.0.0.0 --port 8188
Restart=always
RestartSec=10
StandardOutput=journal
StandardError=journal

# Environment
Environment="PATH=/usr/local/bin:/usr/bin:/bin"
Environment="PYTHONUNBUFFERED=1"

[Install]
WantedBy=multi-user.target
EOF

echo "? Service file created"

# Reload systemd
echo "?? Reloading systemd daemon..."
systemctl daemon-reload

# Enable service
echo "? Enabling service..."
systemctl enable comfyui

echo ""
echo "======================================"
echo "? Service setup complete!"
echo "======================================"
echo ""
echo "To start the service:"
echo "  sudo systemctl start comfyui"
echo ""
echo "To check status:"
echo "  sudo systemctl status comfyui"
echo ""
echo "To view logs:"
echo "  sudo journalctl -u comfyui -f"
echo ""
echo "To stop the service:"
echo "  sudo systemctl stop comfyui"
echo ""
echo "To restart the service:"
echo "  sudo systemctl restart comfyui"
echo ""
echo "To disable auto-start on boot:"
echo "  sudo systemctl disable comfyui"
echo ""
echo "======================================"

# Ask if user wants to start now
read -p "Do you want to start the service now? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "?? Starting service..."
    systemctl start comfyui
    sleep 2
    systemctl status comfyui
fi

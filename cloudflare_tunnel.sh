#!/bin/bash

##############################################################################
# Cloudflare Tunnel Setup Script for ComfyUI
# Creates a secure public URL for accessing ComfyUI remotely
##############################################################################

set -e

echo "=========================================="
echo "Cloudflare Tunnel Setup for ComfyUI"
echo "=========================================="
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
COMFYUI_PORT=${COMFYUI_PORT:-8188}
INSTALL_DIR="/tmp/cloudflared"

# Function to print colored messages
print_status() {
    echo -e "${GREEN}[?]${NC} $1"
}

print_error() {
    echo -e "${RED}[?]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[!]${NC} $1"
}

print_info() {
    echo -e "${BLUE}[i]${NC} $1"
}

# Check if ComfyUI is running
check_comfyui() {
    print_info "Checking if ComfyUI is running on port ${COMFYUI_PORT}..."
    
    if curl -s http://localhost:${COMFYUI_PORT} > /dev/null 2>&1; then
        print_status "ComfyUI is running!"
        return 0
    else
        print_error "ComfyUI is not running on port ${COMFYUI_PORT}"
        echo ""
        echo "Please start ComfyUI first:"
        echo "  cd ComfyUI && python main.py --listen"
        echo ""
        return 1
    fi
}

# Install cloudflared
install_cloudflared() {
    print_info "Installing cloudflared..."
    
    # Detect OS and architecture
    OS=$(uname -s | tr '[:upper:]' '[:lower:]')
    ARCH=$(uname -m)
    
    case $ARCH in
        x86_64)
            ARCH="amd64"
            ;;
        aarch64|arm64)
            ARCH="arm64"
            ;;
        armv7l)
            ARCH="arm"
            ;;
        *)
            print_error "Unsupported architecture: $ARCH"
            return 1
            ;;
    esac
    
    # Check if cloudflared is already installed
    if command -v cloudflared &> /dev/null; then
        print_status "cloudflared is already installed"
        cloudflared --version
        return 0
    fi
    
    # Download based on OS
    mkdir -p "$INSTALL_DIR"
    cd "$INSTALL_DIR"
    
    if [ "$OS" = "linux" ]; then
        print_info "Downloading cloudflared for Linux ${ARCH}..."
        
        if [ "$ARCH" = "amd64" ]; then
            # For Debian/Ubuntu systems, use .deb
            if command -v dpkg &> /dev/null; then
                wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
                sudo dpkg -i cloudflared-linux-amd64.deb
            else
                # For other systems, use binary
                wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64
                chmod +x cloudflared-linux-amd64
                sudo mv cloudflared-linux-amd64 /usr/local/bin/cloudflared
            fi
        else
            wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-${ARCH}
            chmod +x cloudflared-linux-${ARCH}
            sudo mv cloudflared-linux-${ARCH} /usr/local/bin/cloudflared
        fi
        
    elif [ "$OS" = "darwin" ]; then
        print_info "Downloading cloudflared for macOS..."
        
        if command -v brew &> /dev/null; then
            brew install cloudflared
        else
            wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-darwin-amd64.tgz
            tar -xzf cloudflared-darwin-amd64.tgz
            chmod +x cloudflared
            sudo mv cloudflared /usr/local/bin/
        fi
    else
        print_error "Unsupported OS: $OS"
        return 1
    fi
    
    if command -v cloudflared &> /dev/null; then
        print_status "cloudflared installed successfully!"
        cloudflared --version
        return 0
    else
        print_error "Failed to install cloudflared"
        return 1
    fi
}

# Start Cloudflare Tunnel
start_tunnel() {
    print_info "Starting Cloudflare Tunnel..."
    echo ""
    echo "Creating secure tunnel to ComfyUI..."
    echo "This may take 10-15 seconds..."
    echo ""
    
    # Start tunnel and capture output
    cloudflared tunnel --url http://localhost:${COMFYUI_PORT} 2>&1 | while IFS= read -r line; do
        echo "$line"
        
        # Extract and highlight the URL
        if [[ $line == *"trycloudflare.com"* ]]; then
            URL=$(echo "$line" | grep -oP 'https://[a-zA-Z0-9-]+\.trycloudflare\.com')
            if [ ! -z "$URL" ]; then
                echo ""
                echo "=========================================="
                echo -e "${GREEN}? SUCCESS!${NC} Your ComfyUI is now public!"
                echo "=========================================="
                echo ""
                echo -e "${BLUE}?? Public URL:${NC}"
                echo -e "   ${GREEN}${URL}${NC}"
                echo ""
                echo -e "${BLUE}?? iPad Setup (Comfy Remote):${NC}"
                HOST=$(echo "$URL" | sed 's|https://||')
                echo "   Host: ${HOST}"
                echo "   Port: 443"
                echo "   HTTPS: ? Enable"
                echo ""
                echo -e "${BLUE}?? Direct Browser Access:${NC}"
                echo "   ${URL}"
                echo ""
                echo "=========================================="
                echo -e "${YELLOW}??  Keep this terminal running!${NC}"
                echo "     Press Ctrl+C to stop the tunnel"
                echo "=========================================="
                echo ""
            fi
        fi
    done
}

# Main execution
main() {
    echo ""
    
    # Check if ComfyUI is running
    if ! check_comfyui; then
        exit 1
    fi
    
    echo ""
    
    # Install cloudflared if needed
    if ! install_cloudflared; then
        exit 1
    fi
    
    echo ""
    echo "=========================================="
    echo "Starting Tunnel..."
    echo "=========================================="
    echo ""
    print_warning "Make sure ComfyUI stays running in another terminal"
    echo ""
    
    # Start the tunnel
    start_tunnel
}

# Handle Ctrl+C
trap 'echo ""; print_warning "Tunnel stopped. ComfyUI is still running locally."; exit 0' INT

# Run main function
main

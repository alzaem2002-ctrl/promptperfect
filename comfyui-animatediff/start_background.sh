#!/bin/bash

# ComfyUI-AnimateDiff Background Start Script
# This script starts ComfyUI with AnimateDiff support in the background

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}Starting ComfyUI-AnimateDiff in background...${NC}"

# Check if virtual environment exists
if [ -d "venv" ]; then
    echo -e "${YELLOW}Activating virtual environment...${NC}"
    source venv/bin/activate
elif [ -d ".venv" ]; then
    echo -e "${YELLOW}Activating virtual environment...${NC}"
    source .venv/bin/activate
fi

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: python3 not found${NC}"
    exit 1
fi

# Create logs directory if it doesn't exist
mkdir -p logs

# Start ComfyUI in background with nohup
LOG_FILE="logs/comfyui_$(date +%Y%m%d_%H%M%S).log"
echo -e "${GREEN}Logging to: $LOG_FILE${NC}"

# Try to start ComfyUI
if [ -f "main.py" ]; then
    # If main.py exists in current directory
    nohup python3 main.py > "$LOG_FILE" 2>&1 &
elif [ -f "comfyui/main.py" ]; then
    # If main.py exists in comfyui subdirectory
    nohup python3 comfyui/main.py > "$LOG_FILE" 2>&1 &
else
    echo -e "${YELLOW}Warning: main.py not found. Attempting to run ComfyUI from current directory...${NC}"
    # Try running with python -m if installed as package
    nohup python3 -m comfyui > "$LOG_FILE" 2>&1 &
fi

PID=$!
echo -e "${GREEN}ComfyUI-AnimateDiff started in background with PID: $PID${NC}"
echo -e "${YELLOW}Check logs at: $LOG_FILE${NC}"
echo -e "${GREEN}To stop, run: kill $PID${NC}"

# Save PID to file for easier management
echo $PID > .comfyui_pid
echo -e "${GREEN}PID saved to .comfyui_pid${NC}"

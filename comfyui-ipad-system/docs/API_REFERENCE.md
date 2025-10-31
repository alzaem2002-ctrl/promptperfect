# ?? API Reference - ???? ComfyUI

> ???? ???? ?? API ????? ??????? ????? ?????? iPad

## ?? ?????????

1. [ComfyUI API](#1-comfyui-api)
2. [Cursor Agent API](#2-cursor-agent-api)
3. [iPad Controller API](#3-ipad-controller-api)

---

## 1. ComfyUI API

ComfyUI ???? REST API ??? ?????? 8188.

### ???? ??????? ????????

#### GET `/system_stats`

?????? ??? ???????? ??????.

**????:**
```bash
curl http://localhost:8188/system_stats
```

**?????????:**
```json
{
  "system": {
    "os": "Linux",
    "python_version": "3.10.12",
    "comfyui_version": "0.3.67"
  },
  "devices": [
    {
      "name": "NVIDIA GeForce RTX 3060",
      "type": "cuda",
      "vram_total": 12884901888,
      "vram_free": 10737418240
    }
  ]
}
```

#### POST `/prompt`

????? prompt ???? ???????.

**????:**
```bash
curl -X POST http://localhost:8188/prompt \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": {
      "3": {
        "inputs": {
          "seed": 42,
          "steps": 20,
          "cfg": 7.5,
          "sampler_name": "euler",
          "scheduler": "normal",
          "denoise": 1.0,
          "model": ["4", 0],
          "positive": ["6", 0],
          "negative": ["7", 0],
          "latent_image": ["5", 0]
        },
        "class_type": "KSampler"
      }
    }
  }'
```

**?????????:**
```json
{
  "prompt_id": "12345678-1234-1234-1234-123456789abc",
  "number": 1,
  "node_errors": {}
}
```

#### GET `/history`

?????? ??? ????? ???????.

```bash
curl http://localhost:8188/history
```

#### GET `/queue`

?????? ??? ????? ???????? ???????.

```bash
curl http://localhost:8188/queue
```

#### WebSocket `/ws`

????? WebSocket ????????? ?????.

**???? (JavaScript):**
```javascript
const ws = new WebSocket('ws://localhost:8188/ws');

ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  console.log('Update:', data);
};
```

---

## 2. Cursor Agent API

?????? ????? ???? ????? Python.

### ????????? ???????

```python
from automation.cursor_agent import ComfyUIAgent

# ????? instance
agent = ComfyUIAgent(
    comfyui_dir="/path/to/ComfyUI",
    host="localhost",
    port=8188
)

# ?????? ?? ?????
if agent.check_health():
    print("ComfyUI ???? ?")

# ??? ??????
agent.start_comfyui()

# ?????? ??? ???????? ??????
stats = agent.get_system_stats()
print(f"CPU: {stats['cpu']}%")
print(f"Memory: {stats['memory']['percent']}%")

# ????? ???????
agent.restart_comfyui()

# ??????? (??? ????? ???? ?? 7 ????)
agent.cleanup_old_outputs(days=7)

# ??? ???????
agent.backup_workflows()

# ?????? ?????? (???? ????????)
agent.monitor(interval=60)
```

### ?????? ????????

#### `ComfyUIAgent.__init__(comfyui_dir, host, port)`

????? instance ????.

**?????????:**
- `comfyui_dir` (str): ???? ComfyUI
- `host` (str): ??? ?????? (???????: "localhost")
- `port` (int): ??? ?????? (???????: 8188)

#### `check_health() -> bool`

?????? ?? ??? ??????.

**??????:** `True` ??? ??? ????? `False` ???? ???.

#### `start_comfyui() -> bool`

??? ???? ComfyUI.

**??????:** `True` ??? ??? ?????.

#### `stop_comfyui()`

????? ???? ComfyUI.

#### `restart_comfyui() -> bool`

????? ????? ??????.

#### `get_system_stats() -> dict`

?????? ??? ???????? ??????.

**??????:**
```python
{
    "cpu": 45.2,  # ???? ?????
    "memory": {
        "total": 16.0,  # GB
        "used": 8.5,
        "percent": 53.1
    },
    "disk": {
        "total": 500.0,
        "used": 250.0,
        "percent": 50.0
    }
}
```

#### `monitor(interval=60)`

?????? ??????.

**?????????:**
- `interval` (int): ???? ????? ????????

#### `cleanup_old_outputs(days=7)`

????? ??????? ???????.

**?????????:**
- `days` (int): ??? ????? ???? ?? ??? ????? ?? ??????

#### `backup_workflows()`

??? ??????? ??? workflows.

---

## 3. iPad Controller API

????? iPad ?????? JavaScript ???????.

### JavaScript Functions

#### `connect()`

??????? ????? ComfyUI.

```javascript
function connect() {
    const ip = document.getElementById('serverIp').value;
    const port = document.getElementById('serverPort').value;
    serverUrl = `http://${ip}:${port}`;
    
    fetch(`${serverUrl}/system_stats`)
        .then(response => response.json())
        .then(data => {
            isConnected = true;
            updateConnectionStatus(true);
        })
        .catch(error => {
            updateConnectionStatus(false);
        });
}
```

#### `generate()`

????? ???? ?????.

```javascript
async function generate() {
    const prompt = document.getElementById('promptInput').value;
    const negativePrompt = document.getElementById('negativePrompt').value;
    
    // ????? ?????
    const workflow = buildWorkflow(prompt, negativePrompt);
    
    const response = await fetch(`${serverUrl}/prompt`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ prompt: workflow })
    });
    
    const result = await response.json();
    console.log('Prompt ID:', result.prompt_id);
}
```

#### `buildWorkflow(prompt, negativePrompt)`

???? workflow ComfyUI.

```javascript
function buildWorkflow(prompt, negativePrompt) {
    return {
        "3": {
            "inputs": {
                "seed": Math.floor(Math.random() * 1000000),
                "steps": 20,
                "cfg": 7.5,
                "sampler_name": "euler",
                "scheduler": "normal",
                "denoise": 1.0,
                "model": ["4", 0],
                "positive": ["6", 0],
                "negative": ["7", 0],
                "latent_image": ["5", 0]
            },
            "class_type": "KSampler"
        },
        "4": {
            "inputs": {
                "ckpt_name": "v1-5-pruned-emaonly.safetensors"
            },
            "class_type": "CheckpointLoaderSimple"
        },
        "5": {
            "inputs": {
                "width": 512,
                "height": 512,
                "batch_size": 1
            },
            "class_type": "EmptyLatentImage"
        },
        "6": {
            "inputs": {
                "text": prompt,
                "clip": ["4", 1]
            },
            "class_type": "CLIPTextEncode"
        },
        "7": {
            "inputs": {
                "text": negativePrompt,
                "clip": ["4", 1]
            },
            "class_type": "CLIPTextEncode"
        },
        "8": {
            "inputs": {
                "samples": ["3", 0],
                "vae": ["4", 2]
            },
            "class_type": "VAEDecode"
        },
        "9": {
            "inputs": {
                "filename_prefix": "ComfyUI",
                "images": ["8", 0]
            },
            "class_type": "SaveImage"
        }
    };
}
```

### WebSocket ????????? ?????

```javascript
let ws = null;

function connectWebSocket() {
    ws = new WebSocket(`ws://${serverIp}:${serverPort}/ws`);
    
    ws.onmessage = (event) => {
        const data = JSON.parse(event.data);
        
        switch(data.type) {
            case 'status':
                updateStatus(data.data);
                break;
            case 'progress':
                updateProgress(data.data);
                break;
            case 'executing':
                console.log('Executing node:', data.data.node);
                break;
            case 'executed':
                console.log('Completed!');
                displayResults(data.data);
                break;
        }
    };
    
    ws.onerror = (error) => {
        console.error('WebSocket error:', error);
    };
    
    ws.onclose = () => {
        console.log('WebSocket closed');
        // ????? ??????? ??? 5 ?????
        setTimeout(connectWebSocket, 5000);
    };
}
```

---

## ?? ????? ?????

### ???? 1: ????? ???? ???????

```python
import requests
import json
import time

# ????? ???????
base_url = "http://localhost:8188"

# ???? ??? workflow
workflow = {
    "3": {
        "inputs": {
            "seed": 42,
            "steps": 20,
            "cfg": 7.5,
            "sampler_name": "euler",
            "scheduler": "normal",
            "denoise": 1.0,
            "model": ["4", 0],
            "positive": ["6", 0],
            "negative": ["7", 0],
            "latent_image": ["5", 0]
        },
        "class_type": "KSampler"
    },
    "4": {
        "inputs": {"ckpt_name": "v1-5-pruned-emaonly.safetensors"},
        "class_type": "CheckpointLoaderSimple"
    },
    "5": {
        "inputs": {"width": 512, "height": 512, "batch_size": 1},
        "class_type": "EmptyLatentImage"
    },
    "6": {
        "inputs": {
            "text": "beautiful sunset over mountains, cinematic, 8k",
            "clip": ["4", 1]
        },
        "class_type": "CLIPTextEncode"
    },
    "7": {
        "inputs": {
            "text": "ugly, blurry, low quality",
            "clip": ["4", 1]
        },
        "class_type": "CLIPTextEncode"
    },
    "8": {
        "inputs": {"samples": ["3", 0], "vae": ["4", 2]},
        "class_type": "VAEDecode"
    },
    "9": {
        "inputs": {"filename_prefix": "API_Test", "images": ["8", 0]},
        "class_type": "SaveImage"
    }
}

# ????? ?????
response = requests.post(
    f"{base_url}/prompt",
    json={"prompt": workflow}
)

result = response.json()
prompt_id = result['prompt_id']

print(f"Prompt ID: {prompt_id}")

# ?????? ??????
while True:
    queue = requests.get(f"{base_url}/queue").json()
    
    # ?????? ??? ?????
    if not any(item['prompt_id'] == prompt_id for item in queue['queue_running']):
        break
    
    print("Generating...")
    time.sleep(2)

print("Done! Check the output folder.")
```

### ???? 2: ?????? ??????

```python
from automation.cursor_agent import ComfyUIAgent
import time

agent = ComfyUIAgent("/path/to/ComfyUI")

while True:
    if not agent.check_health():
        print("?? ComfyUI down! Restarting...")
        agent.start_comfyui()
    
    stats = agent.get_system_stats()
    print(f"CPU: {stats['cpu']}% | Memory: {stats['memory']['percent']}%")
    
    time.sleep(60)
```

---

## ?? ????? ?????

- [ComfyUI Official API Docs](https://github.com/comfyanonymous/ComfyUI/wiki/API)
- [Examples Repository](https://github.com/comfyanonymous/ComfyUI_examples)

---

<div align="center">

[?????? ??????](USER_GUIDE_AR.md) ? [?????? ????????](../README.md)

</div>

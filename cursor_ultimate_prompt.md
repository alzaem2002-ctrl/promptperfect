# البرومبت الشامل والحاسم لـ Cursor Agent  
**لتوليد فيديو احترافي من الصور بلا قيود على iPad Air**

***

## المرحلة 1: فحص وتهيئة البيئة الأساسية

```bash
python --version            # يجب أن يكون 3.10+  
pip --version  
df -h                       # تحقق من أن لديك 50GB+ مساحة  
git --version
mkdir -p ~/comfyui-animatediff-pro
cd ~/comfyui-animatediff-pro
python3.10 -m venv venv
source venv/bin/activate
pip install --upgrade pip setuptools wheel
```

***

## المرحلة 2: تثبيت ComfyUI

```bash
git clone https://github.com/comfyanonymous/ComfyUI.git
cd ComfyUI
pip install -r requirements.txt
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
python -c "import torch; print(torch.__version__); print(torch.cuda.is_available())"
cd ..
```

***

## المرحلة 3: تثبيت AnimateDiff Evolved

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git
git clone https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet.git
git clone https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite.git
cd ../..
```

***

## المرحلة 4: إنشاء هيكلة المجلدات

```bash
mkdir -p ComfyUI/models/checkpoints
mkdir -p ComfyUI/models/vae
mkdir -p ComfyUI/models/animatediff_models
mkdir -p ComfyUI/models/animatediff_motion_lora
mkdir -p ComfyUI/custom_nodes/ComfyUI-AnimateDiff-Evolved/models
mkdir -p ComfyUI/custom_nodes/ComfyUI-AnimateDiff-Evolved/motion_lora
mkdir -p ComfyUI/output
find ComfyUI -type d -name "checkpoints" -o -name "vae" -o -name "models"
```

***

## المرحلة 5: تحميل النماذج الأساسية

```bash
wget -P ComfyUI/models/animatediff_models/ https://huggingface.co/guoyww/animatediff/resolve/main/v3_sd15_mm.safetensors
wget -P ComfyUI/models/checkpoints/ https://huggingface.co/SG161222/Realistic_Vision_V6.0_B1/resolve/main/Realistic_Vision_V6.0_B1_fp16.safetensors
wget -P ComfyUI/models/vae/ https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae.safetensors
ls -lh ComfyUI/models/checkpoints/
ls -lh ComfyUI/models/animatediff_models/
ls -lh ComfyUI/models/vae/
```

***

## المرحلة 6: إنشاء سكريبت التشغيل

**املأ ملف باسم** `run_animatediff.py` **بالمحتوى التالي:**

```python
#!/usr/bin/env python3
import json, subprocess, time, sys

def create_workflow():
    workflow = {
        "1": {"inputs": {"ckpt_name": "Realistic_Vision_V6.0_B1_fp16.safetensors"}, "class_type": "CheckpointLoaderSimple"},
        "2": {"inputs": {"text": "stunning cinematic landscape, mountains, sunrise, 8k, masterpiece"}, "class_type": "CLIPTextEncode"},
        "3": {"inputs": {"text": "low quality, worst quality, blurry, watermark"}, "class_type": "CLIPTextEncode"},
        "4": {"inputs": {"motion_model_name": "v3_sd15_mm.safetensors"}, "class_type": "AnimateDiffLoaderV3"},
        "5": {"inputs": {"context_length": 16, "context_stride": 1, "context_overlap": 4, "closed_loop": False, "motion_scale": 1.0, "beta_schedule": "sqrt_linear"}, "class_type": "ADE_AnimateDiffOptions"},
        "6": {"inputs": {"seed": 42, "steps": 20, "cfg": 7.5, "sampler_name": "euler", "scheduler": "normal", "denoise": 1.0, "model": ["1", 0], "positive": ["2", 0], "negative": ["3", 0], "latent_image": ["5", 0]}, "class_type": "KSampler"},
        "7": {"inputs": {"samples": ["6", 0]}, "class_type": "VAEDecode"},
        "8": {"inputs": {"images": ["7", 0], "frame_rate": 8, "format": "video/h264-mp4", "crf": 21, "filename_prefix": "animatediff"}, "class_type": "VHS_VideoCombine"}
    }
    return workflow

def start_server():
    print("Starting ComfyUI server...")
    subprocess.Popen([sys.executable, "ComfyUI/main.py"])
    time.sleep(10)

def save_workflow():
    workflow = create_workflow()
    with open('workflow.json', 'w') as f:
        json.dump(workflow, f, indent=2)
    print("✓ Workflow saved to workflow.json")

if __name__ == "__main__":
    save_workflow()
    start_server()
    print("✓ ComfyUI is running at http://127.0.0.1:8188")
```

```bash
chmod +x run_animatediff.py
python run_animatediff.py
```

***

## المرحلة 7: اختبار النظام

```bash
source venv/bin/activate
cd ComfyUI
python main.py
curl http://127.0.0.1:8188/system_stats
ls -la models/checkpoints/
ls -la models/animatediff_models/
```

***

## المرحلة 8: إنشـاء README

```markdown
# ComfyUI AnimateDiff Pro

نظام احترافي لتوليد الفيديو من الصور

## الميزات
- فيديو بجودة عالية
- تحكم في الحركة
- بلا قيود للفيديو
- أتمتة كاملة

## البدء السريع
source venv/bin/activate
python run_animatediff.py
```

***

## إعدادات Cursor Agent

1. Settings > Features > Agent Mode > Enable
2. Settings > Beta > YOLO Mode > Enable
3. Allowlist: git, pip, python, mkdir, wget, curl
4. Claude 3.5 Sonnet أو أحدث
5. Full Codebase Context

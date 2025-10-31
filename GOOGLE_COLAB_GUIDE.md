# دليل نقل مشروع ComfyUI إلى Google Colab

## 🎯 لماذا Google Colab؟

### المميزات:
- ✅ **GPU مجاني** (T4 - أسرع 10-20x من CPU)
- ✅ **وصول من أي مكان** (بما في ذلك iPad)
- ✅ **لا حاجة لتثبيت محلي**
- ✅ **مساحة تخزين مؤقتة**
- ✅ **جاهز للاستخدام خلال دقائق**

### العيوب:
- ⏱️ **جلسة محدودة** (12 ساعة كحد أقصى)
- 💾 **الملفات تُحذف** بعد انتهاء الجلسة
- 🔄 **يجب إعادة التثبيت** في كل جلسة جديدة

---

## 📦 طريقة 1: Notebook جاهز للنسخ واللصق

### إنشاء Notebook جديد:

1. افتح https://colab.research.google.com
2. اضغط **New Notebook**
3. غير اسم الملف إلى: `ComfyUI_AnimateDiff.ipynb`
4. انسخ الكود التالي في الخلايا:

---

### Cell 1: التحقق من GPU وإعداد البيئة

```python
# التحقق من GPU
!nvidia-smi

import os
import subprocess

# إعداد المتغيرات
HOME = os.path.expanduser("~")
PROJECT_DIR = f"{HOME}/comfyui-animatediff"

print(f"✓ GPU متاح!")
print(f"✓ المجلد: {PROJECT_DIR}")
```

---

### Cell 2: تثبيت ComfyUI

```python
%%capture
# إنشاء المجلد وتثبيت ComfyUI
!mkdir -p {PROJECT_DIR}
%cd {PROJECT_DIR}

# استنساخ ComfyUI
!git clone https://github.com/comfyanonymous/ComfyUI.git
%cd ComfyUI

# تثبيت المتطلبات
!pip install -r requirements.txt

print("✓ تم تثبيت ComfyUI")
```

---

### Cell 3: تثبيت Custom Nodes

```python
%%capture
%cd {PROJECT_DIR}/ComfyUI/custom_nodes

# استنساخ الملحقات
!git clone https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git
!git clone https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet.git
!git clone https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite.git

# تثبيت متطلبات VideoHelper
%cd ComfyUI-VideoHelperSuite
!pip install -r requirements.txt

print("✓ تم تثبيت جميع الملحقات")
```

---

### Cell 4: إنشاء هيكلة المجلدات

```python
import os

%cd {PROJECT_DIR}/ComfyUI

# إنشاء المجلدات
folders = [
    "models/checkpoints",
    "models/vae",
    "models/animatediff_models",
    "models/animatediff_motion_lora",
    "output"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)
    
print("✓ تم إنشاء جميع المجلدات")
```

---

### Cell 5: تحميل النماذج

```python
import gdown

%cd {PROJECT_DIR}/ComfyUI/models

# تحميل Stable Diffusion 1.5
print("⏳ تحميل Stable Diffusion 1.5...")
!wget -q --show-progress -P checkpoints/ \
  https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned-emaonly.safetensors

# تحميل AnimateDiff v2
print("⏳ تحميل AnimateDiff v2...")
!wget -q --show-progress -P animatediff_models/ \
  https://huggingface.co/guoyww/animatediff/resolve/main/mm_sd_v15_v2.ckpt

# تحميل VAE
print("⏳ تحميل VAE...")
!wget -q --show-progress -P vae/ \
  https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.safetensors

print("✓ تم تحميل جميع النماذج!")
```

---

### Cell 6: إنشاء Workflow

```python
import json

workflow = {
    "1": {"inputs": {"ckpt_name": "v1-5-pruned-emaonly.safetensors"}, "class_type": "CheckpointLoaderSimple"},
    "2": {"inputs": {"text": "stunning cinematic landscape, mountains, sunrise, 8k, masterpiece", "clip": ["1", 1]}, "class_type": "CLIPTextEncode"},
    "3": {"inputs": {"text": "low quality, worst quality, blurry, watermark", "clip": ["1", 1]}, "class_type": "CLIPTextEncode"},
    "4": {"inputs": {"model_name": "mm_sd_v15_v2.ckpt"}, "class_type": "ADE_LoadAnimateDiffModel"},
    "5": {"inputs": {"batch_size": 16, "width": 512, "height": 512}, "class_type": "EmptyLatentImage"},
    "6": {"inputs": {"seed": 42, "steps": 20, "cfg": 7.5, "sampler_name": "euler", "scheduler": "normal", "denoise": 1.0, "model": ["4", 0], "positive": ["2", 0], "negative": ["3", 0], "latent_image": ["5", 0]}, "class_type": "KSampler"},
    "7": {"inputs": {"samples": ["6", 0], "vae": ["1", 2]}, "class_type": "VAEDecode"},
    "8": {"inputs": {"images": ["7", 0], "frame_rate": 8, "loop_count": 0, "filename_prefix": "animatediff", "format": "video/h264-mp4", "pix_fmt": "yuv420p", "crf": 19, "save_metadata": True}, "class_type": "VHS_VideoCombine"}
}

%cd {PROJECT_DIR}
with open('workflow.json', 'w') as f:
    json.dump(workflow, f, indent=2)
    
print("✓ تم إنشاء workflow.json")
```

---

### Cell 7: تشغيل ComfyUI مع Cloudflared (للوصول من iPad)

```python
import subprocess
import threading
import time

%cd {PROJECT_DIR}/ComfyUI

# تثبيت cloudflared
!wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
!dpkg -i cloudflared-linux-amd64.deb

# دالة لتشغيل ComfyUI
def run_comfyui():
    subprocess.run(["python", "main.py", "--listen", "0.0.0.0", "--port", "8188"])

# بدء ComfyUI في thread منفصل
thread = threading.Thread(target=run_comfyui, daemon=True)
thread.start()

# انتظر قليلاً
time.sleep(10)

# تشغيل cloudflared للحصول على رابط عام
print("🚀 تشغيل cloudflared...")
print("⏳ انتظر حتى يظهر رابط https://...")
!cloudflared tunnel --url http://localhost:8188
```

---

### Cell 8 (اختياري): تحميل الفيديوهات المُنتجة

```python
from google.colab import files
import os

# عرض الفيديوهات المتاحة
output_dir = f"{PROJECT_DIR}/ComfyUI/output"
videos = [f for f in os.listdir(output_dir) if f.endswith('.mp4')]

print(f"📹 الفيديوهات المتاحة: {len(videos)}")
for video in videos:
    print(f"  • {video}")

# تحميل فيديو محدد
if videos:
    video_path = os.path.join(output_dir, videos[-1])
    print(f"\n⏬ تحميل: {videos[-1]}")
    files.download(video_path)
```

---

## 🎬 كيفية الاستخدام:

### 1. نسخ الكود:
- انسخ كل cell أعلاه إلى خلية منفصلة في Colab
- رتب الخلايا بنفس الترتيب

### 2. تفعيل GPU:
- اذهب لـ **Runtime > Change runtime type**
- اختر **GPU** في Hardware accelerator
- اضغط **Save**

### 3. التشغيل:
- شغّل الخلايا من 1 إلى 7 بالترتيب
- انتظر حتى يظهر رابط cloudflared
- انسخ الرابط وافتحه من iPad Safari

### 4. الاستخدام:
- الواجهة ستفتح في متصفح
- اسحب workflow.json (إذا احتجت)
- أو استخدم الواجهة مباشرة
- اضغط "Queue Prompt"
- انتظر التوليد (1-3 دقائق على GPU!)

---

## 📦 طريقة 2: Notebook جاهز من GitHub

يمكنك استخدام notebooks جاهزة:

```python
# في Colab
!git clone https://github.com/camenduru/ComfyUI-colab
# اتبع التعليمات في README
```

أو ابحث في GitHub عن:
- "ComfyUI Colab"
- "AnimateDiff Colab"

---

## 🔄 حفظ النماذج لتجنب إعادة التحميل

### استخدام Google Drive:

```python
from google.colab import drive
drive.mount('/content/drive')

# إنشاء مجلد في Drive
!mkdir -p /content/drive/MyDrive/ComfyUI_Models

# نسخ النماذج
!cp -r {PROJECT_DIR}/ComfyUI/models/* /content/drive/MyDrive/ComfyUI_Models/

# في الجلسة التالية، استخدم:
!cp -r /content/drive/MyDrive/ComfyUI_Models/* {PROJECT_DIR}/ComfyUI/models/
```

---

## ⚡ مقارنة الأداء

| البيئة | الوقت لفيديو 16 إطار |
|--------|---------------------|
| **CPU (المحلي)** | 5-15 دقيقة |
| **Colab T4 GPU** | 1-3 دقائق |
| **Colab A100 GPU (Pro)** | 30-60 ثانية |

---

## 🎯 نصائح مهمة:

### 1. إدارة الجلسة:
- Colab يقطع الاتصال بعد 90 دقيقة من عدم النشاط
- استخدم Extensions لإبقاء الجلسة نشطة
- أو اضغط Ctrl+Shift+I وأضف هذا في Console:
```javascript
function KeepAlive() {
    console.log("Keeping alive...");
}
setInterval(KeepAlive, 60000);
```

### 2. حفظ العمل:
- احفظ الفيديوهات فوراً بعد التوليد
- استخدم Google Drive لحفظ النماذج
- اعمل backup للـ workflows

### 3. تحسين السرعة:
- استخدم دقة 512x512 (أسرع)
- قلل عدد الخطوات إلى 15-20
- استخدم samplers سريعة (euler, ddim)

---

## 🆚 مقارنة: Cursor vs Colab

| الميزة | Cursor Remote | Google Colab |
|--------|--------------|--------------|
| **GPU** | ❌ CPU فقط | ✅ T4 GPU مجاني |
| **السرعة** | بطيء (5-15 دقيقة) | سريع (1-3 دقائق) |
| **الاستمرارية** | ✅ دائم | ⏱️ جلسة مؤقتة |
| **الوصول** | يحتاج ngrok | ✅ رابط مباشر |
| **التخزين** | ✅ دائم | ⚠️ مؤقت |
| **التكلفة** | حسب Cursor | مجاني (محدود) |

---

## 🚀 التوصية:

### للاستخدام السريع والتجريب:
✅ **استخدم Google Colab** - أسرع بكثير!

### للإنتاج والعمل الطويل:
✅ **استخدم الخادم المحلي/VPS** - أكثر استقراراً

### الحل الأمثل:
- **طور على Colab** (سريع للتجربة)
- **أنتج على خادم دائم** (للعمل الجاد)

---

## 📱 الوصول من iPad:

### مع Colab:
1. شغّل الـ notebook
2. انتظر رابط cloudflared
3. افتح الرابط من Safari على iPad
4. استخدم الواجهة كاملة!

### مميزات إضافية:
- ✅ لا حاجة لـ SSH apps
- ✅ رابط مباشر من المتصفح
- ✅ يعمل من أي مكان
- ✅ GPU مجاني!

---

## 🎬 الخلاصة:

**Google Colab = أفضل خيار للاستخدام من iPad!**

- سريع (GPU مجاني)
- سهل الإعداد (5-10 دقائق)
- وصول مباشر (بدون SSH)
- مثالي للتجريب والتطوير

**فقط انسخ الكود أعلاه إلى Colab وابدأ! 🚀**

---

**تاريخ التحديث**: 2025-10-31  
**الإصدار**: 1.0

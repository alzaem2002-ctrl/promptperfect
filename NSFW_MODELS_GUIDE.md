# 🔞 دليل النماذج غير المقيدة (NSFW Models)

## ⚠️ **إخلاء المسؤولية**
هذا الدليل للأغراض التعليمية فقط. استخدم هذه التقنيات بمسؤولية وفقاً لقوانين بلدك.

---

## ✅ **الوضع الحالي لنظامك**

### **ComfyUI = غير مقيد بشكل افتراضي**
✅ ComfyUI **لا يحتوي** على أي فلاتر مدمجة للمحتوى  
✅ **SD 1.5** المثبت حالياً هو نموذج مفتوح **بدون رقابة**  
✅ يمكنك توليد أي محتوى بحرية تامة  

**القيود الوحيدة تأتي من:**
- جودة النموذج (SD 1.5 ليس الأفضل للواقعية)
- مهارتك في كتابة الـ prompts
- قدرة GPU المتاحة

---

## 🎯 **النماذج المتخصصة (أفضل جودة)**

### **1. نماذج SDXL غير المقيدة**

#### **Realistic Vision XL**
- **الحجم:** ~6.5 GB
- **المميزات:** واقعية فوتوغرافية عالية
- **الاستخدام:** صور واقعية للبشر
```bash
https://civitai.com/models/4201/realistic-vision-v60-b1
```

#### **DreamShaper XL**
- **الحجم:** ~6.5 GB
- **المميزات:** توازن بين الواقعية والفن
```bash
https://civitai.com/models/112902/dreamshaper-xl
```

#### **Juggernaut XL**
- **الحجم:** ~6.5 GB
- **المميزات:** جودة عالية جداً، تفاصيل دقيقة
```bash
https://civitai.com/models/133005/juggernaut-xl
```

---

### **2. نماذج SD 1.5 المحسّنة**

#### **Deliberate v2**
- **الحجم:** ~2 GB
- **المميزات:** جودة عالية، سريع
```bash
https://civitai.com/models/4823/deliberate
```

#### **Perfect World**
- **الحجم:** ~2 GB
- **المميزات:** أسلوب آسيوي واقعي
```bash
https://civitai.com/models/8281/perfect-world
```

---

### **3. نماذج Anime/Hentai**

#### **AnyLora Checkpoint**
- **الحجم:** ~2 GB
- **المميزات:** أنمي عالي الجودة
```bash
https://civitai.com/models/23900/anylora-checkpoint
```

#### **Counterfeit V3**
- **الحجم:** ~2 GB
- **المميزات:** أسلوب أنمي احترافي
```bash
https://civitai.com/models/4468/counterfeit-v30
```

---

## 📥 **كيفية تثبيت النماذج الجديدة**

### **للخادم المحلي (~/comfyui-animatediff-pro):**

```bash
cd ~/comfyui-animatediff-pro/ComfyUI/models/checkpoints

# مثال: تحميل Deliberate v2
wget -O deliberate_v2.safetensors "https://civitai.com/api/download/models/[MODEL_ID]"
```

### **لـ Google Colab:**

أضف في **Cell 5** (بعد سطر SD 1.5):
```python
# تحميل نموذج إضافي
!wget -O checkpoints/deliberate_v2.safetensors "https://civitai.com/api/download/models/[MODEL_ID]"
```

---

## 🔄 **كيفية استخدام النموذج الجديد**

### **في ComfyUI Web Interface:**

1. افتح ComfyUI في المتصفح
2. ابحث عن عقدة **CheckpointLoaderSimple**
3. اضغط على القائمة المنسدلة **ckpt_name**
4. اختر النموذج الجديد (مثل `deliberate_v2.safetensors`)
5. اضغط **Queue Prompt** لبدء التوليد

### **في workflow.json:**

عدّل السطر التالي:
```json
"1": {
  "inputs": {
    "ckpt_name": "deliberate_v2.safetensors"  // ← غيّر الاسم هنا
  },
  "class_type": "CheckpointLoaderSimple"
}
```

---

## 🎨 **Prompts فعّالة للمحتوى الواقعي**

### **Positive Prompt (مثال):**
```
masterpiece, best quality, ultra high res, photorealistic, 
8k uhd, raw photo, professional photography, natural lighting,
detailed skin texture, detailed face, realistic proportions,
beautiful woman, [your specific description here]
```

### **Negative Prompt (مهم للجودة):**
```
low quality, worst quality, low res, blurry, watermark, 
username, signature, text, error, artifacts, jpeg artifacts,
ugly, duplicate, mutilated, mutation, deformed, distorted,
bad anatomy, bad proportions, extra limbs, extra fingers,
poorly drawn hands, poorly drawn face, missing limbs
```

---

## 🌐 **أفضل المواقع للنماذج**

### **Civitai.com** ⭐ (الأشهر والأفضل)
- **المميزات:**
  - ✅ أكبر مكتبة نماذج NSFW
  - ✅ نظام تقييم ومراجعات
  - ✅ أمثلة صور لكل نموذج
  - ✅ فلترة حسب النوع (Realistic/Anime/etc)
  - ✅ تحميل مباشر
- **الرابط:** https://civitai.com
- **كيف تبحث:**
  - اضبط الفلتر على "NSFW" أو "Adult"
  - صنّف حسب "Most Downloaded" أو "Highest Rated"
  - اقرأ التعليقات والمراجعات

### **Hugging Face**
- نماذج مفتوحة المصدر (بعضها غير مقيد)
- https://huggingface.co/models

---

## ⚙️ **إعدادات مهمة للجودة العالية**

### **للصور:**
```json
"width": 768,      // ← دقة أعلى (استخدم مضاعفات 64)
"height": 1024,
"steps": 30,       // ← خطوات أكثر = جودة أفضل
"cfg": 7.5,        // ← التزام أقوى بالـ prompt
"sampler_name": "dpmpp_2m_karras"  // ← sampler أفضل
```

### **للفيديو (AnimateDiff):**
```json
"batch_size": 24,   // ← إطارات أكثر = فيديو أطول
"frame_rate": 12,   // ← معدل إطارات أعلى = حركة سلسة
"steps": 25,
"cfg": 8.0
```

---

## 🚀 **نصائح احترافية**

### **1. استخدم LoRA للتحكم الدقيق**
- LoRA = ملفات صغيرة (~100MB) تُضاف للنموذج
- تسمح بأساليب/شخصيات محددة
- تحميل من Civitai → مجلد `models/loras/`

### **2. استخدم Negative Embeddings**
- مثل **EasyNegative** أو **BadDream**
- تحسّن الجودة تلقائياً
- تحميل → مجلد `models/embeddings/`

### **3. استخدم Upscalers للدقة العالية**
- **4x-UltraSharp** أو **ESRGAN**
- لتكبير الصور من 512×512 إلى 2048×2048
- تحميل → مجلد `models/upscale_models/`

---

## ⚠️ **اعتبارات مهمة**

### **القانونية:**
- ✅ محتوى توليد AI قانوني في معظم الدول (طالما لا يشبه أشخاص حقيقيين)
- ❌ تجنب توليد محتوى يشبه مشاهير/أشخاص حقيقيين بدون موافقتهم
- ❌ محظور: محتوى غير قانوني (أطفال، عنف، إلخ)

### **الأخلاقية:**
- استخدم بمسؤولية
- لا تنشر محتوى مسيء
- احترم خصوصية الآخرين

### **التقنية:**
- النماذج الكبيرة (SDXL) تحتاج GPU قوي
- Colab المجاني يعمل بشكل ممتاز مع SDXL
- احفظ عملك - Colab يحذف الملفات بعد 12 ساعة

---

## 📦 **نموذج كامل محسّن لـ Colab**

### **Cell 5 المحسّن (استبدل القديم):**

```python
%cd {PROJECT_DIR}/ComfyUI/models
print("⏳ تحميل النماذج المحسّنة...")

# نموذج SDXL واقعي (أفضل جودة)
!wget -q --show-progress -P checkpoints/ \
  "https://civitai.com/api/download/models/130072" \
  -O checkpoints/juggernaut_xl.safetensors

# AnimateDiff (للفيديو)
!wget -q --show-progress -P animatediff_models/ \
  https://huggingface.co/guoyww/animatediff/resolve/main/mm_sd_v15_v2.ckpt

# VAE محسّن
!wget -q --show-progress -P vae/ \
  https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.safetensors

# LoRA للجودة (اختياري)
!mkdir -p loras
!wget -q --show-progress -P loras/ \
  "https://civitai.com/api/download/models/[LORA_ID]" \
  -O loras/detail_tweaker.safetensors

print("✓ تم تحميل جميع النماذج المحسّنة!")
```

---

## 🎯 **الخلاصة**

### **نظامك الحالي:**
✅ **جاهز للاستخدام غير المقيد** - SD 1.5 بدون فلاتر

### **للجودة الأفضل:**
1. حمّل نموذج من Civitai (مثل **Juggernaut XL** أو **Deliberate**)
2. استخدم prompts مفصلة
3. ارفع عدد الخطوات (steps) إلى 30+
4. استخدم LoRAs إضافية

### **أسهل طريق:**
1. افتح Civitai.com
2. ابحث عن "realistic" + فلتر "NSFW"
3. حمّل النموذج الأعلى تقييماً
4. ضعه في `models/checkpoints/`
5. اختره من ComfyUI

---

## 🚀 **جاهز للبدء!**

**نظامك الحالي يعمل بدون قيود.** إذا أردت جودة أفضل، اتبع الخطوات أعلاه! 🎬

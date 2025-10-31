# 🎯 دليل الاستخدام الفوري - Google Colab

## 📥 الخطوة 1: حمّل الملفات (من هذا المجلد)

### الملفات المطلوبة:
```
✅ ComfyUI_AnimateDiff_Colab.ipynb          (الملف الرئيسي)
✅ animatediff_workflow_colab.json          (workflow جاهز)
✅ COLAB_QUICK_START.md                     (دليل سريع)
✅ README_Colab.md                          (للمراجعة)
```

---

## 🌐 الخطوة 2: افتح Google Colab

### الطريقة السريعة:
1. اذهب إلى: **https://colab.research.google.com/**
2. أو ابحث في Google عن: **"Google Colab"**

---

## 📤 الخطوة 3: ارفع الملف

### في صفحة Colab:
1. اضغط **File** (ملف)
2. اختر **Upload notebook** (رفع دفتر ملاحظات)
3. اختر ملف `ComfyUI_AnimateDiff_Colab.ipynb`
4. انتظر حتى يتم الرفع (ثوانٍ)

---

## ⚙️ الخطوة 4: فعّل GPU (مهم جداً!)

### ⚠️ لا تنسَ هذه الخطوة!

1. في Colab، اضغط **Runtime** (وقت التشغيل)
2. اختر **Change runtime type** (تغيير نوع وقت التشغيل)
3. في **Hardware accelerator**، اختر **GPU**
4. اضغط **Save** (حفظ)

### التحقق:
- يجب أن يظهر "GPU" في الزاوية اليمنى العليا
- إذا لم يظهر، أعد الخطوات أعلاه

---

## ▶️ الخطوة 5: شغّل الخلايا

### بالترتيب من الأعلى للأسفل:

#### ✅ خلية 1: التحقق من GPU
- اضغط ▶️ بجانب الخلية
- يجب أن يظهر: "✓ GPU متاح!"
- ⏱️ ~10 ثوانٍ

#### ✅ خلية 2: استنساخ ComfyUI
- اضغط ▶️
- يتم استنساخ المشروع
- ⏱️ ~30 ثانية

#### ✅ خلية 3: تثبيت المتطلبات
- اضغط ▶️
- تثبيت المكتبات
- ⏱️ ~2-3 دقائق
- ⚠️ قد ترى warnings - تجاهلها

#### ✅ خلايا 4-8: تنزيل النماذج
- اضغط ▶️ على كل خلية
- التنزيل: ~8 GB
- ⏱️ ~5-10 دقائق
- 📊 ستشاهد شريط التقدم
- ☕ وقت القهوة!

#### ✅ خلية 9: تثبيت Cloudflare
- اضغط ▶️
- ⏱️ ~30 ثانية

#### ✅ خلية 10: تشغيل الخادم
- اضغط ▶️
- ⏱️ ~1 دقيقة

**🔗 سيظهر رابط مثل:**
```
🌐 رابط الوصول للواجهة:
🔗 https://xxxxx-xx-xx.trycloudflare.com
```

**✅ انسخ الرابط! افتحه في تبويب جديد!**

---

## 🎬 الخطوة 6: إنشاء أول فيديو

### في واجهة ComfyUI التي فتحت:

#### الطريقة السهلة (Workflow جاهز):
1. ارجع لملفاتك، افتح `animatediff_workflow_colab.json`
2. انسخ محتواه (Ctrl+A ثم Ctrl+C)
3. في ComfyUI، اضغط **Load** (تحميل)
4. الصق المحتوى أو اسحب الملف
5. سيظهر الـ workflow كاملاً!

#### تعديل Prompts:
في الـ workflow، ابحث عن boxes النصوص:

**Positive Prompt:**
```
stunning cinematic landscape, mountains at sunrise, golden hour, 8k
```

**Negative Prompt:**
```
low quality, blurry, watermark, text
```

**جرّب تغييرها!**

#### توليد الفيديو:
1. اضغط **Queue Prompt** (أعلى اليمين)
2. انتظر 2-5 دقائق
3. سيظهر الفيديو!

---

## 📥 الخطوة 7: تحميل الفيديو

### العودة لـ Colab:
1. ارجع لتبويب Colab
2. شغّل الخلية الأخيرة "تحميل الفيديوهات"
3. سيتم التحميل تلقائياً!

---

## 🎨 أمثلة Prompts للتجربة:

### 🏔️ جبال:
```
Positive: "epic mountain landscape, golden hour, cinematic"
Negative: "low quality, blurry"
```

### 🌊 بحر:
```
Positive: "ocean waves, dramatic sunset, beautiful"
Negative: "calm, static"
```

### 🏙️ مدينة:
```
Positive: "cyberpunk city, neon lights, futuristic"
Negative: "daytime, old"
```

### 🔥 أكشن:
```
Positive: "epic explosion, dramatic, cinematic 4k"
Negative: "peaceful, calm"
```

---

## ⚙️ إعدادات موصى بها:

### للمبتدئين (سريع):
- Resolution: 512x512
- Frames: 8
- Steps: 15

### للجودة العادية:
- Resolution: 512x512
- Frames: 16
- Steps: 20

### للجودة العالية:
- Resolution: 512x512
- Frames: 16
- Steps: 25-30

---

## 🔧 حل المشاكل:

### ❌ "No GPU detected"
**الحل:**
1. Runtime → Change runtime type
2. GPU → Save
3. Runtime → Restart runtime
4. شغّل الخلايا من جديد

### ❌ "Out of memory"
**الحل:**
- قلل Frames من 16 إلى 8
- قلل Resolution من 512 إلى 384

### ❌ الرابط لا يعمل
**الحل:**
- انتظر دقيقة إضافية
- ابحث عن رابط جديد في الخلية
- تأكد أن خلية التشغيل ما زالت تعمل

### ❌ Session crashed
**الحل:**
- Runtime → Restart runtime
- شغّل جميع الخلايا من جديد
- (عادي في Colab المجاني)

---

## 💡 نصائح ذهبية:

1. ✅ **لا تغلق Colab** - الجلسة ستنتهي
2. ✅ **حمّل الفيديوهات فوراً** - مؤقتة
3. ✅ **جرّب seeds مختلفة** - نتائج مختلفة
4. ✅ **ابدأ بإعدادات بسيطة** - ثم زد
5. ✅ **احفظ workflows الناجحة** - أعد استخدامها
6. ✅ **Colab مجاني لـ 12 ساعة** - خطط
7. ✅ **كل جلسة = إعداد جديد** - عادي

---

## ⏱️ الوقت المتوقع:

| المرحلة | الوقت |
|---------|-------|
| رفع الملف | 1 دقيقة |
| تفعيل GPU | 30 ثانية |
| الإعداد (خلايا 1-9) | 10 دقائق |
| توليد فيديو | 2-5 دقائق |
| **المجموع** | **~15 دقيقة** |

---

## 📱 من الموبايل؟

يعمل على الموبايل! 📱
- افتح Chrome أو Safari
- اذهب لـ colab.research.google.com
- نفس الخطوات!

---

## ✅ Checklist:

- [ ] حمّلت الملفات من المشروع
- [ ] فتحت Google Colab
- [ ] رفعت ComfyUI_AnimateDiff_Colab.ipynb
- [ ] فعّلت GPU
- [ ] شغّلت جميع الخلايا بالترتيب
- [ ] حصلت على الرابط
- [ ] فتحت واجهة ComfyUI
- [ ] أنشأت أول فيديو!
- [ ] حمّلت الفيديو

---

## 🎉 أنت جاهز!

**اتبع الخطوات أعلاه واحدة تلو الأخرى.**

**بالتوفيق في إنشاء فيديوهات AI رائعة! 🎬✨**

---

## 🆘 محتاج مساعدة؟

اقرأ:
- `COLAB_QUICK_START.md` - دليل سريع
- `README_Colab.md` - دليل شامل

---

**🚀 ابدأ الآن! كل شيء جاهز!**

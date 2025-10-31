# دليل الوصول لـ ComfyUI من iPad

## 📱 الوضع الحالي

النظام مُثبت على **خادم بعيد** (remote server) وليس على iPad نفسه.  
iPad لا يمكنه تشغيل Python/ComfyUI محلياً بسهولة.

**الحل**: الوصول للخادم البعيد من iPad!

---

## 🎯 الطريقة الموصى بها: SSH + ngrok

### الخطوة 1: تطبيق SSH على iPad

حمّل أحد هذه التطبيقات:

#### 🥇 Termius (موصى به - مجاني)
- **الرابط**: https://apps.apple.com/app/termius/id549039908
- **المميزات**: سهل، مجاني، واجهة ممتازة
- **السلبيات**: بعض الميزات المتقدمة مدفوعة

#### 🥈 Blink Shell (احترافي)
- **الرابط**: https://apps.apple.com/app/blink-shell/id1156707581
- **المميزات**: محترف جداً، سريع
- **السلبيات**: مدفوع ($20)

#### 🥉 iSH Shell (بديل محلي)
- **الرابط**: https://apps.apple.com/app/ish-shell/id1436902243
- **المميزات**: محاكي Linux على iPad
- **السلبيات**: أبطأ من SSH الحقيقي

---

### الخطوة 2: الاتصال بالخادم

1. افتح التطبيق (مثلاً Termius)
2. أضف host جديد:
   - **Host**: عنوان IP للخادم
   - **Username**: ubuntu (أو اسم المستخدم الخاص بك)
   - **Port**: 22 (افتراضي)
   - **Authentication**: Password أو SSH Key

3. اتصل بالخادم
4. ستظهر لك terminal على الخادم!

---

### الخطوة 3: تشغيل ComfyUI

في terminal على iPad، نفّذ:

```bash
~/comfyui-animatediff-pro/START.sh
```

أو:

```bash
cd ~/comfyui-animatediff-pro
source venv/bin/activate
cd ComfyUI
python main.py
```

---

## 🌐 الوصول لواجهة ComfyUI من iPad

### السيناريو 1: نفس الشبكة المحلية

إذا كان الخادم والiPad على نفس WiFi:

1. احصل على IP الخادم المحلي:
   ```bash
   hostname -I
   ```
   مثال: `192.168.1.100`

2. شغّل ComfyUI على الخادم

3. على iPad، افتح Safari:
   ```
   http://192.168.1.100:8188
   ```

---

### السيناريو 2: خادم بعيد (VPS/Cloud)

استخدم **ngrok** لعمل tunnel آمن:

#### تثبيت ngrok على الخادم:

```bash
# 1. تحميل ngrok
wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz
tar xvzf ngrok-v3-stable-linux-amd64.tgz
sudo mv ngrok /usr/local/bin/

# 2. التسجيل والحصول على token
# سجل في: https://dashboard.ngrok.com/signup
# احصل على auth token

# 3. إضافة token
ngrok config add-authtoken YOUR_AUTH_TOKEN_HERE
```

#### تشغيل ComfyUI مع ngrok:

```bash
# Terminal 1: شغّل ComfyUI
cd ~/comfyui-animatediff-pro
source venv/bin/activate
cd ComfyUI
python main.py

# Terminal 2: شغّل ngrok (في terminal آخر)
ngrok http 8188
```

ستحصل على رابط مثل:
```
https://xxxx-xxxx-xxxx.ngrok-free.app
```

افتح هذا الرابط من Safari على iPad! 🎉

---

## 🚀 سكريبت تشغيل تلقائي مع ngrok

يمكنك إنشاء سكريبت لتشغيل كل شيء مرة واحدة:

```bash
#!/bin/bash
# ملف: start_with_ngrok.sh

cd ~/comfyui-animatediff-pro
source venv/bin/activate
cd ComfyUI

# شغّل ComfyUI في الخلفية
nohup python main.py > ~/comfyui.log 2>&1 &

# انتظر قليلاً
sleep 5

# شغّل ngrok
echo "🚀 تشغيل ngrok..."
ngrok http 8188
```

احفظه وشغّله:
```bash
chmod +x ~/comfyui-animatediff-pro/start_with_ngrok.sh
~/comfyui-animatediff-pro/start_with_ngrok.sh
```

---

## 🛡️ الأمان

### ngrok مجاني له حدود:
- ✅ آمن ومشفر
- ⚠️ الرابط يتغير كل مرة (في النسخة المجانية)
- ⚠️ حد استخدام شهري

### لتأمين أكثر:
1. استخدم Basic Auth في ComfyUI
2. أو استخدم Cloudflare Tunnel (بديل لـ ngrok)

---

## 🔄 بدائل ngrok

### Cloudflare Tunnel (مجاني دائماً):

```bash
# تثبيت cloudflared
wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
sudo dpkg -i cloudflared-linux-amd64.deb

# تسجيل دخول
cloudflared tunnel login

# إنشاء tunnel
cloudflared tunnel create comfyui

# تشغيل
cloudflared tunnel --url http://localhost:8188 run comfyui
```

---

## 📱 نصائح للاستخدام على iPad

### 1. استخدم Safari (أفضل من Chrome على iPad)
- دعم أفضل للمس
- أداء أحسن

### 2. وضع ملء الشاشة
- اضغط على أيقونة المشاركة
- اختر "Add to Home Screen"
- سيعمل كتطبيق مستقل!

### 3. Apple Pencil
- يعمل بشكل ممتاز مع واجهة ComfyUI
- سحب وإفلات Nodes سهل جداً

### 4. Split View
- شغّل Safari مع Termius جنباً إلى جنب
- راقب السجلات أثناء العمل

---

## ⚠️ مشاكل شائعة وحلولها

### المشكلة: لا يمكنني الاتصال بالخادم
**الحل**: 
- تحقق من أن الخادم يعمل
- تحقق من بيانات الاتصال (IP, username, password)
- تحقق من Firewall

### المشكلة: ngrok لا يعمل
**الحل**:
- تأكد من التسجيل والحصول على auth token
- نفّذ: `ngrok config add-authtoken YOUR_TOKEN`
- تحقق من أن port 8188 مفتوح

### المشكلة: الواجهة بطيئة
**الحل**:
- استخدم WiFi قوي
- أغلق تطبيقات أخرى على iPad
- قلل جودة المعاينة في ComfyUI

---

## 🎬 الخلاصة

### للوصول المحلي (نفس الشبكة):
```bash
# على الخادم
~/comfyui-animatediff-pro/START.sh

# على iPad Safari
http://192.168.1.X:8188
```

### للوصول من أي مكان:
```bash
# على الخادم
# Terminal 1
~/comfyui-animatediff-pro/START.sh

# Terminal 2  
ngrok http 8188

# انسخ الرابط وافتحه على iPad
```

---

## 📚 موارد إضافية

- **ngrok docs**: https://ngrok.com/docs
- **Termius guide**: https://termius.com/education
- **ComfyUI mobile tips**: https://comfyanonymous.github.io/ComfyUI_examples/

---

**🎉 الآن يمكنك استخدام ComfyUI من iPad بسهولة! 🚀**

---

**تاريخ التحديث**: 2025-10-31  
**الإصدار**: 1.0

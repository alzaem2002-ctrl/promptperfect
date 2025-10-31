# 🔌 توزيع المنافذ - منع التعارضات

## المنافذ المستخدمة

| النظام | المنفذ | الاستخدام | العنوان |
|--------|-------|----------|---------|
| **ComfyUI** | 8188 | الواجهة الرئيسية | http://localhost:8188 |
| **AUTOMATIC1111** | 7860 | الواجهة الرئيسية | http://localhost:7860 |
| **InvokeAI** | 9090 | الواجهة الرئيسية | http://localhost:9090 |
| **iPad Controller** | 8080 | تطبيق التحكم | http://localhost:8080 |

## ✅ لا توجد تعارضات

كل نظام يعمل على منفذ مختلف، يمكن تشغيلهم جميعاً معاً!

## 🚀 كيفية البدء

### تشغيل ComfyUI
```bash
bash automation/start-comfyui.sh
# http://localhost:8188
```

### تشغيل AUTOMATIC1111
```bash
bash automation/start-automatic1111.sh
# http://localhost:7860
```

### تشغيل InvokeAI
```bash
bash automation/start-invokeai.sh
# http://localhost:9090
```

### تشغيل iPad Controller
```bash
bash automation/start-ipad-controller.sh
# http://localhost:8080
```

## 💡 نصيحة

يمكنك تشغيل كل نظام في terminal منفصل، وسيعملون جميعاً معاً بدون تعارضات!

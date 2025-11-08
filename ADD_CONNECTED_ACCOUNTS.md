# كيفية إضافة حسابات متصلة إلى التقرير

## 📋 نظرة عامة

قسم "Connected/Related Accounts" (الحسابات المتصلة/المرتبطة) مخصص للحسابات التي تم اكتشافها من خلال:
- المتابعين المشتركين
- البحث عن أسماء مستخدمين مشابهة
- البحث العكسي عن رقم الهاتف
- ربط عناوين البريد الإلكتروني
- مطابقة أسماء المستخدمين عبر المنصات

## 🔧 الطرق المتاحة

### الطريقة 1: استخدام السكريبت المساعد

```python
python3 add_to_report.py
```

ثم عدّل السكريبت لإضافة حساباتك:

```python
add_connected_account(
    report,
    platform="Twitter",
    username="example_user",
    url="https://twitter.com/example_user",
    connection_type="Mutual Follower",
    profile_info={
        "display_name": "Example User",
        "followers": "1,234",
        "following": "567"
    },
    notes="تم العثور عليه من خلال تحليل المتابعين المشتركين على Instagram"
)
```

### الطريقة 2: تعديل ملف JSON مباشرة

افتح ملف `osint_report_20251106_190115.json` وأضف إلى قسم `connected_accounts`:

```json
{
  "platform": "Twitter",
  "username": "example_user",
  "url": "https://twitter.com/example_user",
  "connection_type": "Mutual Follower",
  "status": "found",
  "profile_info": {
    "display_name": "Example User",
    "followers": "1,234"
  },
  "notes": "تم العثور عليه من خلال تحليل المتابعين المشتركين"
}
```

## 📝 أنواع الاتصال (Connection Types)

- **Mutual Follower** - متابع مشترك
- **Mutual Following** - متبوع مشترك
- **Similar Username** - اسم مستخدم مشابه
- **Phone Lookup** - من خلال البحث عن رقم الهاتف
- **Email Association** - من خلال ربط البريد الإلكتروني
- **Cross-Platform Match** - مطابقة عبر المنصات
- **Tagged Together** - تم الإشارة إليهما معاً
- **Location Match** - نفس الموقع الجغرافي

## 🔍 مصادر للبحث عن حسابات متصلة

1. **Instagram:**
   - تحليل قائمة المتابعين
   - تحليل قائمة المتابَعين
   - البحث عن أسماء مشابهة
   - المنشورات المشتركة

2. **TikTok:**
   - المتابعين المشتركين
   - الفيديوهات المشتركة
   - التعليقات والتفاعلات

3. **Phone Number Lookup:**
   - TrueCaller
   - WhitePages
   - PhoneInfoga

4. **Username Search:**
   - Sherlock
   - Maigret
   - Namechk

## ✅ بعد إضافة الحسابات

بعد إضافة الحسابات إلى ملف JSON، قم بتشغيل:

```bash
python3 osint_tool.py
```

سيتم إنشاء تقرير HTML محدث يتضمن جميع الحسابات المتصلة.

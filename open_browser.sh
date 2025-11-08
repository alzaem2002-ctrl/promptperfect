#!/bin/bash
# سكريبت لفتح OSINT Tools في المتصفح

echo "🚀 جاري فتح OSINT Tools..."

# محاولة فتح في المتصفحات المختلفة
if command -v xdg-open &> /dev/null; then
    xdg-open "http://localhost:8000/" 2>/dev/null &
    echo "✅ تم فتح المتصفح!"
elif command -v open &> /dev/null; then
    open "http://localhost:8000/" 2>/dev/null &
    echo "✅ تم فتح المتصفح!"
elif command -v firefox &> /dev/null; then
    firefox "http://localhost:8000/" 2>/dev/null &
    echo "✅ تم فتح Firefox!"
elif command -v chromium-browser &> /dev/null; then
    chromium-browser "http://localhost:8000/" 2>/dev/null &
    echo "✅ تم فتح Chromium!"
elif command -v google-chrome &> /dev/null; then
    google-chrome "http://localhost:8000/" 2>/dev/null &
    echo "✅ تم فتح Chrome!"
else
    echo "⚠️  لم يتم العثور على متصفح"
    echo "📍 افتح هذا الرابط يدوياً:"
    echo "   http://localhost:8000/"
fi

echo ""
echo "📋 الروابط المتاحة:"
echo "   الرئيسية: http://localhost:8000/"
echo "   Social Mapper: http://localhost:8000/social_mapper_arabic.html"
echo "   تقرير OSINT: http://localhost:8000/osint_professional_report_2025-11-07.html"

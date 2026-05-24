# 🔥 Shadow Prompt Bot

بوت تيليجرام متقدم لإدارة وتحضير برومبتات متخصصة للذكاء الاصطناعي.

## ✨ المميزات

- 🚀 4 أنواع من البرومبتات: هاك، كود، كسر، إبداعي
- 🌐 دعم 3 لغات: العربية، الإنجليزية، الفرنسية
- 💾 حفظ سجل البرومبتات في قاعدة بيانات
- 📜 عرض آخر البرومبتات المستخدمة
- 📊 إحصائيات البوت
- 📁 تصدير البرومبتات

## 🚀 النشر على Render

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

### خطوات النشر:

1. انقر على الزر أعلاه
2. اختر مستودع GitHub الخاص بك
3. أضف المتغير البيئي `TELEGRAM_BOT_TOKEN`
4. انقر "Apply"

## 📝 المتغيرات البيئية

| المتغير | الوصف |
|---------|-------|
| `TELEGRAM_BOT_TOKEN` | توكن بوت تيليجرام (مطلوب) |
| `PORT` | منفذ التشغيل (يحدد تلقائياً) |

## 🛠️ التطوير المحلي

```bash
# استنساخ المشروع
git clone https://github.com/YOUR_USERNAME/shadow-prompt-bot.git
cd shadow-prompt-bot

# تثبيت المتطلبات
pip install -r requirements.txt

# تشغيل البوت
export TELEGRAM_BOT_TOKEN="your_token"
python app.py

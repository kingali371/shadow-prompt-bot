FROM python:3.11-slim

WORKDIR /app

# تثبيت المتطلبات
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# نسخ الكود
COPY bot.py .
COPY utils/ ./utils/

# إنشاء مجلد للقاعدة البيانات
RUN mkdir -p /app/data

# متغيرات البيئة
ENV PYTHONUNBUFFERED=1

# تشغيل البوت
CMD ["python", "bot.py"]

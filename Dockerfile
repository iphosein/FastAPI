# Dockerfile — نسخه ۱۰۰٪ کار شده روی Render.com
FROM python:3.11-slim

# نصب build dependencies برای psycopg2 و بقیه
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# اول requirements نصب کن (بدون --user)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# بقیه فایل‌ها رو کپی کن
COPY . .

# یوزر غیرروت برای امنیت
RUN useradd -m appuser
USER appuser

EXPOSE 8000

# migration خودکار + اجرا
CMD ["sh", "-c", "alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000"]

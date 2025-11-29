# Dockerfile — نسخه ۱۰۰٪ کارکردی روی Render.com (نوامبر ۲۰۲۵)
FROM python:3.11-slim

WORKDIR /app

# کپی requirements و نصب (بدون build deps — psycopg2-binary نیاز نداره)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# یوزر غیرروت (امنیت)
RUN adduser --disabled-password --gecos '' appuser
USER appuser

EXPOSE 8000

# migration خودکار + سرور (پورت Render)
CMD ["sh", "-c", "alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]

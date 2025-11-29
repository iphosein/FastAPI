# Dockerfile — کپی کن در ریشه
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

FROM python:3.11-slim
WORKDIR /app

# کپی پکیج‌ها از مرحله قبل
COPY --from=builder /root/.local /root/.local
COPY . .

# غیر روت یوزر (امنیت بالا)
RUN useradd -m appuser
USER appuser

ENV PATH=/root/.local/bin:$PATH
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

# migration خودکار + اجرا
CMD ["sh", "-c", "alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000"]

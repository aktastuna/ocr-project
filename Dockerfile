# syntax=docker/dockerfile:1
FROM python:3.10-slim

# OpenCV + Paddle bağımlılıkları (CPU)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0 \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Önce requirements (cache için)
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Sonra projedeki her şeyi kopyala
COPY . /app

EXPOSE 8000
CMD ["uvicorn", "paddle_engine:app", "--host", "0.0.0.0", "--port", "8000"]
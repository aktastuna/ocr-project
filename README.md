## PaddleOCR FastAPI - Docker

### 1) Build
```bash
docker build -t paddle-ocr-api .
```

### 2) Run
```bash
docker run --rm -p 8000:8000 paddle-ocr-api
```

### 3) Test
```bash
curl -X GET http://localhost:8000/welcome
```

```bash
curl -X POST http://localhost:8000/paddleocr \
  -H "Content-Type: application/json" \
  -d '{"image_base64":"<BASE64_STRING>"}'
```

### Notes
- `image_base64` should be raw base64 (no `data:image/...;base64,` prefix). If you have that prefix, strip it on client side.
- PaddleOCR will download its model files the first time the container starts. To cache these, uncomment the `volumes:` section in `docker-compose.yml`.
- If you plan to use GPU later, you’ll need a different base image + paddlepaddle-gpu, and NVIDIA Container Toolkit.

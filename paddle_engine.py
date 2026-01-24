from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

from pydantic import BaseModel

import logging
logging.basicConfig(format='%(levelname)s %(asctime)s %(module)s.%(funcName)s: %(message)s', level=logging.INFO)

from core.paddle_core.paddle_handler import PaddleHandler
from core.pre_processing.image_pre_process import Base64ToCv2

paddleocr_handler = PaddleHandler()
paddle_ocr = paddleocr_handler.initialize_paddle()
base2cv2 = Base64ToCv2()

logging.info("PaddleOCR engine initialized in Paddle Engine.")
app = FastAPI()

class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        response.headers['X-Frame-Options'] = 'DENY'
        response.headers['Content-Security-Policy'] = "ddefault-src 'self'"
        response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
        response.headers['Cache-Control'] = 'no-store'
        return response
    
app.add_middleware(SecurityHeadersMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PaddleRequest(BaseModel):
    image_base64: str

@app.get("/welcome")
async def welcome():
    return {"message": "Welcome to the PaddleOCR Engine!"}

@app.post("/paddleocr")
async def perform_ocr(request: PaddleRequest):
    try:
        logging.info("Received OCR request.")
        image_data = request.image_base64
        image_data = base2cv2.convert(image_data)
        logging.info(1)
        result = paddleocr_handler.recognize_text(paddle_ocr, image_data)
        logging.info(result)
        logging.info("OCR request processed successfully.")
        return {"result": result}
    except Exception as e:
        logging.error(f"OCR processing failed: {e}")
        raise HTTPException(status_code=500, detail="OCR processing failed.")
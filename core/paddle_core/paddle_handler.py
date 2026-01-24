from paddleocr import PaddleOCR

import logging
logging.basicConfig(format='%(levelname)s %(asctime)s %(module)s.%(funcName)s: %(message)s', level=logging.INFO)

class PaddleHandler:
    """Handler for PaddleOCR operations."""
    def initialize_paddle(self):
        try:
            logging.info("Initializing PaddleOCR...")
            ocr_engine = PaddleOCR(use_angle_cls=True, lang='en')
            logging.info("PaddleOCR initialized successfully.")
        except Exception as e:
            logging.error(f"Error initializing PaddleOCR: {e}")
            ocr_engine = None
            raise e
        return ocr_engine
        

    def recognize_text(self, model, image) -> list:
        """Recognize text from an image using the provided PaddleOCR model.
        Args:
            model: The PaddleOCR model instance.
            image: The image to process.
        Returns:
            A list of recognized text elements.
        """
        try:
            logging.info("Starting text recognition...")
            result = model.ocr(image)[0]["rec_texts"]
            logging.info("Text recognition completed successfully.")
        except Exception as e:
            logging.error(f"Error during text recognition: {e}")
            result = []
            raise e
        return result
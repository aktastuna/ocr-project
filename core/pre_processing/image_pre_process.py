import base64
import numpy as np
import cv2
import logging
logging.basicConfig(format='%(levelname)s %(asctime)s %(module)s.%(funcName)s: %(message)s', level=logging.INFO)

class Base64ToCv2:
    """Utility class to convert base64 encoded strings to cv2 images."""
    @staticmethod
    def convert(base64_str: str) -> np.ndarray:
        """Convert a base64 string to a cv2 image (numpy array).
        Args:
            base64_str (str): The base64 encoded string of the image.
        Returns:
            np.ndarray: The decoded image as a cv2 image (numpy array).
        """
        try:
            logging.info("Converting base64 string to cv2 image...")
            # Decode the base64 string
            img_data = base64.b64decode(base64_str)
            # Convert bytes data to numpy array
            nparr = np.frombuffer(img_data, np.uint8)
            # Decode image from numpy array
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            logging.info("Conversion to cv2 image successful.")
            return img
        except Exception as e:
            logging.error(f"Error converting base64 to cv2 image: {e}")
            raise ValueError(f"Failed to convert base64 string to cv2 image: {e}")
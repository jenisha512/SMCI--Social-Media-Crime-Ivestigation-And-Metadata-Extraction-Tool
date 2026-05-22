import pytesseract
from PIL import Image
import os

# POINT TO WHERE YOU INSTALLED TESSERACT (CRITICAL STEP)
# If you installed it in the default location, this path is correct.
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    """
    Reads text from an image (OCR).
    Returns the text found or None if empty.
    """
    try:
        img = Image.open(image_path)
        # Convert text to string
        extracted_text = pytesseract.image_to_string(img)
        
        if not extracted_text.strip():
            return None
            
        return extracted_text
    except Exception as e:
        return f"Error during OCR: {str(e)}"
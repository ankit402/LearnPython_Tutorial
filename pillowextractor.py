import pytesseract
from PIL import Image

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load and process image
img = Image.open("sample_image.jpg")
text = pytesseract.image_to_string(img)

print("Extracted Text:\n", text)

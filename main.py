import pytesseract
import shutil
import os
import random
try:
 from PIL import Image
except ImportError:
 import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image_path_in_colab = 'Test.jpg'
extractedInformation = pytesseract.image_to_string(Image.open(image_path_in_colab))
print(extractedInformation)
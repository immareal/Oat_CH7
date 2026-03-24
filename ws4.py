import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\STATSCSU\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

img = Image.open("3099c5bc380678ffd037b44b3d815dae.jpg")

text = pytesseract.image_to_string(img, lang="eng")
print(repr(text))
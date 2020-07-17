import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r'C:/Program Files/Tesseract-OCR/tesseract.exe'

a=input('Enter img name :') #sample.jpg for testing purposes
img=cv2.imread(a)
text=pytesseract.image_to_string(img)
print(text)

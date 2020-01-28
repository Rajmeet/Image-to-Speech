# **** IMPORTING **** #
import cv2
import os
from gtts import gTTS
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = (r"C:\Program Files\Tesseract-OCR\tesseract.exe")


# **** CONVERSION **** #
def ImageConversionToText(file):
    img = cv2.imread(file)
    text = pytesseract.image_to_string(img)
    print(text)
    gtts = gTTS(text)
    gtts.save('audio.mp3')
    os.system('audio.mp3')


# **** MAIN **** #
file = input("Image name: (Needs to be in the same directory): ")+'.png'
ImageConversionToText(file)




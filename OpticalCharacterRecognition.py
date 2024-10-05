# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pytesseract
import cv2

path = "C:\\Users\\ahmet\\BasicAIProject\\restoran2.jpg"

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

resim = cv2.imread(path)

metin = pytesseract.image_to_string(resim)

cv2.imshow("resim",resim)
cv2.waitKey(0)
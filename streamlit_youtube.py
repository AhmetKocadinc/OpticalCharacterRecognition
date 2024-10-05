# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 12:37:08 2024

@author: ahmet
"""

import streamlit as st
import pytesseract
import cv2
from PIL import Image
import pandas as pd
import numpy as np

# Tesseract'ın komut yolunu ayarla
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# Başlık
st.title("Resimden Karakter Okuma Uygulaması")

# Resim yükleme
uploaded_file = st.file_uploader("Lütfen bir resim yükleyin", type=["jpg", "png", "jpeg"])

# Resim yüklendiğinde
if uploaded_file is not None:    # Yüklenen resmi görüntü olarak aç
    image = Image.open(uploaded_file)

    # OpenCV formatına çevir
    open_cv_image = np.array(image)
    open_cv_image = cv2.cvtColor(open_cv_image, cv2.COLOR_RGB2BGR)
    
    # Resmi ekranda göster
    st.image(image, caption='Yüklenen Resim', use_column_width=True)
    
    # Pytesseract ile resimden metin okuma
    metin = pytesseract.image_to_string(open_cv_image)
    
     # Metni DataFrame'e yazdırma
    df = pd.DataFrame({"Okunan Metin": [metin]})
    
     # DataFrame'i ekranda göster
    st.write("Resimden Okunan Metin:")
    st.dataframe(df)

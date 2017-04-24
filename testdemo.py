import numpy as np
import cv2
from PIL import Image
import pytesseract



(thresh, bw_img) = cv2.threshold(bw_img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)


img = Image.fromarray(bw_img)
txt = pytesseract.image_to_string(img)
print(txt)

import numpy as np
from numpy.linalg import norm
import cv2
from skimage.filters import threshold_local
import argparse
import imutils
from imutils import contours
import sys
import pytesseract
from PIL import Image

print(f'Image: {Image.__version__}')

def ocr(filename):
    return pytesseract.image_to_string(image = Image.open(filename))

filename = r'paragon_1.jpg'
img = cv2.imread(filename)

print(ocr(filename))

cv2.imshow('img', img)

#ocr()
cv2.waitKey(0)
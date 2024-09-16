# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 11:06:23 2024

@author: jarog
"""

from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import imutils
import argparse
import pickle
import cv2
import os

#run on CPU
# os.environ['CUDA VISIBLE_DEVICES'] = '-1'
#suppress logs
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

#przykladowe uruchomienie
#python 03_classify.py -i downloads\black_dress\0000.jpg -m output\model11_09_2024_14_45.keras


def load(filename):
    image = cv2.imread(filename)
    image = cv2.resize(image, (150,150))
    image = image.astype('float') / 255.
    image = img_to_array(image)
    image = np.expand_dims(image, axis = 0)
    return image
    
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help = 'path to the data')
ap.add_argument('-m', '--model', required=True, help = 'number of epochs')
args = vars(ap.parse_args())

print('[INFO] Loading model...')
model = load_model(args['model'])
#zbędne?:
image = load(args['image'])

y_pred = model.predict(image)[0]

print('[INFO] Loading labels...')
with open(r'output/mlb.pickle', 'rb') as file:
    mlb = pickle.loads(file.read())
    
labels = dict(enumerate(mlb.classes_))
idxs = np.argsort(y_pred)[::-1]

print('[INFO] Loading image...')
image = cv2.imread(args['image'])
image = imutils.resize(image, width=1000)

print('[INFO] Displaying image...')
for i,idx in enumerate(idxs[:2]):
    cv2.putText(img=image, text = f'Labels: {labels[idx]:6} Probability: {y_pred[idx] * 100:.4f}%',
                org=(10, (i*30) + 25), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale = 0.8,
                color=(0,179,137), thickness =2)

cv2.imshow('image', image)
cv2.waitKey(0)








import cv2
import numpy as np
import imutils

img = cv2.imread(r'assets\bear.jpg')
logo = cv2.imread(r'assets\python.png')

rows_img, cols_img, channels_img = img.shape
print(rows_img, cols_img, channels_img)
rows_logo, cols_logo, channels_logo = logo.shape
print(rows_logo, cols_logo, channels_logo)


logo = imutils.resize(logo, height=150)

cv2.imshow('img', img)
cv2.imshow('logo', logo)
# cv2.waitKey(0)

# #wyciecie obszaru roi region of interest
rows, cols, channels = logo.shape
roi = img[:rows, :cols]
print(rows, cols)
cv2.imshow('roi', roi)
# cv2.waitKey(0)


#zmiana na szary
gray = cv2.cvtColor(src = logo, code = cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)
# cv2.waitKey(0)

#wyciącie tylko szarości powyżej progu, [1] wycina jedną warotość (funkcja zwraca dwie)
mask = cv2.threshold(src = gray, thresh = 220, maxval = 255, type = cv2.THRESH_BINARY)[1]
cv2.imshow('mask', mask)
# cv2.waitKey(0)

#zmiana tła na czarne
mask_inv = cv2.bitwise_not(mask)
cv2.imshow('mask_inv', mask_inv)
# cv2.waitKey(0)

#wycinamy tło
img_bg = cv2.bitwise_and(src1 = roi, src2 = roi, mask = mask)
logo_fg = cv2.bitwise_and(src1 = logo, src2 = logo, mask = mask_inv)
cv2.imshow('img_bg', img_bg)
cv2.imshow('logo_fg', logo_fg)
# cv2.waitKey(0)

dst = cv2.add(src1 = img_bg, src2 = logo_fg)
cv2.imshow('dst', dst)
img[:rows, :cols] = dst
cv2.imshow('out', img)
cv2.waitKey(0)


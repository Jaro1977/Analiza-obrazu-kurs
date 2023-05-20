import cv2
import numpy as np

img = cv2.imread(r'C:\Users\user\PycharmProjects\Analiza-obrazu-kurs-test\01basic\assets\checkbox.png')

img =cv2.copyMakeBorder(
    src = img,
    top = 20,
    bottom = 20,
    left=20,
    right=20,
    borderType = cv2.BORDER_CONSTANT,
    value = (255,255,255)
)
# cv2.imshow('img', img)
gray = cv2.cvtColor(src = img, code = cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray', gray)
#rozmycie zdjęcia przy detekcji krawędzi mniej szczegółowo
blurred = cv2.GaussianBlur(src = gray, ksize = (5,5), sigmaX = 0)
# cv2.imshow('blurred', blurred)
#robimy maskę zdjęcia
thresh = cv2.threshold(src = blurred, thresh = 75, maxval=255, type = cv2.THRESH_BINARY)[1]
# cv2.imshow('thresh', thresh)
contours = cv2.findContours(image = thresh, mode = cv2.RETR_LIST, method = cv2.CHAIN_APPROX_SIMPLE)[0]
print(f'[INFO] Liczba wszystkich konturów: {len(contours)}')

img_cnt = cv2.drawContours(image = img.copy(),
                           contours = contours[4],
                           contourIdx = -1,
                           color = (0,255,0),
                           thickness = 5)
cv2.imshow('img_cnt', img_cnt)




cv2.waitKey(0)


contours = cv2.findContours(image = thresh, mode = cv2.RETR_LIST, method = cv2.CHAIN_APPROX_SIMPLE)[0]


cv2.waitKey(0)
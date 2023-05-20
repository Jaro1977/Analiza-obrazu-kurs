import cv2
import numpy as np

original_img = cv2.imread(filename = r'C:\Users\user\PycharmProjects\Analiza-obrazu-kurs-test\assets\python.png')

#img = original_img.copy()
#cv2.imshow(winname = 'original_img', mat = original_img)
#cv2.waitKey(delay = 0)

#height, width = img.shape[:2]
#print(f'wysokość: {height}')
#print(f'szerokość: {width}')

#cv2.line(img = img, pt1 = (0,0), pt2 = (width, height), color = (0,255,0), thickness = 5)
#cv2.imshow(winname = 'img', mat = img)
#cv2.waitKey(delay = 0)

#img = original_img.copy()
#cv2.rectangle(img = img, pt1 = (200,50), pt2 = (400,230), color = (255,0,0), thickness = 3)
#cv2.imshow(winname = 'img', mat = img)
#cv2.waitKey(delay = 0)


# img = original_img.copy()
# cv2.circle(img = img, center = (300,140), radius = 90, color = (255,255,0), thickness = 3)
# cv2.imshow(winname = 'img', mat = img)
# cv2.waitKey(delay = 0)


# img = original_img.copy()
# pts = np.array([[50,100],[100,200],[100,250],[50,300]], dtype = int).reshape((-1,1,2))
# print(pts)
# cv2.polylines(img = img, pts = [pts], isClosed = True, color = (0,255,0), thickness = 3)
# cv2.imshow('img', img)
# cv2.waitKey(delay = 0)

img = original_img.copy()
cv2.putText(img = img,
            text = 'python',
            org=(50,100),
            fontFace = cv2.FONT_HERSHEY_SIMPLEX,
            fontScale = 1.5,
            color = (0,255,0),
            thickness = 2)
cv2.imshow('img', img)
cv2.waitKey(delay = 0)
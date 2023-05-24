import numpy as np
from numpy.linalg import norm
import cv2
# from skimage import threshold_local
import argparse
import imutils
import sys

def get_perspective(image, contours, ratio):
    '''
    this fonction takes image and contours and returns perspective of this contours
    :param image: image, numpy array
    :param contours: contours, numpy array
    :param ratio: rescaling parameter to the original image
    :return: warped image
    '''

    points = contours.reshape(4,2)
    points = points * ratio
    rectangle = np.zeros(shape = (4,2), dtype = 'float32')

    total = points.sum(axis = 1)
    rectangle[0] = points[np.argmin(total)]
    rectangle[2] = points[np.argmax(total)]

    difference = np.diff(points, axis =1)
    rectangle[1] = points[np.argmin(difference)]
    rectangle[3] = points[np.argmax(difference)]

    # rectangle *=ratio

    (a,b,c,d) = rectangle
    width1 = norm(c-d)
    width2 = norm(b-a)

    max_width = max(int(width1), int(width2))
    max_height = max(int(height1), int(height2))

    destination = np.array([[0,0],
                            [max_width-1,0],
                            [max_width-1, max_height-1],
                            0, max_height-1], dtype='float32')

    M = cv2.getPerspectiveTransform(src = rectangle, dst = destination)
    warped_image = cv2.warpPerspective(src = image, M=M, dsize = (max_width, max_height))
    return warped_image

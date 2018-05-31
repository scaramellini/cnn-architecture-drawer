import io
import sys
import numpy as np
import cv2

def tratteggio(x, y, x2, y2, img):
    cv2.line(img, (x, y), (x2, y2), (0, 0, 0), lineType=cv2.LINE_AA)

    deltax = x2 - x

    for i in range(deltax):
        x += 5
        cv2.line(img, (x, y), (x, y2), (255, 255, 255))

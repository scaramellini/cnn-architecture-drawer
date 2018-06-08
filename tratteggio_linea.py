import math
import numpy as np
import cv2

def tratteggio(x0, y0, x1, y1, last):
    deltax = abs(x0 - x1)
    deltay = abs(y0 - y1)
    ipo = int(math.sqrt(deltax ** 2 + deltay ** 2))
    line = np.zeros((ipo*2, ipo*2, 1), np.uint8)
    line.fill(0)
    num_rows, num_cols = line.shape[:2]
    alpha = math.degrees(math.atan(deltay / deltax))
    if y0 < y1 and last == False and x0 > x1:
        rotation_matrix = cv2.getRotationMatrix2D((num_cols / 2, num_rows / 2), alpha, 1)
    elif y0 < y1 and x0 > x1:
        rotation_matrix = cv2.getRotationMatrix2D((num_cols / 2, num_rows / 2), alpha, 1)
    else:
        rotation_matrix = cv2.getRotationMatrix2D((num_cols / 2, num_rows / 2), -alpha, 1)

    turno = True
    if x0 < x1:
        x0, y0 = ipo, ipo
        x1, y1 = x0 + ipo, ipo
    else:
        x0, y0 = ipo, ipo
        x1, y1 = x0 - ipo, ipo
    if deltax < 100 and last == False:
        segmento = ipo / 15
    else:
        segmento = ipo / 10
    base = ((math.cos(alpha) + deltax) / segmento)

    if x0 < x1:
        supx = x0
        savex = x0
        savey = y0
        while x0 < x1 - base - 5:
            x0 = savex
            y0 = savey
            supx += base
            savex = int(math.cos(alpha) + supx)
            if turno == True:
                cv2.line(line, (x0, y0), (savex, savey), (255, 255, 255), lineType=cv2.LINE_AA)
                turno = False
            else:
                if x0 + base < x1:
                    cv2.line(line, (x0, y0), (savex, savey), (0, 0, 0), lineType=cv2.LINE_AA)
                    turno = True
    else:
        supx = x1
        savex = x1
        savey = y1
        while x1 < x0 - base - 5:
            x1 = savex
            y1 = savey
            supx += base
            savex = int(math.cos(alpha) + supx)
            if turno == True:
                cv2.line(line, (x1, y1), (savex, savey), (255, 255, 255), lineType=cv2.LINE_AA)
                turno = False
            else:
                if x1 + base < x0:
                    cv2.line(line, (x1, y1), (savex, savey), (0, 0, 0), lineType=cv2.LINE_AA)
                    turno = True

    line = cv2.warpAffine(line, rotation_matrix, (num_cols, num_rows))

    return line

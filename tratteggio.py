import cv2
import numpy as np
from math import atan, cos, sin, sqrt, floor

LINE_LENGHT = 6
SPACE_LENGHT = 4


def draw_dotted(im, x1, y1, x2, y2, color):
    if x1 == x2:
        # vertical
        if y1 > y2:
            temp = x1
            x1 = x2
            x2 = temp
            temp = y1
            y1 = y2
            y2 = temp
        _x1 = x1
        _y1 = y1
        _x2 = x2
        _y2 = y1 + LINE_LENGHT
        while _y2 < y2:
            cv2.line(im, (_x1, _y1), (_x2, _y2), color)
            _y1 = _y2 + SPACE_LENGHT
            _y2 = _y1 + LINE_LENGHT
    elif y1 == y2:
        # orizzontal
        if x1 > x2:
            temp = x1
            x1 = x2
            x2 = temp
            temp = y1
            y1 = y2
            y2 = temp
        _x1 = x1
        _y1 = y1
        _x2 = x1 + LINE_LENGHT
        _y2 = y2
        while _x2 < x2:
            cv2.line(im, (_x1, _y1), (_x2, _y2), color)
            _x1 = _x2 + SPACE_LENGHT
            _x2 = _x1 + LINE_LENGHT
    else:
        # standard
        if x1 > x2:
            temp = x1
            x1 = x2
            x2 = temp
            temp = y1
            y1 = y2
            y2 = temp
        _x1 = x1
        _y1 = y1
        alpha_angle = atan((y1 - y2) / (x1 - x2))
        print('angle -> ', alpha_angle)
        cos_angle = cos(alpha_angle)
        sin_angle = sin(alpha_angle)
        _x2 = x1 + int(cos_angle * LINE_LENGHT)
        _y2 = y1 + int(sin_angle * LINE_LENGHT)
        while True:
            if x1<x2:
                if _x1 >= x2:
                    break
            else:
                if _x1 <= x2:
                    break
            cv2.line(im, (_x1, _y1), (_x2, _y2), color)
            _x1 = _x2 + int(cos_angle * SPACE_LENGHT)
            _y1 = _y2 + int(sin_angle * SPACE_LENGHT)
            _x2 = _x1 + int(cos_angle * LINE_LENGHT)
            _y2 = _y1 + int(sin_angle * LINE_LENGHT)
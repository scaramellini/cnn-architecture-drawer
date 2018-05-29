import cv2
import numpy as np
import json

OFFSET_FROM_SET_TO_SET = 20
OFFSET_FROM_RECT_TO_RECT = 5
POLY_RECT_WH = 10
# distance from left corner to left corner of poly (both x asnd y)
POLY_FROM_LEFT_TO_LEFT_CORNER_XY = 100
POLY_TOTAL_WH = POLY_FROM_LEFT_TO_LEFT_CORNER_XY + POLY_RECT_WH


def draw_rects(startx, starty, w, h, rects_count, image):
    for i in range(rects_count):
        x = startx + OFFSET_FROM_RECT_TO_RECT * i
        y = starty + OFFSET_FROM_RECT_TO_RECT * i
        if i % 2 == 0:
            colore = 255
        else:
            colore = 128
        cv2.rectangle(image, (x, y), (x + w, y + h), colore, thickness=-1)
        cv2.rectangle(image, (x, y), (x + w, y + h), 0, thickness=1)


def draw_lines():
    pass


def _fillPoly(points, img, fill_color):
    cv2.fillPoly(img, points, fill_color, lineType=cv2.LINE_AA)
    cv2.polylines(img, points, True, 0, lineType=cv2.LINE_AA)


def draw_poly(startx, starty, image):
    # upper rect
    points = np.array([[startx, starty], [startx + POLY_RECT_WH, starty],
                       [startx + POLY_FROM_LEFT_TO_LEFT_CORNER_XY + POLY_RECT_WH,
                        starty + POLY_FROM_LEFT_TO_LEFT_CORNER_XY],
                       [startx + POLY_FROM_LEFT_TO_LEFT_CORNER_XY, starty + POLY_FROM_LEFT_TO_LEFT_CORNER_XY],
                       ])

    _fillPoly([points], image, 128)
    # left rect
    # front rect


if __name__ == '__main__':
    # Main
    with open('input.json', 'r') as input_file:
        input_data = json.load(input_file)

    # Create output image based on the sizes
    '''
    w:
        for every set of rects, get his w
        add a offset for every set
        add the width of the last solid
    '''
    sum_width = 0
    for rect_set in input_data['blocks']:
        sum_width += rect_set['w']
        sum_width += OFFSET_FROM_RECT_TO_RECT * (rect_set['rects_num'] - 1)
    sum_width += POLY_TOTAL_WH
    sum_width += OFFSET_FROM_SET_TO_SET * len(input_data['blocks'])
    '''
    h:
        for every set of rects, get the highest based 
        also on the offsets for every rect.
        check if it is shorter than poly height
    '''
    max_height = -1
    for rect_set in input_data['blocks']:
        set_height = rect_set['h'] + \
                     rect_set['rects_num'] * OFFSET_FROM_RECT_TO_RECT
        if max_height < set_height:
            max_height = set_height
    if max_height < POLY_TOTAL_WH:
        max_height = POLY_TOTAL_WH

    output_image = np.zeros((max_height, sum_width, 1), dtype=np.uint8)
    output_image.fill(255)

    lastStartX = 0
    for rects_data in input_data['blocks']:
        width, height, rects_num = rects_data.values()
        print('width -> ', width)
        print('height -> ', height)
        print('rects_num -> ', rects_num)
        draw_rects(lastStartX, 0, width, height, rects_num, output_image)
        lastStartX += width + OFFSET_FROM_RECT_TO_RECT * (rects_num - 1) + OFFSET_FROM_SET_TO_SET

    draw_poly(lastStartX, 0, output_image)
    # draw_lines()
    cv2.imshow('Output', output_image)
    cv2.waitKey()
    cv2.destroyAllWindows()

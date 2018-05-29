import cv2
import json

OFFSET_FROM_RECT_TO_RECT = 5
POLY_RECT_W = 10
# distance x from left corner to left corner of poly
POLY_FROM_LEFT_TO_LEFT_CORNER_X = 100
POLY_TOTAL_W = POLY_FROM_LEFT_TO_LEFT_CORNER_X + POLY_RECT_W


def draw_rects(startx, starty, w, h):
    pass


def draw_lines():
    pass


def draw_poly():
    pass


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
    sum_width += POLY_TOTAL_W
    print(sum_width)

    for rects_data in input_data['blocks']:
        width, height, rects_num = rects_data.values()
        print('width -> ', width)
        print('height -> ', height)
        print('rects_num -> ', rects_num)
        #draw_rects()
        #draw_lines()
        #draw_solid()

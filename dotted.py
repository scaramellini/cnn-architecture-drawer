import numpy as np
import cv2


def line_iterator(p1x, p1y, p2x, p2y):
    '''
    Ritorna una lista iterabile dei punti di una linea AA
    :param p1x: coordinata x del primo punto
    :param p1y: coordinata y del primo punto
    :param p2x: coordinata x del secondo punto
    :param p2y: coordinata y del secondo punto
    :return: lista iterbile con i punti e la loro intensita' di una linea AA
    '''
    dx = abs(p1x - p2x)
    dy = abs(p1y - p2y)
    matrix = np.zeros(shape=(dy + 1, dx + 1), dtype=np.uint8)
    matrix.fill(255)
    if p1x < p2x:
        offsetx = p1x
    else:
        offsetx = p2x

    if p1y < p2y:
        offsety = p1y
    else:
        offsety = p2y
    cv2.line(matrix, (p1x - offsetx, p1y - offsety), (p2x - offsetx, p2y - offsety), 0, lineType=cv2.LINE_AA)
    cv2.imshow('mat', matrix)
    ritorno = []
    for i, riga in enumerate(matrix):
        for j, pixel in enumerate(riga):
            if pixel != 255:
                ritorno.append((i, j, pixel))
    return ritorno


def dotted_line(p1x, p1y, p2x, p2y, img):
    '''
    Disegnare una linea
    :param p1x:
    :param p1y:
    :param p2x:
    :param p2y:
    :param img:
    :return:
    '''
    iteratore = line_iterator(p1x, p1y, p2x, p2y)

    if p1x < p2x:
        offsetx = p1x
    else:
        offsetx = p2x

    if p1y < p2y:
        offsety = p1y
    else:
        offsety = p2y

    for indice, pixel in enumerate(iteratore):
        if indice % 24 < 18:
            print(' x -> ', pixel[0], 'y -> ', pixel[1])
            print(' p1x -> ', offsetx, 'p1y -> ', offsety)
            try:
                indicex = pixel[0] + offsetx
                indicey = pixel[1] + offsety
                img[indicex][indicey] = 255 - pixel[2]
            except:
                pass


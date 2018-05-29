import io
import sys

# Utilizza il file passato come parametro come standard input
if len(sys.argv) > 1:
    filename = sys.argv[1]
    inp = ''.join(open(filename, "r").readlines())
    sys.stdin = io.StringIO(inp)

import numpy as np
import cv2
from linea import linea_tratteggiata

font = cv2.FONT_ITALIC

listax = []
listay = []
lix = []
liy = []
listaAumento = []
listaAumentoSotto = []
listaSolido = []

def creaSolido(listax, listay):

    x, y = listax.pop(), listay.pop()
    listax.append(x)
    listay.append(y)
    x += 200
    y -= 40
    listaSolido.append(x)
    listaSolido.append(y)

    pts = np.array([[x, y], [x + 20, y], [x + 120, y + 200], [x + 100, y + 200]], np.int32)
    cv2.fillPoly(img, [pts], (169, 169, 169), lineType=cv2.LINE_AA)
    cv2.polylines(img, [pts], True, (0, 0, 0), lineType=cv2.LINE_AA)

    pts = np.array([[x + 100, y + 200], [x + 120, y + 200], [x + 120, y + 220], [x + 100, y + 220]], np.int32)
    cv2.fillPoly(img, [pts], (169, 169, 169), lineType=cv2.LINE_AA)
    cv2.polylines(img, [pts], True, (0, 0, 0), lineType=cv2.LINE_AA)

    pts = np.array([[x, y], [x + 100, y + 200], [x + 100, y + 220], [x, y + 20]], np.int32)
    cv2.fillPoly(img, [pts], (128, 128, 128), lineType=cv2.LINE_AA)
    cv2.polylines(img, [pts], True, (0, 0, 0), lineType=cv2.LINE_AA)

    listaSolido.append(x+100)
    listaSolido.append(y+220)


def creaLineeSopra(listax, listay, listaAumento, solido):
    lista2x = listax.copy()
    lista2y = listay.copy()
    dim = len(listax)
    aumentoSolido = listaAumento.pop()
    for indice in range(dim - 1):
        x, y = listax.pop(), listay.pop()
        x2, y2 = listax.pop(), listay.pop()
        aumento = listaAumento.pop()
        if indice < dim:
            listax.append(x2)
            listay.append(y2)
        linea_tratteggiata(x, y, x2+aumento, y2, img)
    if int(solido) == 1:
        sy = listaSolido.pop()
        sx = listaSolido.pop()
        linea_tratteggiata(lista2x[int(nodo)-1] + aumentoSolido, lista2y[int(nodo)-1], sx, sy, img)



def creaLineeSotto(lix, liy, listaAumentoSotto):
    li2x = lix.copy()
    li2y = liy.copy()
    dim = len(lix)
    for indice in range(dim - 1):
        x, y = lix.pop(), liy.pop()
        x2, y2 = lix.pop(), liy.pop()
        aumento = listaAumentoSotto.pop()
        if indice < dim:
            lix.append(x2)
            liy.append(y2)
        linea_tratteggiata(x-aumento, y, x2, y2, img)
    if int(solido) == 1:
        sy = listaSolido.pop()
        sx = listaSolido.pop()
        linea_tratteggiata(li2x[int(nodo)-1], li2y[int(nodo)-1], sx, sy, img)


def crea(nodi, solido, dim):
    Px, Py = -140, 50
    centramento = 0
    for ogni in range(int(nodi)):
        num = input("inserisci il numero di elementi da disegnare  ")
        lato = input("inserisci la dimensione degli elementi  ")
        if int(nodi) > 1:
            centramento = round(dim * int(nodi) / ((int(nodi) / 2) + 1))
        Px += 150
        aumento = int(lato)*2
        listaAumento.append(aumento)
        x, y = Px, Py
        cv2.putText(img, num + '@' + lato + '*' + lato, (x, y - 20 + centramento), font, 0.5, (0, 0, 0), 1, cv2.LINE_AA)

        if int(num) < 10:

            if int(num) % 2 == 0:

                for each in range(int(num)):

                    if each % 2 == 0:
                        cv2.rectangle(img, (x, y + centramento), (x + aumento, y + aumento + centramento), thickness=-1,
                                      color=(128, 128, 128))
                        cv2.rectangle(img, (x, y + centramento), (x + aumento, y + aumento + centramento), thickness=1,
                                      color=(0, 0, 0))

                        if each == 0:
                            listax.append(x)
                            listay.append(y + centramento)

                        if each == int(num) - 1:
                            lix.append(x + aumento)
                            liy.append(y + aumento + centramento)

                        x += 4
                        y += 7
                    else:

                        cv2.rectangle(img, (x, y + centramento), (x + aumento, y + aumento + centramento), thickness=-1,
                                      color=(255, 255, 255))
                        cv2.rectangle(img, (x, y + centramento), (x + aumento, y + aumento + centramento), thickness=1,
                                      color=(0, 0, 0))

                        if each == int(num) - 1:
                            lix.append(x + aumento)
                            liy.append(y + aumento + centramento)

                        x += 4
                        y += 7
            else:
                for each in range(int(num)):

                    if each % 2 == 0:
                        cv2.rectangle(img, (x, y + centramento), (x + aumento, y + aumento + centramento), thickness=-1,
                                      color=(255, 255, 255))
                        cv2.rectangle(img, (x, y + centramento), (x + aumento, y + aumento + centramento), thickness=1,
                                      color=(0, 0, 0))

                        if each == 0:
                            listax.append(x)
                            listay.append(y + centramento)

                        if each == int(num) - 1:
                            lix.append(x + aumento)
                            liy.append(y + aumento + centramento)

                        x += 4
                        y += 7
                    else:

                        cv2.rectangle(img, (x, y + centramento), (x + aumento, y + aumento + centramento), thickness=-1,
                                      color=(128, 128, 128))
                        cv2.rectangle(img, (x, y + centramento), (x + aumento, y + aumento + centramento), thickness=1,
                                      color=(0, 0, 0))

                        if each == int(num) - 1:
                            lix.append(x + aumento)
                            liy.append(y + aumento + centramento)

                        x += 4
                        y += 7
        else:
            if int(num) % 2 == 0:

                for each in range(10):

                    if each % 2 == 0:
                        cv2.rectangle(img, (x, y + centramento), (x + aumento, y + aumento + centramento), thickness=-1,
                                      color=(128, 128, 128))
                        cv2.rectangle(img, (x, y + centramento), (x + aumento, y + aumento + centramento), thickness=1,
                                      color=(0, 0, 0))

                        if each == 0:
                            listax.append(x)
                            listay.append(y + centramento)
                        if each == 9:
                            lix.append(x + aumento)
                            liy.append(y + aumento + centramento)

                        x += 4
                        y += 7

                    else:
                        cv2.rectangle(img, (x, y + centramento), (x + aumento, y + aumento + centramento), thickness=-1,
                                      color=(255, 255, 255))
                        cv2.rectangle(img, (x, y + centramento), (x + aumento, y + aumento + centramento), thickness=1,
                                      color=(0, 0, 0))

                        if each == 9:
                            lix.append(x + aumento)
                            liy.append(y + aumento + centramento)

                        x += 4
                        y += 7
            else:
                for each in range(10):

                    if each % 2 == 0:
                        cv2.rectangle(img, (x, y + centramento), (x + aumento, y + aumento + centramento), thickness=-1,
                                      color=(255, 255, 255))
                        cv2.rectangle(img, (x, y + centramento), (x + aumento, y + aumento + centramento), thickness=1,
                                      color=(0, 0, 0))

                        if each == 0:
                            listax.append(x)
                            listay.append(y + centramento)
                        if each == 9:
                            lix.append(x + aumento)
                            liy.append(y + aumento + centramento)

                        x += 4
                        y += 7

                    else:
                        cv2.rectangle(img, (x, y + centramento), (x + aumento, y + aumento + centramento), thickness=-1,
                                      color=(128, 128, 128))
                        cv2.rectangle(img, (x, y + centramento), (x + aumento, y + aumento + centramento), thickness=1,
                                      color=(0, 0, 0))

                        if each == 9:
                            lix.append(x + aumento)
                            liy.append(y + aumento + centramento)

                        x += 4
                        y += 7

    if int(solido) == 1:
        creaSolido(listax, listay)

    listaAumentoSotto = listaAumento.copy()
    creaLineeSotto(lix,liy,listaAumentoSotto)
    creaLineeSopra(listax,listay,listaAumento,solido)

    return lato


nodo = input("inserisci il numero di nodi da disegnare  ")
solido = input("inserisci 1 se è presente un solido  ")
dim = 150

img = np.zeros((3000, 3000, 1), np.uint8)
img.fill(255)

lato = crea(nodo, solido, dim)

cv2.imshow('image', img)
cv2.resizeWindow('image', (dim * int(nodo)*3, dim * int(nodo)*3))  #dim * int(nodo) + int(lato)

cv2.waitKey(0)
cv2.destroyAllWindows()

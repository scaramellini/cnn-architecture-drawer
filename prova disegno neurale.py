import io
import sys
import numpy as np
import cv2
from linea import linea_tratteggiata
from tenta

# Utilizza il file passato come parametro come standard input
if len(sys.argv) > 1:
    filename = sys.argv[1]
    inp = ''.join(open(filename, "r").readlines())
    sys.stdin = io.StringIO(inp)

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
    x += 150
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

    listaSolido.append(x + 100)
    listaSolido.append(y + 220)


def creaLinee(listax, listay, listaAumento, solido):
    lista2x = listax.copy()
    lista2y = listay.copy()
    dim = len(listax)
    for indice in range(dim - 1):
        x, y = listax.pop(), listay.pop()
        x2, y2 = listax.pop(), listay.pop()
        aumento = listaAumento.pop()
        if indice < dim:
            listax.append(x2)
            listay.append(y2)
        linea_tratteggiata(x - aumento, y, x2, y2, img)
    if solido == True:
        sy = listaSolido.pop()
        sx = listaSolido.pop()
        linea_tratteggiata(lista2x[int(nodo) - 1], lista2y[int(nodo) - 1], sx, sy, img)


def crea(nodi, solido, dim):
    Px, Py = -140, 50
    centramento = 0
    for ogni in range(int(nodi)):
        Px += 150
        x, y = Px, Py
        num = input("inserisci il numero di elementi da disegnare  ")
        base = input("inserisci la dimensione degli elementi  ")
        altezza = input("inserisci l'altezza degli elementi  ")
        info = input("informazioni addizionali:  ")
        if int(nodi) > 1:
            centramento = round(dim * int(nodi) / ((int(nodi) / 2) + 1))
        aumentoBase = int(base) * 2
        aumentoAltezza = int(altezza) * 2
        listaAumento.append(aumentoBase)
        cv2.putText(img, num + '@' + base + '*' + altezza, (x, y - 20 + centramento), font, 0.5, (0, 0, 0), 1,
                    cv2.LINE_AA)

        if int(num) >= 10:
            num = 10

        if int(num) % 2 == 0:
            color1 = (128, 128, 128)
            color2 = (255, 255, 255)
        else:
            color2 = (128, 128, 128)
            color1 = (255, 255, 255)

        for each in range(int(num)):

            if each % 2 == 0:
                cv2.rectangle(img, (x, y + centramento), (x + aumentoBase, y + aumentoAltezza + centramento),
                              thickness=-1, color=color1)
                cv2.rectangle(img, (x, y + centramento), (x + aumentoBase, y + aumentoAltezza + centramento),
                              thickness=1, color=(0, 0, 0))
            else:

                cv2.rectangle(img, (x, y + centramento), (x + aumentoBase, y + aumentoAltezza + centramento),
                              thickness=-1, color=color2)
                cv2.rectangle(img, (x, y + centramento), (x + aumentoBase, y + aumentoAltezza + centramento),
                              thickness=1, color=(0, 0, 0))

            if each == 0:
                listax.append(x + aumentoBase)
                listay.append(y + centramento)

            if each == int(num) - 1:
                lix.append(x + aumentoBase)
                liy.append(y + aumentoAltezza + centramento)

            x += 4
            y += 7

        cv2.putText(img, info, (x, y + aumentoAltezza + centramento + 20), font, 0.5, (0, 0, 0), 1,
                    cv2.LINE_AA)

    if solido == True:
        creaSolido(listax, listay)

    listaAumentoSotto = listaAumento.copy()
    creaLinee(lix, liy, listaAumentoSotto, solido)
    creaLinee(listax, listay, listaAumento, solido)

    return base


nodo = input("inserisci il numero di nodi da disegnare  ")
solido = bool(input("inserisci 1 se è presente un solido  "))
dim = 150

img = np.zeros((3000, 3000, 1), np.uint8)
img.fill(255)

base = crea(nodo, solido, dim)

cv2.imshow('image', img)
cv2.resizeWindow('image', (dim * int(nodo) * 3, dim * int(nodo) * 3))

cv2.waitKey(0)
cv2.destroyAllWindows()

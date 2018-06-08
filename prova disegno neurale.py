import numpy as np
import cv2
import json
import math
from tratteggio_linea import tratteggio

with open("dati2.json", "r") as leggi:

    contenutojson = json.load(leggi)

    font = cv2.FONT_ITALIC

    nodo = 0
    solido = 0
    info = []
    listax = []
    listay = []
    lix = []
    liy = []
    listaAumento = []
    listaAumentoSotto = []
    listaSolidoSopra = []
    listaSolidoSotto = []
    lati = []

    def disegnaRigheSolido(lista2x, lista2y, listaSolido, lato, pos, prolunga):

        listaScritte = []
        pas = True
        for i in range(int(solido)):
            aumento = prolunga

            if pos == True and pas == True:
                for each in range(len(contenutojson)):
                    if contenutojson[each]["type"] == "connectionSolid":
                        info = contenutojson[each]["bottomText"]
                        listaScritte.append(info)
                listaScritte.reverse()
                pas = False

            if pos == False and pas == True:
                for each in range(len(contenutojson)):
                    if contenutojson[each]["type"] == "solid":
                        info = contenutojson[each]["upperText"]
                        info.reverse()
                        listaScritte.append(info)
                listaScritte.reverse()
                pas = False

            if i == int(solido) - 1:
                sy = listaSolido.pop()
                sx = listaSolido.pop()
                for each in range(len(listaScritte[i])):
                    if pos == False:
                        aumento -= 15
                        cv2.putText(img, listaScritte[i][each], (sx, sy + aumento), font, 0.45, (0, 0, 0), 1,
                                    cv2.LINE_AA)
                    else:
                        aumento += 15
                        cv2.putText(img, listaScritte[i][each], (lista2x[nodo-1] , lista2y[nodo-1] + aumento), font, 0.45, (0, 0, 0), 1,
                                    cv2.LINE_AA)

                last = False
                line = tratteggio(sx,sy,lista2x[int(nodo) - 1],lista2y[int(nodo) - 1], last)
                roix0 = int(sx - line.shape[0] / 2)
                roix1 = int(sx + line.shape[0] / 2)
                roiy0 = int(sy - line.shape[1] / 2)
                roiy1 = int(sy + line.shape[1] / 2)
                roi = img[roiy0:roiy1, roix0:roix1]
                cv2.subtract(roi, line, roi)

            else:
                sy = listaSolido.pop()
                sx = listaSolido.pop()
                sy2 = listaSolido.pop()
                sx2 = listaSolido.pop()
                listaSolido.append(sx2)
                listaSolido.append(sy2)
                for each in range(len(listaScritte[i])):
                    if pos == False:
                        aumento -= 15
                        cv2.putText(img, listaScritte[i][each], (sx , sy2 + aumento), font, 0.45, (0, 0, 0), 1,
                                    cv2.LINE_AA)
                    else:
                        aumento += 15
                        cv2.putText(img, listaScritte[i][each], (sx2 + int(lato[i + 1]), sy2 + aumento), font, 0.45, (0, 0, 0), 1,
                                    lineType=cv2.LINE_AA)

                last = False
                line = tratteggio(sx,sy,sx2 + int(lato[i+1]),sy2,last)
                roix0 = int(sx - line.shape[0]/2)
                roix1 = int(sx + line.shape[0]/2)
                roiy0 = int(sy - line.shape[1]/2)
                roiy1 = int(sy + line.shape[1]/2)
                roi = img[roiy0:roiy1, roix0:roix1]
                cv2.subtract(roi,line, roi)

    def creaSolido(listax, listay):
        x, y = listax.pop(), listay.pop()
        listax.append(x)
        listay.append(y)
        salvax = x
        for k in range(len(contenutojson)):
            if contenutojson[k]["type"] == "solid":
                salvax += 150
                lato = int(contenutojson[k]["side"])/2
                lati.append(lato)
                lunghezza = int(contenutojson[k]["lenght"])
                angolo = math.cos(45) * lunghezza
                listaSolidoSopra.append(salvax)
                listaSolidoSopra.append(y)

                pts = np.array([[salvax, y], [salvax + lato, y], [salvax + lato + angolo, y + lunghezza], [salvax + angolo, y + lunghezza]],
                               np.int32)
                cv2.fillPoly(img, [pts], (169, 169, 169), lineType=cv2.LINE_AA)
                cv2.polylines(img, [pts], True, (0, 0, 0), lineType=cv2.LINE_AA)

                pts = np.array(
                    [[salvax + angolo, y + lunghezza], [salvax + lato + angolo, y + lunghezza], [salvax + lato + angolo, y + lunghezza + lato],
                     [salvax + angolo, y + lunghezza + lato]],
                    np.int32)
                cv2.fillPoly(img, [pts], (169, 169, 169), lineType=cv2.LINE_AA)
                cv2.polylines(img, [pts], True, (0, 0, 0), lineType=cv2.LINE_AA)

                pts = np.array([[salvax, y], [salvax + angolo, y + lunghezza], [salvax + angolo, y + lunghezza + lato], [salvax, y + lato]],
                               np.int32)
                cv2.fillPoly(img, [pts], (128, 128, 128), lineType=cv2.LINE_AA)
                cv2.polylines(img, [pts], True, (0, 0, 0), lineType=cv2.LINE_AA)

                listaSolidoSotto.append(salvax + int(angolo))
                listaSolidoSotto.append(y + lunghezza + int(lato))
        lati.reverse()
        return lati

    def creaLinee(listax, listay, listaAumento):
        dim = len(listax)
        for indice in range(dim - 1):
            x, y = listax.pop(), listay.pop()
            x2, y2 = listax.pop(), listay.pop()
            aumento = listaAumento.pop()
            if indice < dim:
                listax.append(x2)
                listay.append(y2)

            last = True
            line = tratteggio(x-aumento,y,x2,y2,last)
            roix0 = int(x-aumento - line.shape[0] / 2)
            roix1 = int(x-aumento + line.shape[0] / 2)
            roiy0 = int(y - line.shape[1] / 2)
            roiy1 = int(y + line.shape[1] / 2)
            roi = img[roiy0:roiy1, roix0:roix1]
            cv2.subtract(roi, line, roi)

    def crea(nodi, solid, dim):
        listaScritte = []
        Px, Py = 10, 100
        centramento = 0
        for ogni in range(len(contenutojson)):

            for each in range(len(contenutojson)):
                if contenutojson[each]["type"] == "connection":
                    listaScritte.append( contenutojson[each]["bottomText"])

            if contenutojson[ogni]["type"] == "planar":
                riduci = 20
                info = contenutojson[ogni]["upperText"]
                info.reverse()
                x, y = Px, Py
                num = contenutojson[ogni]["layers"]
                base = contenutojson[ogni]["width"]
                altezza = contenutojson[ogni]["height"]
                if int(nodi) > 1:
                    centramento = round(dim * int(nodi) / ((int(nodi) / 2) + 1))
                aumentoBase = int(base)
                aumentoAltezza = int(altezza)
                listaAumento.append(aumentoBase)

                for a in range(len(info)):
                    riduci += 15
                    cv2.putText(img, info[a], (x, y - riduci + centramento), font, 0.5, (0, 0, 0),
                                1,cv2.LINE_AA)

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

                Px = x + aumentoBase + 50

        if len(liy) == 1:
            cv2.putText(img, listaScritte[0], (listax[0], liy[0] + 50), font, 0.5, (0, 0, 0), 1,
                        cv2.LINE_AA)
        else:
            for i in range(len(liy) - 1):
                prolunga = 10
                if liy[i] >= liy[i + 1]:
                    for stringhe in range(len(listaScritte[i])):
                        prolunga += 15
                        cv2.putText(img, listaScritte[i][stringhe], (lix[i], liy[i] + prolunga), font, 0.45, (0, 0, 0), 1,
                                cv2.LINE_AA)
                else:
                    for stringhe in range(len(listaScritte[i])):
                        prolunga += 15
                        cv2.putText(img, listaScritte[i][stringhe], (lix[i], liy[i + 1] + prolunga), font, 0.45, (0, 0, 0), 1,
                                cv2.LINE_AA)
            for stringhe in range(len(listaScritte[i])-2):
                prolunga += 15
                cv2.putText(img, listaScritte[i][stringhe], (lix[i], liy[i] + prolunga), font, 0.45, (0, 0, 0), 1,
                            cv2.LINE_AA)

        if solid == True:
            lato = creaSolido(listax, listay)
            disegnaRigheSolido(lix, liy, listaSolidoSotto, lato, pos=True, prolunga=20)
            disegnaRigheSolido(listax, listay, listaSolidoSopra, lato, pos=False, prolunga=-15)

        listaAumentoSotto = listaAumento.copy()
        creaLinee(lix, liy, listaAumentoSotto)
        creaLinee(listax, listay, listaAumento)

    for i in range(len(contenutojson)):
        if contenutojson[i]["type"] == "planar":
            nodo += 1
        if contenutojson[i]["type"] == "solid":
            solido += 1
            solid = True

    dim = 150

    img = np.zeros((1000, 1500, 1), np.uint8)
    img.fill(255)

    crea(nodo, solid, dim)

    cv2.imshow('image', img)
    cv2.resizeWindow('image', (dim * int(nodo) * 3, dim * int(nodo) * 3))
    cv2.imwrite('cnn_image.jpg',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


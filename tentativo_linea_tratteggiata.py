from linea import createLineIterator
import cv2

salvaY = []

def tratteggio(x, y, x2, y2, img):
    iteratore = createLineIterator((x, y), (x2, y2), img)
    for i, pixels in enumerate(iteratore):
        salvaY.append(pixels[1])
    cv2.line(img, (x, y), (x2, y2), (0, 0, 0), lineType=cv2.LINE_AA)
    print(iteratore)
    deltax = abs(x2 - x)

    for i in range(round(deltax / 10)-1):
        x -= 10
        cv2.line(img, (x,y), (x, y2), (0, 0, 0))

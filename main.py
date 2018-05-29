import numpy as np
import cv2

'''goku = cv2.imread('Screenshot (8).png', -1)
cv2.imshow('image', img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.destroyAllWindows()'''

img = np.zeros((512,512,3), np.uint8)
img.fill(255)

cv2.circle(img,(255,100), 80, (0,0,255), -1)
cv2.circle(img,(255,100), 30, (255,255,255), -1)


cv2.circle(img,(150,290), 80, (0,255,0), -1)
cv2.circle(img,(150,290), 30, (255,255,255), -1)


pts = np.array([[255,100],[150,310],[360,310]], np.int32)
cv2.fillPoly(img,[pts],color=(255,255,255))


cv2.circle(img,(360,290), 80, (255,0,0), -1)
cv2.circle(img,(360,290), 30, (255,255,255), -1)


pts = np.array([[360,290],[300,200],[420,200]], np.int32)
cv2.fillPoly(img,[pts],color=(255,255,255))


font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,470), font, 4,(0,0,0),10,cv2.LINE_AA)


cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

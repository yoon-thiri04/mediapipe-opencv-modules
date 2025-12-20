import cv2
from handtracking_module import handDetector as htm
import time

pTime= 0
cTime = 0
cap = cv2.VideoCapture(0)
detector = htm()
while True:
    success, img = cap.read()
    img =detector.findHands(img)
    lmlist =detector.findPosition(img,draw=False)
    if len(lmlist) != 0:
        print(lmlist[8])
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    # putText , on image(org), round the fps as int and convert to str, the position, font, scale, and color
    cv2.putText(img, str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN, 2,(255,0,255),3)
    cv2.imshow("Image",img)
    cv2.waitKey(1)

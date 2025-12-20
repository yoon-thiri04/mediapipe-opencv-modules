import cv2
from pose_module import poseDetector as pdt
import time

cap = cv2.VideoCapture("D:/Sem8/my_ai_study/advanced_cv/pose_estimation/poseVideos/video3.mp4")

pTime = 0
pose_detector= pdt()

cv2.namedWindow("Image",cv2.WINDOW_NORMAL)
win_w, win_h = 960, 800
cv2.resizeWindow("Image",win_w, win_h)


while True:
    success , img = cap.read()
    
    img = pose_detector.findPose(img)
  
    lmlist = pose_detector.findPosition(img)
    if len(lmlist) != 0:
        print(lmlist[14])
        cv2.circle(img, (lmlist[14][1],lmlist[14][2]),30,(0,0,255),cv2.FILLED)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img,str(int(fps)), (70,100),cv2.FONT_HERSHEY_COMPLEX,3,(255,0,0),3)
    cv2.imshow("Image",img)
    if cv2.waitKey(1) & 0xFF == 27:
            break
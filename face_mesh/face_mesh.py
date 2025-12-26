import mediapipe as mp
import time
import cv2


# 480 points in face mesh 
cap = cv2.VideoCapture("advanced_cv/face_mesh/Videos/4.mp4")
pTime = 0
cv2.namedWindow("Image",cv2.WINDOW_NORMAL)
win_w, win_h = 960, 560
cv2.resizeWindow("Image",win_w, win_h)

# mediapipe part
mpDraw  = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=2)
drawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=1)
while True:
    success, image = cap.read()
    imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)
    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            mpDraw.draw_landmarks(image,faceLms,mpFaceMesh.FACEMESH_CONTOURS,
                                  drawSpec, drawSpec)
            
            for id,lm in enumerate(faceLms.landmark):
                #print(lm) # x, y, z positions normalize from 0 to 1 
                ih, iw, ic = image.shape
                x, y = int(lm.x*iw), int(lm.y*ih)
                print(id, x, y)

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText(image,f"FPS: {int(fps)}",(50,100),cv2.FONT_HERSHEY_PLAIN, 4,(0,255,0),3)
    cv2.imshow("Image",image)
    cv2.waitKey(1)
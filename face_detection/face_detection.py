import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture("D:/Sem8/my_ai_study/advanced_cv/face_detection/videos/1.mp4")
cv2.namedWindow("Image",cv2.WINDOW_NORMAL)
win_w, win_h = 960, 560
cv2.resizeWindow("Image",win_w, win_h)
pTime = 0

mpFace = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
face = mpFace.FaceDetection(0.75)
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = face.process(imgRGB)
    if results.detections:
        for id,detection in enumerate(results.detections):
            #mpDraw.draw_detection(img, detection)
            #print(id,detection)
            #print(detection.score)
            #print(detection.location_data.relative_bounding_box)
            bboxC = detection.location_data.relative_bounding_box
            h,w,c = img.shape
            bbox = int(bboxC.xmin * w), int(bboxC.ymin * h), int(bboxC.width * w), int(bboxC.height * h)

            cv2.rectangle(img ,bbox, (255,0,255),4)
            cv2.putText(img, f'{int(detection.score[0]*100)}%',
                        (bbox[0],bbox[1]-20),
                        cv2.FONT_HERSHEY_PLAIN,4,(255,0,255),4)
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {str(int(fps))}',(50,150),cv2.FONT_HERSHEY_PLAIN,10,
                (0,255,0),4 )
    
    cv2.imshow("Image",img)
    cv2.waitKey(1)

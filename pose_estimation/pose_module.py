import cv2
import mediapipe as mp
import time

# class like object calling(OOP)
class poseDetector():
    def __init__(self, mode= False, upBody = False, smooth=True, 
                 detectionCon=0.5, trackCon = 0.5):
        
        self.mode = mode
        # rm this cause i got unexpected argument error
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon= detectionCon
        self.trackCon = trackCon
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(static_image_mode =self.mode,
                                    
                                     smooth_landmarks= self.smooth,
                                     min_detection_confidence=self.detectionCon,
                                     min_tracking_confidence = self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)

        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks,
                                           self.mpPose.POSE_CONNECTIONS)
        return img
    def findPosition(self, img, draw =True):
        lmlist=[]
        if self.results.pose_landmarks:

            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h,w,c = img.shape
            
                cx, cy = int(lm.x*w), int(lm.y*h)
                lmlist.append([id,cx,cy])
                if draw:
                    cv2.circle(img, (cx,cy), 17, (255,0,0), cv2.FILLED)
        return lmlist
    

def main():
    cap = cv2.VideoCapture('advanced_cv/pose_estimation/poseVideos/video3.mp4')
    pTime = 0
    detector = poseDetector()
    
    cv2.namedWindow("Image", cv2.WINDOW_NORMAL)

    win_w, win_h = 960, 540
    cv2.resizeWindow("Image", win_w, win_h)

    screen_w, screen_h = 1366, 768
    cv2.moveWindow("Image",
               (screen_w - win_w)//2,
               (screen_h - win_h)//2)
    while True:
        success, img = cap.read()
        img= detector.findPose(img)
        lmlist = detector.findPosition(img)
        if len(lmlist)!=0:
            print(lmlist[14])
            cv2.circle(img, (lmlist[14][1], lmlist[14][2]), 30, (0,0,255), cv2.FILLED)
        
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)),(70,50), cv2.FONT_HERSHEY_PLAIN,3,
                    (255,0,0),3)
        cv2.imshow("Image",img)
        if cv2.waitKey(1) & 0xFF == 27:
            break


if __name__ == "__main__":
    main()

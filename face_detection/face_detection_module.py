import cv2
import mediapipe as mp
import time


class FaceDetector():

    def __init__(self, minDetectionCon=0.5):
      # instance variable for this class
      self.mpFace = mp.solutions.face_detection
      self.mpDraw = mp.solutions.drawing_utils
      self.face = self.mpFace.FaceDetection(minDetectionCon)
      
    def findFaces(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self. results = self.face.process(imgRGB)
        bboxes = []
        if self.results.detections:
            for id, detection in enumerate(self.results.detections):
               bboxC = detection.location_data.relative_bounding_box
               h,w,c = img.shape
               bbox = int(bboxC.xmin *w),int(bboxC.ymin * h), int(bboxC.width *w),int(bboxC.height * h)
               bboxes.append([id, bbox,detection.score])
               if draw:
                   
                img = self.fancyDraw(img , bbox)
               
                cv2.putText(img, f"{int(detection.score[0]*100)}%",
                           (bbox[0],bbox[1]-20),
                           cv2.FONT_HERSHEY_PLAIN,4, (0,255,0),3)
        return img, bboxes
    
    def fancyDraw(self,img, bbox,l=30,t = 5, rt =1):
        x, y, w, h = bbox
        x1, y1 = x+w, y+h
        cv2.rectangle(img, bbox, (0,255,0),rt)
        # top left x,y
        cv2.line(img, (x,y),(x+l, y), (0,255,0),t)
        cv2.line(img, (x,y),(x, y+l), (0,255,0),t)

        # top right x1, y
        cv2.line(img, (x1,y),(x1-l, y), (0,255,0),t)
        cv2.line(img, (x1,y),(x1, y+l), (0,255,0),t)
        # bottom left x, y1
        cv2.line(img, (x,y1),(x+l, y1), (0,255,0),t)
        cv2.line(img, (x,y1),(x, y1-l), (0,255,0),t)
        # bottom right x1, y1
        cv2.line(img, (x1,y1),(x1-l, y1), (0,255,0),t)
        cv2.line(img, (x1,y1),(x1, y1-l), (0,255,0),t)
        

        
        return img



def main():
    cap = cv2.VideoCapture(0)
    cv2.namedWindow("Image",cv2.WINDOW_NORMAL)
    win_w, win_h = 960, 560
    cv2.resizeWindow("Image",win_w, win_h)
    pTime = 0
    detector = FaceDetector()
    while True:
        success, img = cap.read()
        img,bboxes = detector.findFaces(img)
        cTime = time.time()
        fps = 1/(cTime- pTime)
        pTime = cTime
        cv2.putText(img, f'FPS: {str(int(fps))}',(50,100),cv2.FONT_HERSHEY_PLAIN,
                    3, (0,255,0),4)
        
        cv2.imshow("Image", img)
        cv2.waitKey(1)
if __name__ == "__main__":
    main()
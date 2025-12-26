import mediapipe as mp
import time
import cv2

class FaceMeshDetector():
    def __init__(self,static_image_mode=False, max_num_faces=2,min_detect_con=0.5, min_tracking_con=0.5):
        self.staticMode = static_image_mode
        self.maxFaces = max_num_faces
        self.minDetectionCon = min_detect_con
        self.minTrackCon= min_tracking_con

        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh
        self.faceMesh = self.mpFaceMesh.FaceMesh(
            static_image_mode = self.staticMode,
            max_num_faces= self.maxFaces,
            min_detection_confidence = self.minDetectionCon,
            min_tracking_confidence = self.minTrackCon
        )
        self.drawSpec = self.mpDraw.DrawingSpec(thickness=1, circle_radius=2)

    def findFaceMesh(self,img,draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceMesh.process(imgRGB)
        faces = []
        if self.results.multi_face_landmarks:
            for faceLms in self.results.multi_face_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img,faceLms,self.mpFaceMesh.FACEMESH_TESSELATION,
                                  self.drawSpec, self.drawSpec) # mpFaceMesh.FACEMESH_TESSELATION for connections and FACEMESH_CONTOURS ,FACEMESH_LEFT_EYE, FACEMESH_RIGHT_EYE
                face =[]
                for id,lm in enumerate(faceLms.landmark):
                    ih, iw, ic = img.shape
                    x, y = int(lm.x*iw), int(lm.y*ih)
                    cv2.putText(img, str(id),(x,y), cv2.FONT_HERSHEY_PLAIN,
                                0.7,(0,255,0),1)
                    
                    face.append([x,y])
                faces.append(face)
        return img,faces

    

def main():
    cap = cv2.VideoCapture("advanced_cv/face_mesh/Videos/5.mp4")
    pTime = 0
    cv2.namedWindow("Image",cv2.WINDOW_NORMAL)
    win_w, win_h = 960, 560
    cv2.resizeWindow("Image",win_w, win_h)
    detector = FaceMeshDetector(max_num_faces=2)
    while True:
        success, image = cap.read()
        img,faces = detector.findFaceMesh(image)
        if len(faces) != 0:
            print(faces[0])
        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime
        cv2.putText(image,f"FPS: {int(fps)}",(50,100),cv2.FONT_HERSHEY_PLAIN, 4,(0,255,0),3)
        cv2.imshow("Image",image)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
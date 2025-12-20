# 🧍 Pose Estimation MediaPipe and OpenCV

This project demonstrates **real-time Pose Estimation** using **MediaPipe** and **OpenCV** in Python.  
Built for **my learning, experimentation, and future extension**.

---

##  Technologies Used

- **Python**: 3.10.11  
- **MediaPipe**: Pose & Hands solutions  
- **OpenCV**: Video processing and visualization  

> ⚠️ MediaPipe officially supports **Python 3.10**, in this project I am using **Python 3.10.11**.

---

### Overview
The pose estimation module uses **MediaPipe Pose** to detect **33 body landmarks** in videos.  
The detected landmarks are drawn on the video frames using OpenCV.

A **custom module (OOP-based)** is created to:
- Detect pose landmarks
- Extract landmark positions
- Make the code reusable and extensible for future features

---

### Module File
- **`pose_module.py`**  
 
The module is designed to be **imported and reused** in other projects.

### Example Usage
- **`new_pose_estimation.py`**  
  This file serves as an **example script** demonstrating how to use  
  `pose_module.py` in a different project context.

---
### Pose Landmarks (Landmark ID → Name)

MediaPipe Pose provides **33 landmarks**, such as:
<img width="723" height="856" alt="media_pipe_poseestimation2" src="https://github.com/user-attachments/assets/6727946b-8cf3-48d5-89a4-03bce9757f42" />


| ID | Landmark Name |
|----|---------------|
| 0  | Nose |
| 1  | Left eye (inner) |
| 2  | Left eye |
| 3  | Left eye (outer) |
| 4  | Right eye (inner) |
| 5  | Right eye |
| 6  | Right eye (outer) |
| 7  | Left ear |
| 8  | Right ear |
| 9  | Mouth (left) |
| 10 | Mouth (right) |
| 11 | Left shoulder |
| 12 | Right shoulder |
| 13 | Left elbow |
| 14 | Right elbow |
| 15 | Left wrist |
| 16 | Right wrist |
| 17 | Left pinky |
| 18 | Right pinky |
| 19 | Left index |
| 20 | Right index |
| 21 | Left thumb |
| 22 | Right thumb |
| 23 | Left hip |
| 24 | Right hip |
| 25 | Left knee |
| 26 | Right knee |
| 27 | Left ankle |
| 28 | Right ankle |
| 29 | Left heel |
| 30 | Right heel |
| 31 | Left foot index |
| 32 | Right foot index |

---

### Performance Note (Latency)

Pose estimation may show **noticeable latency** on systems with limited CPU resources.

Possible reasons:
- Full-body landmark detection is computationally expensive
- Processing **video files** instead of static images or low-resolution camera input
- Running entirely on CPU without GPU acceleration

This is expected behavior on laptops with modest hardware.

---

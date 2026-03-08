
from deepface import DeepFace
import cv2

def detect_emotion():
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    cam.release()

    result = DeepFace.analyze(
        frame,
        actions=['emotion'],
        enforce_detection=False
    )

    return result[0]['dominant_emotion']

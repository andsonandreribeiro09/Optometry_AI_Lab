import mediapipe as mp
import cv2

mp_face_mesh = mp.solutions.face_mesh

def detect_face(frame):
    """
    Retorna landmarks do rosto usando MediaPipe Face Mesh.
    """
    face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True)
    return face_mesh.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

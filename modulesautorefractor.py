import cv2
import numpy as np
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

def estimate_refraction(frame):

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    if not results.multi_face_landmarks:
        return None

    landmarks = results.multi_face_landmarks[0].landmark

    # pontos da íris
    left_eye = landmarks[468]
    right_eye = landmarks[473]

    # coordenadas
    lx = left_eye.x
    rx = right_eye.x

    # diferença horizontal
    eye_offset = abs(rx - lx)

    # simulação de estimativa
    sphere = -2.0 + eye_offset
    cylinder = -0.5
    axis = 180

    return {
        "sphere": round(sphere,2),
        "cylinder": cylinder,
        "axis": axis
    }
import cv2
import mediapipe as mp
import numpy as np

from mediapipe.tasks.python import vision
from mediapipe.tasks.python import BaseOptions

# caminho do modelo
MODEL_PATH = "face_landmarker.task"

options = vision.FaceLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=MODEL_PATH),
    running_mode=vision.RunningMode.IMAGE
)

detector = vision.FaceLandmarker.create_from_options(options)


def detect_face(frame):
    """
    Detecta landmarks faciais usando a nova API do MediaPipe.
    """

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb
    )

    result = detector.detect(mp_image)

    return result

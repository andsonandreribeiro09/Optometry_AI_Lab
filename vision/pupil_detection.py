import cv2
import numpy as np

def detect_pupil(frame):

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gray = cv2.GaussianBlur(gray,(7,7),0)

    circles = cv2.HoughCircles(
        gray,
        cv2.HOUGH_GRADIENT,
        dp=1,
        minDist=50,
        param1=50,
        param2=30,
        minRadius=5,
        maxRadius=30
    )

    pupils = []

    if circles is not None:

        circles = np.uint16(np.around(circles))

        for c in circles[0,:]:

            pupils.append((c[0],c[1],c[2]))

    return pupils
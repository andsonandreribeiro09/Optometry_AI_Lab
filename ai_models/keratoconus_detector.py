import numpy as np

def detect_keratoconus(curvature):

    if curvature > 47:

        return True

    return False
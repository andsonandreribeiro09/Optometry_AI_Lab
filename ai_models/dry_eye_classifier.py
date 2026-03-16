import numpy as np

def classify_dry_eye(blink_rate):

    if blink_rate < 8:

        return "Possível olho seco"

    return "Normal"
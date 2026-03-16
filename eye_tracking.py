import numpy as np

def track_eye(pupil_positions):

    movements = []

    for i in range(1,len(pupil_positions)):

        dx = pupil_positions[i][0] - pupil_positions[i-1][0]
        dy = pupil_positions[i][1] - pupil_positions[i-1][1]

        movements.append((dx,dy))

    return movements
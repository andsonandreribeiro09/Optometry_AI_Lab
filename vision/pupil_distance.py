import numpy as np

def monocular_pd(left, right):
    distance = np.sqrt((right[0]-left[0])**2 + (right[1]-left[1])**2)
    mm_per_pixel = 0.26
    return distance * mm_per_pixel

# alias para compatibilidade
calculate_pd = monocular_pd
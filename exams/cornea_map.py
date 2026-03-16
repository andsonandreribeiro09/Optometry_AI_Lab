import numpy as np

def generate_cornea_map():

    cornea = np.random.normal(43, 1, (10,10))

    curvature = cornea.mean()

    return curvature, cornea
import numpy as np

def generate_cornea_surface():

    x = np.linspace(-3,3,50)
    y = np.linspace(-3,3,50)

    X,Y = np.meshgrid(x,y)

    Z = np.exp(-(X**2+Y**2))

    return X,Y,Z
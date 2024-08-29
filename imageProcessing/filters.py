import numpy as np
from .convolution import convolute
from .utilities import gaussian

def greyscale(img):
    return np.mean(img,axis=-1)
def gaussian_blur(img, radius = 2, sigma = 1):
    x = np.arange(-radius,radius+1)
    y = np.arange(-radius,radius+1).reshape(-1,1)
    kernel = gaussian(x,y,sigma)
    kernel = (kernel - np.min(kernel))/(np.max(kernel) - np.min(kernel))
    out = convolute(img,kernel,padding=True)
    return out

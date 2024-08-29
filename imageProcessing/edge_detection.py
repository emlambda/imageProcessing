import numpy as np
from .convolution import convolute
from .utilities import magnitude, slope, suppression, centroid
from .filters import gaussian_blur

def edge_detection(img):
    kx = np.array([[-1,0,1],
                   [-2,0,2],
                   [-1,0,1]])
    ky = kx.T
    ix = convolute(img,kx,padding=True)
    iy = convolute(img,ky,padding=True)
    mag = magnitude(ix,iy)
    slop = slope(ix,iy)
    sup = suppression(slop,mag)
    return mag,sup,slop
def corners(img,k=0.05,thresh=0.05, cent=10):
    kx = np.array([[-1,0,1],
                   [-2,0,2],
                   [-1,0,1]])
    ky = kx.T
    ix = convolute(img,kx,padding=True)
    iy = convolute(img,ky,padding=True)
    A = ix**2
    B = iy**2
    C = ix*iy

    A = gaussian_blur(A)
    B = gaussian_blur(B)
    C = gaussian_blur(C)

    corn = (A*B-(C**2))-k*((A+B)**2)
    threshold = thresh * np.max(corn)
    corn = np.where(corn > threshold)
    centroids = []
    for i in range(len(corn[0])):
        ind = magnitude(corn[0][i]-corn[0],corn[1][i]-corn[1])
        centroids.append(centroid(corn[1][ind<cent],corn[0][ind<cent]))
    return np.array(list(set(centroids)))

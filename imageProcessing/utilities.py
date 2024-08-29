import numpy as np

def gaussian(x,y,sigma):
    return np.exp(-(x**2+y**2)/(2*sigma**2))*(1/(2*np.pi*sigma**2))
def magnitude(x,y):
    return np.sqrt(x**2+y**2).astype(float)
def slope(x,y):
    return np.arctan(y/x).astype(float)
def suppression(slop, mag):
    out = np.zeros(slop.shape)
    n = slop*180/np.pi
    n[n<0] += 180
    print(mag.shape)
    print(slop.shape)
    for i in range(1,len(slop)-1):
        for j in range(1,len(slop[0])-1):
            if slop[i,j] < 22.5 or slop[i,j] >= 157.5:
                if mag[i,j] <= mag[i,j+1] or mag[i,j] <= mag[i,j-1]:
                    out[i,j] = mag[i,j]
                continue
            elif slop[i,j] < 67.5:
                if mag[i,j] <= mag[i-1,j+1] or mag[i,j] <= mag[i+1,j-1]:
                    out[i,j] = mag[i,j]
                continue
            elif slop[i,j] < 112.5:
                if mag[i,j] <= mag[i-1,j] or mag[i,j] <= mag[i+1,j]:
                    out[i,j] = mag[i,j]
                continue
            elif slop[i,j] < 157.5:
                if mag[i,j] <= mag[i-1,j-1] or mag[i,j] <= mag[i+1,j+1]:
                    out[i,j] = mag[i,j]
    return out
def centroid(x,y):
    l = len(x)
    c_x = sum(x)/l
    c_y = sum(y)/l
    return (int(c_x),int(c_y))

#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def center(a):
    y = (a.shape[0]-1)/2
    x = (a.shape[1]-1)/2
    return (y,x)   # note the order: (center_y, center_x)

def radial_distance(a):
    midpoint = center(a)
    list_distances = [np.linalg.norm((j-midpoint[1], i-midpoint[0])) for i in range(a.shape[0]) \
    for j in range(a.shape[1])]
    distances = np.asarray(list_distances).reshape((a.shape[0], a.shape[1]))
    return distances

def scale(a, tmin=0.0, tmax=1.0):
    """Returns a copy of array 'a' with its values scaled to be in the range
[tmin,tmax]."""
    a_scaled = np.interp(a, (a.min(), a.max()), (tmin, tmax))
    return a_scaled

def radial_mask(a):
    a = scale(1 - radial_distance(a))
    return a

def radial_fade(a):
    a = a * radial_mask(a)[:,:, np.newaxis]
    return a

def main():
    image = plt.imread("src/painting.png").copy()
    f, ax = plt.subplots(3,1)
    ax[0].imshow(image)
    ax[1].imshow(radial_mask(image))
    ax[2].imshow(radial_fade(image))
    plt.show()

if __name__ == "__main__":
    main()

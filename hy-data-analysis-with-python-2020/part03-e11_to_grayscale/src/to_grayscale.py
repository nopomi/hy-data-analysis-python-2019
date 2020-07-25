#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def to_grayscale(image):
    copy = image.copy()
    r = copy[:,:,0]
    g = copy[:,:,1]
    b = copy[:,:,2]
    grayscale = r*0.2126 + g*0.7152 + b*0.0722
    plt.imshow(grayscale)
    plt.gray()
    return grayscale

def to_red(image):
    copy = image.copy()
    copy[:,:,1:] = 0
    return copy

def to_green(image):
    copy = image.copy()
    copy[:,:,(0,2)] = 0
    return copy

def to_blue(image):
    copy = image.copy()
    copy[:,:,0:2] = 0
    return copy

def main():
    painting = plt.imread("src/painting.png")
    plt.imshow(painting)
    plt.show()
    grayscale = to_grayscale(painting)
    red = to_red(painting)
    green = to_green(painting)
    blue = to_blue(painting)
    fig, ax = plt.subplots(3,1)
    ax[0].imshow(red)
    ax[1].imshow(green)
    ax[2].imshow(blue)
    plt.show()



if __name__ == "__main__":
    main()

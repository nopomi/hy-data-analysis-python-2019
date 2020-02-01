#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def subfigures(a):
    fig, ax = plt.subplots(1,2)
    ax[0].plot(a[:,0], a[:,1])
    ax[1].scatter(a[:,0], a[:,1], s=a[:,3], c=a[:,2])
    plt.show()

def main():
    grades_1 = np.array([89, 90, 70, 89, 100, 80, 90, 100])
    grades_2 = np.array([30, 29, 49, 48, 100, 48, 38, 45])
    colors = np.array(np.random.randn(1, 8)[0])
    sizes = np.array(np.random.randint(100, size=8))
    a = np.column_stack((grades_1, grades_2, colors, sizes))
    subfigures(a)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

def main():
    a = np.array([2,4,6,7])
    b = np.array([4,3,5,1])
    c = np.array([1,2,3,4])
    d = np.array([4,2,3,1])
    plt.plot(a,b)
    plt.plot(c,d)
    plt.title("Strange snakes seen from above")
    plt.xlabel("other fence wall")
    plt.ylabel("fence wall")
    plt.show()


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import numpy as np
import scipy.linalg

def vector_angles(X, Y):
    top = np.sum(X*Y, axis=1)
    bottom_1 = np.sqrt(np.sum(X*X, axis=1))
    bottom_2 = np.sqrt(np.sum(Y*Y, axis=1))
    bottom = bottom_1 * bottom_2
    full = top/bottom
    A = np.arccos(np.clip(full, -1.0, 1.0))
    A = np.degrees(A)
    return np.array(A)

def main():
    X = np.random.randint(10, size=(4,5))
    Y = np.random.randint(10, size=(4,5))
    vector_angles(X, Y)
    X2 = np.array([[1,2,3],[3,2,1]])
    Y2 = np.array([[3,2,1],[1,2,3]])
    vector_angles(X2, Y2)

if __name__ == "__main__":
    main()

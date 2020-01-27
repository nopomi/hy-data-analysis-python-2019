#!/usr/bin/env python3

import numpy as np
#import scipy.linalg

def vector_lengths(a):
    A = np.sqrt(np.sum(a**2, axis=1))
    return np.array(A)

def main():
    a = np.random.randint(10, size=(4,5))
    print(vector_lengths(a))

if __name__ == "__main__":
    main()

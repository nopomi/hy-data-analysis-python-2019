#!/usr/bin/env python3
import numpy as np
from functools import reduce


def multiply_arrays(a, b):
    return a@b

def matrix_power(a, n):
    if n == 0:
        return np.eye(a.shape[0])
    if n < 0:
        a = np.linalg.inv(a)
        n = -1*n
    A = reduce(multiply_arrays, (a for i in range(n)))
    return A

def main():
    a = np.random.randint(11, size=25).reshape(5,5)
    n = -3
    print(matrix_power(a,n))


if __name__ == "__main__":
    main()

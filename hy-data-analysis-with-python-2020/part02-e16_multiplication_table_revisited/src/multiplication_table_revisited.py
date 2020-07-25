#!/usr/bin/env python3

import numpy as np

def multiplication_table(n):
    x = np.arange(n)
    y = np.arange(n).reshape(n, 1)
    return x*y

def main():
    print(multiplication_table(10))

if __name__ == "__main__":
    main()

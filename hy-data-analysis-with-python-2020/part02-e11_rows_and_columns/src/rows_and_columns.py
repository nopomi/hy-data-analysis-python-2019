#!/usr/bin/env python3

import numpy as np

def get_rows(a):
    L = []
    for i in range(a.shape[0]):
        L.append(a[i,:])
    return L

def get_columns(a):
    L = []
    for i in range(a.shape[1]):
        L.append(a[:,i])
    return L

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Rows:", get_rows(a))
    print("Columns:", get_columns(a))

if __name__ == "__main__":
    main()

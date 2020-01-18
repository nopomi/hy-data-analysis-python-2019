#!/usr/bin/env python3

import numpy as np

def get_row_vectors(a):
    return []

def get_column_vectors(a):
    return []

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Row vectors:", get_row_vectors(a))
    print("Column vectors:", get_column_vectors(a))

if __name__ == "__main__":
    main()

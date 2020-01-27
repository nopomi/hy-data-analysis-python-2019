#!/usr/bin/env python3

import numpy as np

def diamond(n):
    top_right = np.eye(n, dtype=int)
    top_left = np.rot90(top_right)
    top_half = np.concatenate((top_left, top_right[:,1:]), axis=1)
    full_diamond = np.concatenate((top_half,np.flip(top_half)[1:]),axis=0)
    return np.array(full_diamond)

def main():
    print(diamond(1))
    print(diamond(2))
    print(diamond(3))
    print(diamond(4))
    print(diamond(10))

if __name__ == "__main__":
    main()

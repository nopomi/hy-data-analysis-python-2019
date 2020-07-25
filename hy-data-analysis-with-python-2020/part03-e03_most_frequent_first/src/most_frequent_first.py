#!/usr/bin/env python3

import numpy as np

def most_frequent_first(a, c):
    unique, counts = np.unique(a[:,c], return_counts=True)
    ordered = unique[counts.argsort()][::-1]
    A = np.concatenate([a[a[:,c] == i] for i in ordered])
    return A

def main():
    a = np.array([[5,0,3,3,7,9,3,5,2,4]
    ,[7,6,8,8,1,6,7,7,8,1]
    ,[5,9,8,9,4,3,0,3,5,0]
    ,[2,3,8,1,3,3,3,7,0,1]
    ,[9,9,0,4,7,3,2,7,2,0]
    ,[0,4,5,5,6,8,4,1,4,9]
    ,[8,1,1,7,9,9,3,6,7,2]
    ,[0,3,5,9,4,4,6,4,4,3]
    ,[4,4,8,4,3,7,5,5,0,1]
    ,[5,9,3,0,5,0,1,2,4,2]])
    print(a[:,-1])
    print(most_frequent_first(a,-1))

if __name__ == "__main__":
    main()

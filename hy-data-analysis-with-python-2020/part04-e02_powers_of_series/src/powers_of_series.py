#!/usr/bin/env python3

import pandas as pd

def powers_of_series(s, k):
    df = pd.DataFrame()
    for i in range(1, k+1):
        df[i] = s**i
    return df

def main():
    s = pd.Series([1,2,3,4,5], index=list("abcde"))
    print(powers_of_series(s, 3))

if __name__ == "__main__":
    main()

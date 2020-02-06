#!/usr/bin/env python3

import pandas as pd

def inverse_series(s):
    return pd.Series(s.index, index=s.values)

def main():
    s1 = pd.Series([1,2,3,3], index=list("abcd"))
    s_inv =inverse_series(s1)
    print(s_inv)
    print(s_inv[3])

if __name__ == "__main__":
    main()

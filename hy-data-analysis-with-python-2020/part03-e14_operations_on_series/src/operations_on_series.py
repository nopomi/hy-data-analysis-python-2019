#!/usr/bin/env python3

import pandas as pd

def create_series(L1, L2):
    s1 = pd.Series(L1, index=list("abc"))
    s2 = pd.Series(L2, index=list("abc"))
    return (s1, s2)

def modify_series(s1, s2):
    s1["d"] = s2["b"]
    s2 = s2.drop("b")
    return (s1, s2)

def main():
    L1 = list("123")
    L2 = list("456")
    s1, s2 = create_series(L1, L2)
    s1_mod, s2_mod = modify_series(s1, s2)
    print(s1_mod + s2_mod)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import pandas as pd
import numpy as np

def last_week():
    current = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    lw = current.copy()
    lw["LW"] = lw["LW"].replace(["Re", "New"], np.nan)
    lw = lw.astype({'LW': 'float'})
    lw["Peak Pos"].where(lambda x: (lw["Peak Pos"] != lw["Pos"]) | (lw["Peak Pos"] == lw["LW"]), np.nan, inplace=True)
    lw.drop(lw[lw["LW"].isna()].index, inplace=True)
    lw["Pos"] = lw["LW"]
    lw = lw.astype({'Pos':'int64'})
    missing = pd.DataFrame([i for i in range(1,41) if i not in lw["Pos"].values], columns=["Pos"])
    lw = lw.append(missing, sort=False)
    lw["WoC"] = lw["WoC"]-1
    lw["LW"] = np.nan
    lw.sort_values(by = 'Pos', inplace=True)
    lw.reset_index(inplace=True, drop=True)
    return lw

def main():
    df = last_week()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:", df.dtypes)
    print(df)


if __name__ == "__main__":
    main()

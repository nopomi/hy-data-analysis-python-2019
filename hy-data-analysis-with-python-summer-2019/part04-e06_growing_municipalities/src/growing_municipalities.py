#!/usr/bin/env python3

import pandas as pd

def growing_municipalities(df):
    growers = df[df["Population change from the previous year, %"]>0]
    ratio = growers.shape[0] / df.shape[0]
    return ratio

def main():
    df = pd.read_csv("src/municipal.tsv", sep="\t")
    ratio = growing_municipalities(df[:100])
    print("Proportion of growing municipalities: {:.1f}%".format(ratio*100))

if __name__ == "__main__":
    main()

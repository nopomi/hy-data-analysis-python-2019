#!/usr/bin/env python3

import pandas as pd

def main():
    df = pd.read_csv("src/municipal.tsv", sep="\t")
    rows, columns = df.shape
    print(f"Shape: {rows},{columns}")
    print("Columns:")
    for i in df.columns:
        print(i)


if __name__ == "__main__":
    main()

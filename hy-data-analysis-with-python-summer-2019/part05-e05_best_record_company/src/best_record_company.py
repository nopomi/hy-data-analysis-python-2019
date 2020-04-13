#!/usr/bin/env python3

import pandas as pd

def best_record_company():
    df = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep="\t")
    best_of = df.groupby("Publisher").sum()['WoC'].idxmax()
    return df[df['Publisher'] == best_of]

def main():
    df = best_record_company()
    print(df)

if __name__ == "__main__":
    main()

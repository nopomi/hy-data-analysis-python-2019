#!/usr/bin/env python3

import pandas as pd

def top_bands():
    bands = pd.read_csv('src/bands.tsv', sep='\t')
    top_list = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t')
    bands['Band'] = bands['Band'].str.upper()
    df = pd.merge(bands, top_list, left_on='Band', right_on='Artist')
    return df

def main():
    df = top_bands()
    print(df.shape)
    print(df.keys())
    print(df.head())

if __name__ == "__main__":
    main()

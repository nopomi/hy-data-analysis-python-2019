#!/usr/bin/env python3

import pandas as pd

def suicide_fractions():
    fractions = pd.read_csv('src/who_suicide_statistics.csv')
    #fractions = df.groupby('country').apply(lambda df.mean() : df['suicides_no']/df['population'])
    fractions['fraction'] = fractions['suicides_no'] / fractions['population']
    fractions = fractions.groupby('country').mean()
    return fractions['fraction']

def main():
    df = suicide_fractions()
    print(df.shape)
    print(df.keys())
    print(df.head())

if __name__ == "__main__":
    main()

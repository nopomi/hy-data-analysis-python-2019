#!/usr/bin/env python3

import pandas as pd
import numpy as np

def clean_name(s):
    if ', ' in s:
        last, first = s.split(", ")
        return f"{first.capitalize()} {last.capitalize()}"
    return s.title()

def cleaning_data():
    df = pd.read_csv("src/presidents.tsv", sep="\t")
    df['Start'] = df['Start'].str.extract('(\d+)', expand=False)
    df['Seasons'].replace(["one", "two"], [1, 2], inplace=True)
    df['Last'].replace("-", np.nan, inplace=True)
    df['President'] = df['President'].apply(clean_name)
    df['Vice-president'] = df['Vice-president'].apply(clean_name)
    df = df.astype({'President':'object', 'Start':'int', 'Last':'float', 'Seasons':'int', 'Vice-president':'object'})
    return df

def main():
    print(cleaning_data())

if __name__ == "__main__":
    main()

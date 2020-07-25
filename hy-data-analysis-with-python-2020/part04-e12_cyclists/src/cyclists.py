#!/usr/bin/env python3

import pandas as pd

def cyclists():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    print(df.shape)
    df = df.dropna(how='all')
    df = df.dropna(how='all', axis=1)
    return df


def main():
    df = cyclists()
    print(df.shape)
    print(df)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import pandas as pd

def last_week():
    return pd.DataFrame()

def main():
    df = last_week()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:", df.dtypes)
    print(df)


if __name__ == "__main__":
    main()

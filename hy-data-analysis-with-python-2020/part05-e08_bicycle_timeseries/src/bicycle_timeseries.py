#!/usr/bin/env python3

import pandas as pd

def bicycle_timeseries():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df2 = df["Päivämäärä"].str.split(expand=True)
    df2.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
    hourmin = df2["Hour"].str.split(":", expand=True)
    df2["Hour"] = hourmin.iloc[:, 0]
    df = pd.merge(df, df2, left_index=True, right_index=True)
    df = df.dropna(how='all')
    df["Month"] = df["Month"].map({"tammi":1, "helmi":2, "maalis":3, "huhti":4, "touko":5, "kesä":6, "heinä":7, "elo":8, "syys":9, "loka":10, "marras":11, "joulu":12})
    df.astype({'Day':'int', 'Month':'int', 'Year':'int', 'Hour':'int'})
    df["Datetime"] = pd.to_datetime(df[["Year", "Month", "Day", "Hour"]])
    df = df.drop(columns=["Päivämäärä", "Unnamed: 21", "Year", "Month", "Day", "Hour", "Weekday"])
    df = df.set_index("Datetime")
    return df


def main():
    df = bicycle_timeseries()
    print(df.shape)
    print(df.head())
    print(df.keys())

if __name__ == "__main__":
    main()

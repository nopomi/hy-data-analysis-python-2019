#!/usr/bin/env python3

import pandas as pd

def split_date(df):
    df = df["Päivämäärä"].str.split(expand=True)
    df = df.dropna(how="all")
    df.columns=["Weekday", "Day", "Month", "Year", "Hour"]
    df["Hour"] = [i.split(":")[0] for i in df["Hour"]]
    df = df.astype({"Day":'int', "Year":'int', "Hour":'int'})
    df["Weekday"].replace(["ma", "ti", "ke", "to", "pe", "la", "su"], ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], inplace=True)
    df["Month"] = df["Month"].map({"tammi":1, "helmi":2, "maalis":3, "huhti":4, "touko":5, "kesä":6, "heinä":7, "elo":8, "syys":9, "loka":10, "marras":11, "joulu":12})
    df = df.astype({"Day":'int', "Year":'int', "Hour":'int', "Weekday":'object'})
    return df

def split_date_continues():
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
    df = df.dropna(how='all', axis=0).dropna(how='all', axis=1)
    dates = split_date(df)
    df.drop('Päivämäärä', axis=1, inplace=True)
    df = pd.concat([dates, df], axis=1)
    return df

def main():
    df = split_date_continues()
    print("Shape:", df.shape)
    print("Column names:\n", df.columns)
    print(df.head())


if __name__ == "__main__":
    main()

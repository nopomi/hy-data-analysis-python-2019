#!/usr/bin/env python3

import pandas as pd
import numpy as np


def split_date():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df = df["Päivämäärä"].str.split(expand=True)
    df = df.dropna(how="all")
    df.columns=["Weekday", "Day", "Month", "Year", "Hour"]
    df["Hour"] = [i.split(":")[0] for i in df["Hour"]]
    df = df.astype({"Day":'int32', "Year":'int32', "Hour":'int32'})
    df["Weekday"].replace(["ma", "ti", "ke", "to", "pe", "la", "su"], ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], inplace=True)
    df["Month"] = df["Month"].map({"tammi":1, "helmi":2, "maalis":3, "huhti":4, "touko":5, "kesä":6, "heinä":7, "elo":8, "syys":9, "loka":10, "marras":11, "joulu":12})
    return df

def main():
    print(split_date())

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

days = dict(zip("ma ti ke to pe la su".split(), "Mon Tue Wed Thu Fri Sat Sun".split()))
months = dict(zip("tammi helmi maalis huhti touko kesä heinä elo syys loka marras joulu".split(), range(1, 13)))

def split_date(df):
    d = df["Päivämäärä"].str.split(expand=True)
    d.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
    hourmin = d["Hour"].str.split(":", expand=True)
    d["Hour"] = hourmin.iloc[:, 0]
    d["Weekday"] = d["Weekday"].map(days)
    d["Month"] = d["Month"].map(months)
    d = d.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})
    return d


def cyclists_per_day():
    pm = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
    pm = pm.dropna(axis=0, how="all").dropna(axis=1, how="all")
    d = split_date(pm)
    pm.drop("Päivämäärä", axis=1, inplace=True)
    pm = pd.concat([d, pm], axis=1)
    pm.drop(['Hour', 'Weekday'], axis=1, inplace=True)
    grouped = pm.groupby(['Year', 'Month', 'Day']).sum()
    return grouped

def main():
    df = cyclists_per_day()
    print(df.shape)
    print(df.keys())
    print(df.head())

if __name__ == "__main__":
    main()

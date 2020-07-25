#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

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

def commute():
    df = bicycle_timeseries()
    df = df['2017-08-01':'2017-08-31']
    weekdays = df.groupby(df.index.weekday).sum()
    weekdays.index = range(1,8)
    weekdays.index.name = 'Weekdays'
    return weekdays

def main():
    df = commute()
    df.plot(kind='line')
    weekdays="mon tue wed thu fri sat sun".title().split()
    plt.gca().set_xticklabels(weekdays)
    plt.show()


if __name__ == "__main__":
    main()

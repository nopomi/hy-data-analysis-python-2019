#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn import linear_model

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

def cycling_weather_continues(station):
    pm = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
    pm = pm.dropna(axis=0, how="all").dropna(axis=1, how="all")
    kw = pd.read_csv('src/kumpula-weather-2017.csv', sep=',')
    kw = kw.dropna(axis=0, how="all").dropna(axis=1,how="all")
    pm = pm[["Päivämäärä", station]]
    d = split_date(pm)
    pm = pm.drop("Päivämäärä", axis=1)
    pm = pd.concat([d, pm], axis=1)
    pm = pm[pm["Year"] == 2017]
    pm = pm.groupby(["Day","Month","Year"], as_index=False).sum().reset_index()
    pm = pm.drop(["Hour"], axis=1)
    merged = pd.merge(kw, pm, right_on=['Year', 'Month', 'Day'], left_on=['Year', 'm', 'd'])
    merged.drop(['m', 'd', 'Time', 'Time zone'], axis=1, inplace=True)
    merged = merged.fillna(method='ffill')
    merged.to_csv('merged.csv')
    reg = linear_model.LinearRegression(fit_intercept=True)
    X = merged[['Precipitation amount (mm)', 'Snow depth (cm)', 'Air temperature (degC)']]
    y = merged[[station]]
    reg.fit(X,y)
    total_score = reg.score(X,y)

    return reg.coef_[0], total_score

def main():
    station = "Merikannontie"
    scores = cycling_weather_continues(station)
    print(f"Measuring station: {station}")
    print(f"Regression coefficient for variable 'precipitation': {scores[0][0]:.1f}")
    print(f"Regression coefficient for variable 'snow depth': {scores[0][1]:.1f}")
    print(f"Regression coefficient for variable 'temperature': {scores[0][2]:.1f}")
    print(f"Score: {scores[1]:.2f}")

if __name__ == "__main__":
    main()

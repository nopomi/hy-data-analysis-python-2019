#!/usr/bin/env python3

import pandas as pd

def average_temperature():
    wh = pd.read_csv("src/kumpula-weather-2017.csv")
    wh = wh[wh['m'] == 7]
    return wh["Air temperature (degC)"].mean()

def main():
    print("Average temperature in July: {:.1f}".format(average_temperature()))

if __name__ == "__main__":
    main()

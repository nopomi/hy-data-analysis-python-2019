#!/usr/bin/env python3

import pandas as pd

def snow_depth():
    wh = pd.read_csv("src/kumpula-weather-2017.csv")
    max = wh["Snow depth (cm)"].max()
    return max

def main():
    print("Max snow depth: " + str(snow_depth()))

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import pandas as pd
from sklearn.linear_model import LinearRegression

def mystery_data():
    df = pd.read_csv('src/mystery_data.tsv', sep='\t')
    model = LinearRegression(fit_intercept=False)
    model.fit(df.iloc[:,0:5], df.iloc[:,5])
    return model.coef_

def main():
    coefficients = mystery_data()
    for i, coef in enumerate(coefficients):
        print(f"Coefficient for X{i} is {coef}")

if __name__ == "__main__":
    main()

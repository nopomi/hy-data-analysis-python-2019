#!/usr/bin/env python3

import pandas as pd
from sklearn import linear_model


def coefficient_of_determination():
    df = pd.read_csv("src/mystery_data.tsv", sep="\t")
    X = df.loc[:, "X1":"X5"]
    y = df.Y
    reg = linear_model.LinearRegression(fit_intercept=True)
    scores = []
    reg.fit(X,y)
    scores.append(reg.score(X,y))
    for c in X.columns:
        reg.fit(X[c].values.reshape(-1,1),y)
        scores.append(reg.score(X[c].values.reshape(-1,1), y))
    return scores

def main():
    scores = coefficient_of_determination()
    for i, score in enumerate(scores):
        if i == 0:
            print(f"R2-score with feature(s) X: {score}")
        else:
            print(f"R2 score with feature(s) X{i+1}: {score}")

if __name__ == "__main__":
    main()

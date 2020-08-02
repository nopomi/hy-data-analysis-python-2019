#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def explained_variance():
    df = pd.read_csv("src/data.tsv", sep="\t")
    model = PCA()
    model.fit(df)
    return df.var(axis=0), model.explained_variance_

def main():
    v, ev = explained_variance()
    print("The variances are: ", end="")
    for i in v:
        print(f"{i:.3f}", end=" ")
    print("\n")
    print("The explained variances after PCA are: ", end="")
    for j in ev:
        print(f"{j:.3f}", end=" ")
    print("\n")
    plt.plot(np.arange(1,11), np.cumsum(ev))
    plt.show()

if __name__ == "__main__":
    main()

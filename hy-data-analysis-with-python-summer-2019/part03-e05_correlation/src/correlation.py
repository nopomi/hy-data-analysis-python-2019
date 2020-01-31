#!/usr/bin/env python3

import scipy.stats
import numpy as np


def load2():
    """This loads the data from the internet. Does not work well on the TMC server."""
    import seaborn as sns
    return sns.load_dataset('iris').drop('species', axis=1).values

def load():
    import pandas as pd
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values


def lengths():
    a = load()
    corr, conf = scipy.stats.pearsonr(a[:,0],a[:,2])
    return corr

def correlations():
    a = load()
    return np.corrcoef(a, rowvar=False)

def main():
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()

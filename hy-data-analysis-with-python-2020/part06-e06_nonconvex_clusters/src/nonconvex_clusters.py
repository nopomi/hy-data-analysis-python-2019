#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score
import scipy
import matplotlib.pyplot as plt

def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation

def nonconvex_clusters():
    df = pd.read_csv("src/data.tsv",sep="\t")
    X = df[["X1","X2"]]
    y = df["y"]
    label_count = len(y.unique())
    eps_values = np.arange(0.05,0.2,0.05)
    results = []
    for i, v in enumerate(eps_values):
        model = DBSCAN(eps=v)
        model.fit(X)
        cluster_count = len(set(model.labels_)) - (1 if -1 in model.labels_ else 0)
        outlier_count = np.count_nonzero(model.labels_ == -1)
        non_outliers = model.labels_ != -1
        permutations = find_permutation(cluster_count, y[non_outliers], model.labels_[non_outliers])
        new_labels = [permutations[label] for label in model.labels_[non_outliers]]
        if label_count != cluster_count:
            score = np.nan
        else:
            score = accuracy_score(y[non_outliers], new_labels)
        results.append([v, score, cluster_count, outlier_count])
        #plt.scatter(X["X1"], X["X2"], c=model.labels_)
        #plt.show()
    return pd.DataFrame(data=results,columns=["eps", "Score", "Clusters", "Outliers"], dtype="float")

def main():
    print(nonconvex_clusters())

if __name__ == "__main__":
    main()

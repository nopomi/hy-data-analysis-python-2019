#!/usr/bin/env python3

import pandas as pd
import numpy as np
import scipy
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import accuracy_score
from sklearn.metrics import pairwise_distances

from matplotlib import pyplot as plt

import seaborn as sns
sns.set(color_codes=True)
import scipy.spatial as sp
import scipy.cluster.hierarchy as hc

def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation

def toint(x):
    return 'ACGT'.find(x)

def get_features_and_labels(filename):
    df = pd.read_csv(filename, sep="\t")
    X = [[toint(c) for c in s] for s in df["X"]]
    return (np.array(X), np.array(df["y"]))

def plot(distances, method='average', affinity='euclidean'):
    mylinkage = hc.linkage(sp.distance.squareform(distances), method=method)
    g=sns.clustermap(distances, row_linkage=mylinkage, col_linkage=mylinkage )
    g.fig.suptitle(f"Hierarchical clustering using {method} linkage and {affinity} affinity")
    plt.show()

def cluster_euclidean(filename):
    X, y = get_features_and_labels(filename)
    model = AgglomerativeClustering(linkage="average", affinity="euclidean")
    model.fit(X)
    permutation = find_permutation(2, y, model.labels_)
    new_labels = [permutation[label] for label in model.labels_]
    score = accuracy_score(y, new_labels)
    distances=pairwise_distances(X, metric="euclidean")
    #plot(distances)
    return score

def cluster_hamming(filename):
    X, y = get_features_and_labels(filename)
    distances = pairwise_distances(X, metric="hamming")
    model = AgglomerativeClustering(affinity="precomputed", linkage="average")
    model.fit_predict(distances)
    permutation = find_permutation(2, y, model.labels_)
    new_labels = [permutation[label] for label in model.labels_]
    score = accuracy_score(y, new_labels)
    #plot(distances, method="average", affinity="hamming")
    return score


def main():
    print("Accuracy score with Euclidean affinity is", cluster_euclidean("src/data.seq"))
    print("Accuracy score with Hamming affinity is", cluster_hamming("src/data.seq"))

if __name__ == "__main__":
    main()

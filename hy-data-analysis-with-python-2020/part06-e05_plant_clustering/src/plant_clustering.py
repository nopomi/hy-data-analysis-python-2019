#!/usr/bin/env python3

import scipy
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.cluster import KMeans

def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation

def plant_clustering():
    iris = load_iris()
    model=KMeans(3, random_state=0)
    model.fit(iris.data)
    permutation = find_permutation(3, iris.target, model.labels_)
    new_labels = [permutation[label] for label in model.labels_]
    score = accuracy_score(iris.target, new_labels)
    return score

def main():
    print(plant_clustering())

if __name__ == "__main__":
    main()

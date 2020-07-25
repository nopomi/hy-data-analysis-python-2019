#!/usr/bin/env python3

import scipy


def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation

def plant_clustering():
    return 0.0

def main():
    print(plant_clustering())

if __name__ == "__main__":
    main()

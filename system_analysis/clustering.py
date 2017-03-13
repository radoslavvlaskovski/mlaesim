import numpy as np
import sklearn.cluster as cluster
from etc import plotter
from pprint import pprint

def clustering(data_points, cluster_number, graph = False):
    class_numbers = np.arange(0, cluster_number)
    clusters = list()
    for i in range(0, cluster_number):
        clusters.append(list())
    kmeans = cluster.KMeans(n_clusters=cluster_number).fit_predict(data_points)
    for i in range(0, len(kmeans)):
        for j in class_numbers:
            if kmeans[i] == j:
                clusters[j].append(data_points[i])


    for i in range(0, len(clusters)):
        clusters[i] = np.array(clusters[i])

    if graph:
        plot(clusters)

    return create_thresholds(clusters, cluster_number)

def create_thresholds(clusters, cluster_number, max_vm_number=8):
    thresholds = list()

    for cluster in clusters:
        for i in range(1, max_vm_number + 1):
            max = 0
            min = 101
            for k in cluster:
                if k[1] == i:
                    if k[0] > max:
                        max = k[0]
                    if k[0] < min :
                        min = k[0]
            thresholds.append([i, min, max])

    thresholds_combined = list()
    for i in range(1, max_vm_number + 1):
        thresholds_combined.append(list())
        for threshold in thresholds:
            if threshold[0] == i:
                thresholds_combined[i - 1].append(threshold[1])
                thresholds_combined[i - 1].append(threshold[2])
        thresholds_combined[i-1].sort()
        j = 2
        while j < len(thresholds_combined[i - 1]):
            th = (thresholds_combined[i - 1][j] + thresholds_combined[i-1][j - 1]) / 2
            thresholds_combined[i - 1][j] = th
            thresholds_combined[i - 1][j - 1] = th
            j += 2
        thresholds_combined[i - 1][0] = 0
        thresholds_combined[i - 1][len(thresholds_combined[i - 1]) - 1] = 100
        thresholds_combined[i - 1] = list(set(thresholds_combined[i - 1]))
        thresholds_combined[i-1].sort()

    return thresholds_combined

def make_decision(thresholds, vm_number, cpu_usage):

    if vm_number >= len(thresholds):
        vm_number = len(thresholds)
    relevant_thresholds = thresholds[vm_number - 1]
    if cpu_usage < relevant_thresholds[1]:
        return 0
    elif cpu_usage > relevant_thresholds[2]:
        return 2
    else:
        return 1

def plot(clusters):
    if clusters[0].shape[1] == 2:
        plotter.plot_clusters2d(clusters)
    if clusters[0].shape[1] == 3:
        plotter.plot_clusters3d(clusters)


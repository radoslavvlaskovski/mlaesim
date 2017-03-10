import numpy as np
import sklearn.cluster as cluster
from etc import plotter


def clustering(data_points, cluster_number):
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
    if clusters[0].shape[1] == 2:
        plotter.plot_clusters2d(clusters)
    if clusters[0].shape[1] == 3:
        plotter.plot_clusters3d(clusters)

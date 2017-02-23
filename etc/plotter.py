import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint
from mpl_toolkits.mplot3d import Axes3D

colors = ['b', 'r', 'g', 'k', 'm', 'c']

'''
def plot_measurements():
    req_mean = read_req_mean()
    req_mean["timestamp"] = req_mean["timestamp"] - np.ones(len(req_mean)) * 1456100000
    req_mean = np.array(req_mean)
    req_mean = np.delete(req_mean, (0), axis=1)
    cpu_mean = read_cpu_mean()
    cpu_mean["timestamp"] = cpu_mean["timestamp"] - np.ones(len(cpu_mean)) * 1456100000
    cpu_mean = np.array(cpu_mean)
    cpu_mean = np.delete(cpu_mean, (0), axis=1)

    dp = create_data_points()

    plt.xlabel("Requests")
    plt.ylabel("CPU %")
    plt.scatter(dp.T[0], dp.T[1])
    plt.show()
'''


def plot_clusters2d(clusters):
    for i in range(0, len(clusters)):
        plt.scatter(clusters[i].T[0], clusters[i].T[1], color=colors[i])
    plt.show()

def plot_clusters3d(clusters):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    for i in range(0, len(clusters)):
        ax.scatter(clusters[i].T[0], clusters[i].T[1], clusters[i].T[2], color=colors[i])
    plt.show()
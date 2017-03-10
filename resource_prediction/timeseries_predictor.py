import pandas
from pprint import *
import numpy as np
import matplotlib.pyplot as plt
import sklearn.cluster as cluster
from mpl_toolkits.mplot3d import Axes3D
import statsmodels.api as sm

def requests_predictions(data_points):

    start = "1970-01-01 01:01:00"
    end = "1970-01-01 08:01:00"
    p = 2
    d = 0
    q = 12

    print(data_points.index)
    data_points.index = pandas.to_datetime(req.index, unit="m")
    del data_points["timestamp"]
    del data_points["#key"]
    data_points["value"] = data_points["value"].astype(float)
    pprint(data_points)

    arma20 = sm.tsa.ARIMA(data_points, (p, d, q)).fit()

    plt.plot(arma20.predict(start=start, end=end, dynamic=True), color="r")
    plt.plot(data_points, color="b")
    plt.show()

    return

'''
def plot_rel_cpu_req():
    req_mean = read_req_mean()
    cpmc = cpu_mean_compressed()
    data_points = list()
    for i in range(1, len(req_mean) - 1):
        data_points.append([req_mean["value"][i], cpmc[i - 1][1] * cpmc[i - 1][2]])
    data_points = np.array(data_points)

    plt.plot(req_mean["timestamp"][2:], data_points.T[0], color="b")
    plt.plot(req_mean["timestamp"][2:], data_points.T[1], color="r")
    plt.show()
'''

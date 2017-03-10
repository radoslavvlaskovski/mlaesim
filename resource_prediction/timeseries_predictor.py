import pandas
from pprint import *
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from etc import reader

def requests_predictions():

    data_points = reader.create_regression_dp()
    start = 0
    end = 5094
    p = 2
    d = 0
    q = 12

    arma20 = sm.tsa.ARIMA(data_points.astype(float), (p, d, q)).fit()

    #plt.plot(arma20.predict(start=start, end=end, dynamic=True), color="r")
    plt.plot(data_points.T[0], data_points.T[1], color="b")
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



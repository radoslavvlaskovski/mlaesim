import pandas
from pprint import *
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from etc import reader


def requests_predictions():

    data_points = reader.create_regression_dp()
    dp = data_points.T[1]
    pprint(dp)
    start = 100
    end = 5092
    p = 4
    d = 1
    q = 3

    arma20 = sm.tsa.ARIMA(dp.astype(float), (p, d, q)).fit(transparams=True)
    predicted_values = arma20.predict(start=start, end=end, dynamic=True)
    pprint(dp)
    pprint(predicted_values)

    plt.plot(data_points.T[0][100:], predicted_values, color="r")
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



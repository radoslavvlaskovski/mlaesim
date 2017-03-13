import pandas
from pprint import *
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from etc import reader


def requests_predictions():

    data_points = reader.create_regression_dp()
    dp = data_points.T[1]
    start = 100
    end = 5092
    p = 4
    d = 0
    q = 2

    arma20 = sm.tsa.ARIMA(dp.astype(float), (p, d, q)).fit(transparams=True)
    predicted_values = arma20.predict(start=start, end=end, dynamic=True)
    pprint(predicted_values)

    plt.plot(data_points.T[0][100:], predicted_values, color="r")
    plt.plot(data_points.T[0], data_points.T[1], color="b")
    plt.title("ARIMA Prediction with (" + str(p) + ", " + str(d) + ", " + str(q) + ")" )
    plt.show()

    return



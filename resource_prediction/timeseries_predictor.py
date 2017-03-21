import pandas
from pprint import *
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from etc import reader


def requests_predictions():

    data_points = reader.create_regression_dp()
    dp = data_points.T[1]
    dp = dp.astype(float)
    threshold_for_bug = 1
    dp[dp < threshold_for_bug] = threshold_for_bug
    start = 100
    end = 5092
    p = 2
    d = 1
    q = 2
    pprint(np.log(dp))

    arma20 = sm.tsa.ARIMA(np.log(dp), order=(p, d, q)).fit()
    predicted_values = arma20.predict(start=100, end=end, dynamic=True, typ="levels")
    pprint(np.exp(predicted_values))

    plt.plot(data_points.T[0][100:], predicted_values, color="r")
    plt.plot(data_points.T[0], np.log(dp), color="b")
    plt.title("ARIMA Prediction with (" + str(p) + ", " + str(d) + ", " + str(q) + ")" )
    plt.show()

    return



from pprint import *
import numpy as np
import matplotlib.pyplot as plt
from etc import reader

def requests_predictions():

    data_points = reader.create_regression_dp()
    dp = data_points.T[1]



    #plt.plot(data_points.T[0][], predicted_values, color="r")
    plt.plot(data_points.T[0], data_points.T[1], color="b")
    plt.show()

    return
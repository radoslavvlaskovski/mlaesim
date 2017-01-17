import pandas
from pprint import *
import numpy as np
import matplotlib.pyplot as plt

def read_ase_measurements_requests():

    requests = pandas.read_csv("resources/haproxy-78877094-requests.csv", sep=";")
    requests = np.array(requests)
    requests = np.delete(requests, (0), axis=1)
    return requests

def read_ase_measurements_errors():

    errors = pandas.read_csv("resources/haproxy-78877094-errors.csv", sep=";")
    errors = np.array(errors)
    errors = np.delete(errors, (0), axis=1)
    return errors

def plot_measurements():

    requests = read_ase_measurements_requests()
    errors = read_ase_measurements_errors()
    plt.subplot(211)
    plt.plot(requests.T[0], requests.T[1])
    plt.subplot(212)
    plt.plot(errors.T[0], errors.T[1])
    plt.show()


plot_measurements()

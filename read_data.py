import pandas
from pprint import *
import numpy as np
import matplotlib.pyplot as plt

weird_name = ["elasticapp-19291764"]
filenames = ["elasticapp-33707438", "elasticapp-46926644", "elasticapp-54363890",
             "elasticapp-61489080", "elasticapp-70576956", "elasticapp-79702942", "elasticapp-87181135", "elasticapp-94268427",
             "elasticapp-23246583", "elasticapp-33971639", "elasticapp-46957027", "elasticapp-55401853", "elasticapp-64146112",
             "elasticapp-70709910", "elasticapp-81354282", "elasticapp-87584735", "elasticapp-94398520", "elasticapp-25728627",
             "elasticapp-39023379", "elasticapp-47468170", "elasticapp-55884125", "elasticapp-66210763", "elasticapp-70773241",
             "elasticapp-81916236", "elasticapp-88642565", "elasticapp-95995152", "elasticapp-29836852", "elasticapp-39365659",
             "elasticapp-51206812", "elasticapp-5615799", "elasticapp-68271271", "elasticapp-71467906", "elasticapp-84632431",
             "elasticapp-92117055", "elasticapp-97188228", "elasticapp-31921146", "elasticapp-43537261", "elasticapp-51667217",
             "elasticapp-60101113", "elasticapp-68318198", "elasticapp-7514481", "elasticapp-85866103", "elasticapp-93679808",
             "elasticapp-3201563", "elasticapp-44517722", "elasticapp-53488918", "elasticapp-60847780", "elasticapp-70469690",
             "elasticapp-7800933", "elasticapp-87031633", "elasticapp-93912691"]

def read_ase_measurements_requests():

    requests = pandas.read_csv("resources/haproxy-78877094-requests.csv", sep=";")
    #requests = np.array(requests)
    #requests = np.delete(requests, (0), axis=1)
    return requests

def read_ase_measurements_errors():

    errors = pandas.read_csv("resources/haproxy-78877094-errors.csv", sep=";")
    errors = np.array(errors)
    errors = np.delete(errors, (0), axis=1)
    return errors

def read_metrics():

    alloc_all = list()
    for file_name in filenames :
        alloc_all.append(pandas.read_csv("resources/cpu_allocation/" + file_name + ".dat", sep=" "))
    return alloc_all

def create_data_points():

    metrics = read_metrics()
    requests = read_ase_measurements_requests()
    count = 0

    for i in range(0, 600):
        timestamp = requests["timestamp"][i]
        for vm in metrics:
            for t_vm in vm["timestamp"]:
               if t_vm == timestamp:
                   count += 1
    print count

def plot_measurements():

    requests = read_ase_measurements_requests()
    errors = read_ase_measurements_errors()
    plt.subplot(211)
    plt.plot(requests.T[0], requests.T[1])
    plt.subplot(212)
    plt.plot(errors.T[0], errors.T[1])
    plt.show()

create_data_points()

import pandas
from pprint import *
import numpy as np


weird_file = ["elasticapp-19291764"]
filenames = ["elasticapp-33707438", "elasticapp-46926644", "elasticapp-54363890",
             "elasticapp-61489080", "elasticapp-70576956", "elasticapp-79702942", "elasticapp-87181135",
             "elasticapp-94268427",
             "elasticapp-23246583", "elasticapp-33971639", "elasticapp-46957027", "elasticapp-55401853",
             "elasticapp-64146112",
             "elasticapp-70709910", "elasticapp-81354282", "elasticapp-87584735", "elasticapp-94398520",
             "elasticapp-25728627",
             "elasticapp-39023379", "elasticapp-47468170", "elasticapp-55884125", "elasticapp-66210763",
             "elasticapp-70773241",
             "elasticapp-81916236", "elasticapp-88642565", "elasticapp-95995152", "elasticapp-29836852",
             "elasticapp-39365659",
             "elasticapp-51206812", "elasticapp-5615799", "elasticapp-68271271", "elasticapp-71467906",
             "elasticapp-84632431",
             "elasticapp-92117055", "elasticapp-97188228", "elasticapp-31921146", "elasticapp-43537261",
             "elasticapp-51667217",
             "elasticapp-60101113", "elasticapp-68318198", "elasticapp-7514481", "elasticapp-85866103",
             "elasticapp-93679808",
             "elasticapp-3201563", "elasticapp-44517722", "elasticapp-53488918", "elasticapp-60847780",
             "elasticapp-70469690",
             "elasticapp-7800933", "elasticapp-87031633", "elasticapp-93912691"]


def read_ase_measurements_requests():
    requests = pandas.read_csv("../resources/haproxy-78877094-requests.csv", sep=";")
    return requests


def read_ase_measurements_errors():
    errors = pandas.read_csv("../resources/haproxy-78877094-errors.csv", sep=";")
    return errors


def read_metrics():
    alloc_all = list()
    for file_name in filenames:
        alloc_all.append(pandas.read_csv("../resources/cpu_allocation/" + file_name + ".dat", sep=" "))
    return alloc_all


def create_mean_cpu():
    metrics = read_metrics()

    timestamp_max = 0
    timestamp_min = 1500000000
    for vm in metrics:
        max_t = vm["timestamp"][len(vm) - 1]
        min_t = vm["timestamp"][0]

        if max_t > timestamp_max:
            timestamp_max = max_t
        if min_t < timestamp_min:
            timestamp_min = min_t

    num_vms = list()
    for i in range(timestamp_min, timestamp_max, 6):
        count = 0
        cpu = 0
        for vm in metrics:
            vm_start = vm["timestamp"][0]
            vm_end = vm["timestamp"][len(vm) - 1]
            if vm_start <= i <= vm_end:
                count += 1
                for j in range(0, len(vm) - 1):
                    cur_t = vm["timestamp"][j]
                    if cur_t > i:
                        cpu += vm["value"][j]
                        break

        num_vms.append([i, int(cpu / count), count])

    pprint(pandas.DataFrame(num_vms).to_csv("resources/cpu_mean.csv"))


def read_cpu_mean():
    cpu_mean = pandas.read_csv("../resources/cpu_mean.csv", sep=",")
    return cpu_mean


def cpu_mean_compressed():
    cpu_mean = read_cpu_mean()
    compressed = list()
    for i in range(0, len(cpu_mean) - 11, 10):
        timestamp = cpu_mean["timestamp"][i]
        mean_load = 0
        for j in range(i, i + 9):
            mean_load += cpu_mean["value"][j]
        compressed.append([timestamp, int(mean_load / 10), cpu_mean["count"][i]])
    return np.array(compressed)


def requests_per_vm():
    requests = read_ase_measurements_requests()
    cpu_mean = read_cpu_mean()
    requests_per_vm = list()

    for j in range(0, len(requests["timestamp"])):
        timestamp = requests["timestamp"][j]
        value = requests["value"][j]
        i = 0
        while cpu_mean["timestamp"][i] < timestamp and len(cpu_mean) - 1 > i:
            i += 1
        requests_per_vm.append([timestamp, int(value / cpu_mean["count"][i])])

    pprint(pandas.DataFrame(requests_per_vm).to_csv("../resources/requests_mean.csv"))


def read_req_mean():
    req_mean = pandas.read_csv("../resources/requests_mean.csv", sep=",")
    return req_mean


def create_data_points():
    req_mean = read_req_mean()
    cpmc = cpu_mean_compressed()
    data_points = list()
    for i in range(1, len(req_mean) - 1):
        data_points.append([req_mean["value"][i], cpmc[i - 1][1]])
    return np.array(data_points)


def create_3d_data_points():
    req_mean = read_req_mean()
    cpmc = cpu_mean_compressed()
    data_points = list()
    for i in range(1, len(req_mean) - 1):
        data_points.append([req_mean["value"][i], cpmc[i - 1][1], cpmc[i - 1][2]])
    return np.array(data_points)

def create_data_points_no_requests():
    cpu_mean = read_cpu_mean()
    data_points = list()
    for i in range(1, len(cpu_mean) - 1):
        data_points.append([cpu_mean["value"], cpu_mean["count"]])
    return np.array(data_points)

def create_3d_data_points_no_requests():
    cpu_mean = read_cpu_mean()
    data_points = list()
    for i in range(1, len(cpu_mean) - 1):
        data_points.append([cpu_mean["value"][i], cpu_mean["count"][i], cpu_mean["value"][i] * cpu_mean["count"][i]])
    return np.array(data_points)


def create_regression_dp():

    data_points = read_cpu_mean()
    print(len(data_points))
    data_points["timestamp"] -= np.ones(len(data_points)) * 1456160000
    dp = np.delete(np.array(data_points), 0, axis=1)
    dp = dp.astype(int)

    for i in range(0, len(data_points)):
        dp[i][1] = dp[i][1] * dp[i][2]
    dp = np.delete(dp, 2, axis=1)
    return np.array(dp)
from etc import reader
from resource_prediction import regression
from system_analysis import clustering
from resource_prediction import timeseries_predictor

def cluster_test():

    dp = reader.create_data_points_no_requests()
    clustering.clustering(dp, 3)
    #clustering.clustering(dp, 5)


def regression_test():
    #regression.ridge()
    #regression.polynomial()
    regression.svr()
    return

def timeseries_test():

    timeseries_predictor.requests_predictions()


def run_test():
    cluster_test()
    return
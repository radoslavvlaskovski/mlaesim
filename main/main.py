from etc import reader
from resource_prediction import regression
from system_analysis import clustering
from resource_prediction import timeseries_predictor

def cluster_test():

    dp = reader.create_data_points_no_requests()
    clustering.clustering(dp, 3)
    #clustering.clustering(dp, 5)


def ridge_test():
    regression.ridge()
    regression.polynomial()
    return

def timeseries_test():

    timeseries_predictor.requests_predictions()


def run_test():
    cluster_test()
    return

def run_simulation():

    # Simulate system behaviour by calculating a requests affect on the system
    # Think of a comparison function - (70-75% is optimal CPU utilization)
    # -> For each time step compute the score of the system
    # Generate own example ?

    # Combine the whole algorithm -> classification? + regression

    # Reinforcement Learning ?

    # Train on part of the data

    # Test on the other part + use comparison

    return


run_test()
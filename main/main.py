from etc import reader
from models import clustering, regression

def algorithm_simulation():

    # Divide data in testing data and train

    # Use train data for classification

    # Predict next req number

    # Create policy


    return

def cluster_test():

    dp = reader.create_3d_data_points_no_requests()
    clustering.clustering(dp, 2)
    clustering.clustering(dp, 3)


def ridge_test():
    regression.ridge()
    regression.polynomial()
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

cluster_test()
ridge_test()
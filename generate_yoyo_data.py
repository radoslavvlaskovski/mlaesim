import numpy as np
import matplotlib.pyplot as plt

def generate_data():

    # FIX set as the sin func + norm distr
    return np.random.normal(45, 2, 600)

def plot_data():

    yoyo_data = generate_data()

    plt.plot(yoyo_data)
    plt.show()


plot_data()
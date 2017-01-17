import numpy as np
import matplotlib.pyplot as plt
from pprint import *

def generate_data():

    # FIX set as the sin func + norm distr
    f = 5
    Fs = 600
    x = np.arange(600)
    return np.sin(2 * np.pi * f * x / Fs) * 5 + np.ones(600)*45

def plot_data():

    yoyo_data = generate_data()
    pprint(yoyo_data)

    plt.plot(np.arange(600), yoyo_data)
    plt.show()


plot_data()
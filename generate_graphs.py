# Receives a list with values and creates a graph from it.

import numpy as np
import matplotlib.pyplot as plt


def arrangeList(list):
    """Sorts based on AoA and hysteresis"""
    sortlist=sorted(list)
    arr = np.array(sortlist)
    arr = arr[:,1:]
    return arr


def correct_array_for_chord(array):
    """Corrects array so the chord goes from 0 to 100"""
    corrected_array = array
    corrected_array[:, 1] = array[:, 1] * (-1) + 100
    return corrected_array


def get_graph(array, TwoDorThreeD='2D'):
    """Plots graph for transition line as a function of AoA"""
    plt.figure()
    plt.grid(visible=True)
    plt.plot(array[:, 0], array[:, 1], linestyle='solid', color='blue')
    plt.scatter(array[:, 0], array[:, 1], linestyle='solid', color='blue')

    plt.title("Transition line of a " + str(TwoDorThreeD) + " as a function of AoA")
    plt.xlabel("AoA [deg]")
    plt.ylabel("Location of transition [%x/c from LE]")

    plt.show()

import constants
import translationLayer
import transientSimulation
import matplotlib.pyplot as plt

def set_time_resolution(): #sets the time resolution for the x-axis of the graph in seconds
    tick_location = [] #list to store the x-axis tick locations on the graph
    tick_label = [] #list to store the x-axis tick labels on the graph
    num_of_seconds = (len(transientSimulation.storage) * constants.resolution) / translationLayer.nominal_angular_frequency
    int_num_of_seconds = 0
    while (int_num_of_seconds < (num_of_seconds + 1)):
        tick_location.append(int_num_of_seconds * (len(transientSimulation.storage) / num_of_seconds))
        tick_label.append(int_num_of_seconds)
        int_num_of_seconds = int_num_of_seconds + constants.time_resolution
    plt.xticks(tick_location , tick_label)

transientSimulation.calc_wave()
plt.plot(transientSimulation.storage)
set_time_resolution()
plt.show()
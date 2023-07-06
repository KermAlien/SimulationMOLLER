import translationLayer
import transientSimulation
import matplotlib.pyplot as plt

storage = transientSimulation.storage

generation_resolution = translationLayer.generation_resolution
time_resolution = translationLayer.time_resolution
nominal_angular_frequency = translationLayer.nominal_angular_frequency

def set_time_resolution(): #sets the time resolution for the x-axis of the graph in microseconds
    tick_location = [] #list to store the x-axis tick locations on the graph
    tick_label = [] #list to store the x-axis tick labels on the graph
    num_of_microseconds = ((len(storage) * generation_resolution) / nominal_angular_frequency)
    int_num_of_microseconds = 0
    while (int_num_of_microseconds < (num_of_microseconds + 1)):
        tick_location.append(int_num_of_microseconds * (len(storage) / num_of_microseconds))
        tick_label.append(int_num_of_microseconds)
        int_num_of_microseconds = int_num_of_microseconds + time_resolution
    plt.xticks(tick_location , tick_label)

transientSimulation.calc_wave()
plt.plot(storage)
set_time_resolution()
plt.show()
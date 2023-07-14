import translationLayer
import transientSimulation
import matplotlib.pyplot as plt

storage = transientSimulation.storage

nominal_angular_frequency_positive = translationLayer.nominal_angular_frequency_positive
nominal_angular_frequency_negative = translationLayer.nominal_angular_frequency_negative
switching_period = translationLayer.switching_period
transient_rise_time_positive = translationLayer.transient_rise_time_positive
transient_rise_time_negative = translationLayer.transient_rise_time_negative
num_of_modules = translationLayer.num_of_modules
generation_resolution = translationLayer.generation_resolution
graph_time_interval = translationLayer.graph_time_interval
lower_bound_limit_radians = translationLayer.lower_bound_limit_radians
upper_bound_limit_radians = translationLayer.upper_bound_limit_radians
num_of_seconds = translationLayer.num_of_seconds
lower_bound_limit = translationLayer.lower_bound_limit
lower_bound_limit_radians = translationLayer.lower_bound_limit_radians
upper_bound_limit = translationLayer.upper_bound_limit
upper_bound_limit_radians = translationLayer.upper_bound_limit_radians

def set_time_resolution(interval): #sets the time resolution for the x-axis of the graph in seconds, parameters array in format list, resolution in radians, angular_frequency in radians / second, and interval in seconds
    tick_location = [] #list to store the tick locations on the graph
    tick_label = [] #list to store the tick labels on the graph
    int_num_of_seconds = 0
    while (int_num_of_seconds < upper_bound_limit):
        tick_location.append(int_num_of_seconds * (len(storage) / (upper_bound_limit - lower_bound_limit)))
        num_of_decimal_places = 5 #sets the number of decimal places in graph labels
        rounded_label = round(int_num_of_seconds + lower_bound_limit , num_of_decimal_places)
        tick_label.append(rounded_label)
        int_num_of_seconds = int_num_of_seconds + interval
    plt.xticks(tick_location , tick_label)

def read_current_amplitude(radian_location): #returns the current amplitude of the wave at a given radian location, parameter radian_location in radians
    current_amplitude = storage[radian_location / generation_resolution]
    return current_amplitude

transientSimulation.calc_wave(lower_bound_limit_radians , upper_bound_limit_radians)
plt.plot(storage)
set_time_resolution(graph_time_interval)
plt.show()

#not sure if set_time_resolution() is setting an accurate time scale
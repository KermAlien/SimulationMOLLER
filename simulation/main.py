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

def set_time_resolution(interval): #sets the time resolution for the x-axis of the graph in seconds, parameters array in format list, resolution in radians, angular_frequency in radians / second, and interval in seconds
    tick_location = [] #list to store the tick locations on the graph
    tick_label = [] #list to store the tick labels on the graph
    num_of_modules_positive = round(num_of_modules / 2)
    num_of_modules_negative = int(num_of_modules / 2)
    num_of_seconds_positive = (num_of_modules_positive * switching_period) + (num_of_modules_negative * transient_rise_time_positive)
    num_of_seconds_negative = (num_of_modules_negative * switching_period) + ((num_of_modules_positive - 1) * transient_rise_time_negative)
    num_of_seconds = num_of_seconds_positive + num_of_seconds_negative
    int_num_of_seconds = 0
    while (int_num_of_seconds < (num_of_seconds + interval)):
        tick_location.append(int_num_of_seconds * (len(storage) / num_of_seconds))
        num_of_decimal_places = 4
        rounded_label = round(int_num_of_seconds , num_of_decimal_places)
        tick_label.append(rounded_label)
        int_num_of_seconds = int_num_of_seconds + interval
    plt.xticks(tick_location , tick_label)

def read_current_amplitude(radian_location): #returns the current amplitude of the wave at a given radian location, parameter radian_location in radians
    current_amplitude = storage[radian_location / generation_resolution]
    return current_amplitude

transientSimulation.calc_wave()
plt.plot(storage)
set_time_resolution(graph_time_interval)
plt.show()

#not sure if set_time_resolution() is setting an accurate time scale
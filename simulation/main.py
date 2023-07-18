import translationLayer
import transientSimulation
import samplingSimulation
import matplotlib.pyplot as plt

transientSimulation.calc_wave()
# samplingSimulation.calc_wave_BCM()

storage = transientSimulation.storage

# BCM_storage = samplingSimulation.BCM_storage

# nominal_angular_frequency_positive = translationLayer.nominal_angular_frequency_positive
# nominal_angular_frequency_negative = translationLayer.nominal_angular_frequency_negative
# switching_period = translationLayer.switching_period
# num_of_modules = translationLayer.num_of_modules
# graph_time_interval = translationLayer.graph_time_interval

# def set_time_resolution(interval): #sets the time resolution for the x-axis of the graph in seconds, parameters array in format list, resolution in radians, angular_frequency in radians / second, and interval in seconds
#     tick_location = [] #list to store the tick locations on the graph
#     tick_label = [] #list to store the tick labels on the graph
#     num_of_modules_positive = round(num_of_modules / 2)
#     num_of_modules_negative = int(num_of_modules / 2)
#     num_of_seconds_positive = (num_of_modules_positive * switching_period) + (num_of_modules_negative * transient_rise_time_positive)
#     num_of_seconds_negative = (num_of_modules_negative * switching_period) + ((num_of_modules_positive - 1) * transient_rise_time_negative)
#     num_of_seconds = num_of_seconds_positive + num_of_seconds_negative
#     int_num_of_seconds = 0
#     while (int_num_of_seconds < (num_of_seconds + interval)):
#         tick_location.append(int_num_of_seconds * (len(storage) / num_of_seconds))
#         num_of_decimal_places = 4
#         rounded_label = round(int_num_of_seconds , num_of_decimal_places)
#         tick_label.append(rounded_label)
#         int_num_of_seconds = int_num_of_seconds + interval
#     plt.xticks(tick_location , tick_label)

# def read_current_amplitude(radian_location): #returns the current amplitude of the wave at a given radian location, parameter radian_location in radians
#     current_amplitude = storage[radian_location / generation_resolution]
#     return current_amplitude

# tick_location_detector = [] #list to store the x-axis tick locations on the graph
# tick_label_detector = [] #list to store the x-axis tick labels on the graph
# num_of_microseconds_detector = ((len(detector_storage) * interval_d) / nominal_angular_frequency)
# int_num_of_microseconds_detector = 0
# while (int_num_of_microseconds_detector < (num_of_microseconds_detector + 1)):
#     tick_location_detector.append(int_num_of_microseconds_detector * (len(detector_storage) / num_of_microseconds_detector))
#     tick_label_detector.append(int_num_of_microseconds_detector)
#     int_num_of_microseconds_detector = int_num_of_microseconds_detector + time_resolution

# tick_location_BCM = [] #list to store the x-axis tick locations on the graph
# tick_label_BCM = [] #list to store the x-axis tick labels on the graph
# num_of_microseconds_BCM = ((len(BCM_storage) * interval_b) / nominal_angular_frequency)
# int_num_of_microseconds_BCM = 0
# while (int_num_of_microseconds_BCM < (num_of_microseconds_BCM + 1)):
#     tick_location_BCM.append(int_num_of_microseconds_BCM * (len(BCM_storage) / num_of_microseconds_BCM))
#     tick_label_BCM.append(int_num_of_microseconds_BCM)
#     int_num_of_microseconds_BCM = int_num_of_microseconds_BCM + time_resolution

# fig, axs = plt.subplots(2)

# fig.tight_layout()

# axs[0].set_xticks(tick_location_detector)
# axs[0].set_xticklabels(tick_label_detector)
# axs[0].plot(detector_storage)
# axs[0].set_title('Detector')

# axs[1].set_xticks(tick_location_BCM)
# axs[1].set_xticklabels(tick_label_BCM)
# axs[1].plot(BCM_storage)
# axs[1].set_title('BCM')

# plt.show()





plt.plot(storage)
# set_time_resolution(graph_time_interval)
plt.show()

#not sure if set_time_resolution() is setting an accurate time scale
import constants
import translationLayer
import transientSimulation
import samplingSimulation
import matplotlib.pyplot as plt

transientSimulation.calc_wave()
# samplingSimulation.calc_wave_detector()
# samplingSimulation.calc_wave_BCM()

# BCM_storage = samplingSimulation.BCM_storage
# detector_storage = samplingSimulation.detector_storage
# interval_d = samplingSimulation.interval_d
# interval_b = samplingSimulation.interval_b

storage = transientSimulation.storage

time_resolution = translationLayer.time_resolution
nominal_angular_frequency = translationLayer.nominal_angular_frequency


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



# tick_location = [] #list to store the x-axis tick locations on the graph
# tick_label = [] #list to store the x-axis tick labels on the graph
# num_of_microseconds = ((len(storage) * generation_resolution) / nominal_angular_frequency)
# int_num_of_microseconds = 0
# while (int_num_of_microseconds < (num_of_microseconds + generation_resolution)):
#     tick_location.append(int_num_of_microseconds * (len(storage) / num_of_microseconds))
#     tick_label.append(int_num_of_microseconds)
#     int_num_of_microseconds = int_num_of_microseconds + time_resolution
# plt.xticks(tick_location , tick_label)

plt.plot(storage)
plt.show()
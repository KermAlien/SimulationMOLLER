import translationLayer
import transientSimulation
import samplingSimulation
import matplotlib.pyplot as plt

samplingSimulation.calc_wave_BCM()

storage = transientSimulation.storage
BCM_storage = samplingSimulation.BCM_storage

graph_time_interval = translationLayer.graph_time_interval
generation_resolution = translationLayer.generation_resolution
BCM_resolution = samplingSimulation.BCM_resolution
BCM_resolution = 1 / BCM_resolution

tick_location_detector = [] #list to store the x-axis tick locations on the graph
tick_label_detector = [] #list to store the x-axis tick labels on the graph
num_of_microseconds_detector = (len(storage) * generation_resolution)
int_num_of_microseconds_detector = 0
while (int_num_of_microseconds_detector < (num_of_microseconds_detector + 1)):
    tick_location_detector.append(int_num_of_microseconds_detector * (len(storage) / num_of_microseconds_detector))
    tick_label_detector.append(round(int_num_of_microseconds_detector , 4))
    int_num_of_microseconds_detector = int_num_of_microseconds_detector + graph_time_interval

tick_location_BCM = [] #list to store the x-axis tick locations on the graph
tick_label_BCM = [] #list to store the x-axis tick labels on the graph
num_of_microseconds_BCM = (len(BCM_storage) * BCM_resolution)
int_num_of_microseconds_BCM = 0
while (int_num_of_microseconds_BCM < (num_of_microseconds_BCM + 1)):
    tick_location_BCM.append(int_num_of_microseconds_BCM * (len(BCM_storage) / num_of_microseconds_BCM))
    tick_label_BCM.append(round(int_num_of_microseconds_BCM , 4))
    int_num_of_microseconds_BCM = int_num_of_microseconds_BCM + graph_time_interval

fig, axs = plt.subplots(2)

fig.tight_layout()

axs[0].set_xticks(tick_location_detector)
axs[0].set_xticklabels(tick_label_detector)
axs[0].plot(storage)
axs[0].set_title('Detector')

axs[1].set_xticks(tick_location_BCM)
axs[1].set_xticklabels(tick_label_BCM)
axs[1].plot(BCM_storage)
axs[1].set_title('BCM')

plt.show()
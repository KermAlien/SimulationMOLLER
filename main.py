import translationLayer
import transientSimulationDetector
import transientSimulationBCM
import matplotlib.pyplot as plt

transientSimulationDetector.calc_wave()
transientSimulationBCM.calc_wave()

storageDetector = transientSimulationDetector.storage
detector_resolution = translationLayer.detector_resolution

storageBCM = transientSimulationBCM.storage
BCM_resolution = translationLayer.BCM_resolution

time_resolution = translationLayer.time_resolution
nominal_angular_frequency = translationLayer.nominal_angular_frequency


tick_location_detector = [] #list to store the x-axis tick locations on the graph
tick_label_detector = [] #list to store the x-axis tick labels on the graph
num_of_microseconds_detector = ((len(storageDetector) * detector_resolution) / nominal_angular_frequency)
int_num_of_microseconds_detector = 0
while (int_num_of_microseconds_detector < (num_of_microseconds_detector + 1)):
    tick_location_detector.append(int_num_of_microseconds_detector * (len(storageDetector) / num_of_microseconds_detector))
    tick_label_detector.append(int_num_of_microseconds_detector)
    int_num_of_microseconds_detector = int_num_of_microseconds_detector + time_resolution

tick_location_BCM = [] #list to store the x-axis tick locations on the graph
tick_label_BCM = [] #list to store the x-axis tick labels on the graph
num_of_microseconds_BCM = ((len(storageBCM) * BCM_resolution) / nominal_angular_frequency)
int_num_of_microseconds_BCM = 0
while (int_num_of_microseconds_BCM < (num_of_microseconds_BCM + 1)):
    tick_location_BCM.append(int_num_of_microseconds_BCM * (len(storageBCM) / num_of_microseconds_BCM))
    tick_label_BCM.append(int_num_of_microseconds_BCM)
    int_num_of_microseconds_BCM = int_num_of_microseconds_BCM + time_resolution

fig, axs = plt.subplots(2)

fig.tight_layout()

axs[0].set_xticks(tick_location_detector)
axs[0].set_xticklabels(tick_label_detector)
axs[0].plot(storageDetector)
axs[0].set_title('Detector')

axs[1].set_xticks(tick_location_BCM)
axs[1].set_xticklabels(tick_label_BCM)
axs[1].plot(storageBCM)
axs[1].set_title('BCM')

plt.show()
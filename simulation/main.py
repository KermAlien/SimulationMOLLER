import translationLayer
import triggerPulse
import transientSimulation
import BCMSimulation
import detectorSimulation
import matplotlib.pyplot as plt

trigger = triggerPulse.trigger
storage = transientSimulation.storage
bcm = BCMSimulation.bcm
detector = detectorSimulation.detector

generation_resolution = translationLayer.generation_resolution
graph_time_interval = translationLayer.graph_time_interval
lower_bound_limit = translationLayer.lower_bound_limit
upper_bound_limit = translationLayer.upper_bound_limit
lower_bound_limit_radian = translationLayer.lower_bound_limit_radian
upper_bound_limit_radian = translationLayer.upper_bound_limit_radian

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

triggerPulse.calc_trigger()
transientSimulation.calc_wave(lower_bound_limit_radian , upper_bound_limit_radian)
BCMSimulation.calc_bcm()
detectorSimulation.calc_detector()

fig, axs = plt.subplots(4)
fig.tight_layout()
axs[0].set_title('Trigger Pulse')
axs[0].plot(trigger)
axs[1].set_title('Light State Generation')
axs[1].plot(storage)
axs[2].set_title('Beam Current Monitor')
axs[2].plot(bcm)
axs[3].set_title('Detector')
axs[3].plot(detector)

plt.show()

#not sure if set_time_resolution() is setting an accurate time scale
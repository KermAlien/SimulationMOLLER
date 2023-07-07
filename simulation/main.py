import translationLayer
import transientSimulation
#import triggerPulse
import matplotlib.pyplot as plt

storage = transientSimulation.storage
#trigger = triggerPulse.trigger

generation_resolution = translationLayer.generation_resolution
graph_time_scale = translationLayer.graph_time_scale
nominal_angular_frequency = translationLayer.nominal_angular_frequency

def set_time_resolution(): #sets the time resolution for the x-axis of the graph in seconds
    tick_location = [] #list to store the x-axis tick locations on the graph
    tick_label = [] #list to store the x-axis tick labels on the graph
    num_of_seconds = (len(storage) * generation_resolution) / nominal_angular_frequency
    int_num_of_seconds = 0
    while (int_num_of_seconds < (num_of_seconds + 1)):
        tick_location.append(int_num_of_seconds * (len(storage) / num_of_seconds))
        tick_label.append(int_num_of_seconds)
        int_num_of_seconds = int_num_of_seconds + graph_time_scale
    plt.xticks(tick_location , tick_label)

transientSimulation.calc_wave()
plt.plot(storage)
#triggerPulse.calc_trigger_module()
#plt.plot(trigger)
#set_time_resolution()
plt.show()

#temp = []
#time= 0
#while (time < 1):
#    temp.append(transientSimulation.calc_transient_decay(time))
#    time = time + 0.001
#plt.plot(temp)
#plt.show()
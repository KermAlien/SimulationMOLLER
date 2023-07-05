import constants
import translationLayer
import transientSimulation
import matplotlib.pyplot as plt

transientSimulation.calc_wave()

plt.plot(transientSimulation.storage)

tick_location = []
tick_label = []

num_of_seconds = (len(transientSimulation.storage) * constants.resolution) / translationLayer.nominal_angular_frequency
int_num_of_seconds = 0
while (int_num_of_seconds < (num_of_seconds + 1)):
    tick_location.append(int_num_of_seconds * (len(transientSimulation.storage) / num_of_seconds))
    tick_label.append(int_num_of_seconds)
    int_num_of_seconds = int_num_of_seconds + 1

plt.xticks(tick_location , tick_label)
plt.show()
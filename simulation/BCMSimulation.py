import translationLayer
import transientSimulation

bcm_sampling_rate = translationLayer.bcm_sampling_rate
num_of_seconds_bounded = translationLayer.num_of_seconds_bounded
num_of_radians_bounded = translationLayer.num_of_radians_bounded

bcm = [] #list used for BCMSimulation generation

def calc_bcm():
    num_of_calcs = num_of_seconds_bounded * bcm_sampling_rate
    bcm_resolution = num_of_radians_bounded / num_of_calcs
    time = 0
    while(time < num_of_radians_bounded - (0.12 * num_of_radians_bounded)):
        bcm.append(transientSimulation.read_current_amplitude(time))
        time = time + bcm_resolution
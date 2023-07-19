import translationLayer
import transientSimulation

bcm_sampling_rate = translationLayer.bcm_sampling_rate
num_of_seconds_bounded = translationLayer.num_of_seconds_bounded
num_of_radians_bounded = translationLayer.num_of_radians_bounded

bcm = [] #list used for BCMSimulation generation

def calc_bcm():
    num_of_calcs = num_of_seconds_bounded * bcm_sampling_rate #number of beam current monitor measurements over bounded interval
    bcm_resolution = num_of_radians_bounded / num_of_calcs #beam current monitor resolution in radians
    time = 0
    while(time < (0.88 * num_of_radians_bounded)):
        bcm.append(transientSimulation.read_current_amplitude(time))
        time = time + bcm_resolution
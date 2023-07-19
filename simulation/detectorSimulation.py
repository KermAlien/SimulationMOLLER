import translationLayer
import transientSimulation

detector_sampling_rate = translationLayer.detector_sampling_rate
num_of_seconds_bounded = translationLayer.num_of_seconds_bounded
num_of_radians_bounded = translationLayer.num_of_radians_bounded

detector = [] #list used for detectorSimulation generation

def calc_detector():
    num_of_calcs = num_of_seconds_bounded * detector_sampling_rate #number of detector measurements over bounded interval
    detector_resolution = num_of_radians_bounded / num_of_calcs #detector resolution in radians
    time = 0
    while(time < (0.88 * num_of_radians_bounded)):
        detector.append(transientSimulation.read_current_amplitude(time))
        time = time + detector_resolution
import translationLayer
import transientSimulation

switching_angular_frequency = translationLayer.switching_angular_frequency
generation_resolution = translationLayer.generation_resolution
BCM_resolution = translationLayer.BCM_resolution

transientSimulation.calc_wave()

storage = transientSimulation.storage

BCM_storage = [] #list used for BCM graph generation

seconds_in_wave = len(storage) * generation_resolution

num_of_measurements_BCM = BCM_resolution * seconds_in_wave #number of measurements that the BCM takes of the original wave

def read_current_amplitude(time): #returns the current amplitude of the wave at a given time, parameter time in seconds
    current_amplitude = storage[int(time / generation_resolution)]
    return current_amplitude

def calc_wave_BCM():
    time1 = 0
    time2 = 0
    while (time1 < num_of_measurements_BCM):
        BCM_storage.append(read_current_amplitude(time2))
        time2 = time2 + (1 / BCM_resolution)
        time1 = time1 + 1
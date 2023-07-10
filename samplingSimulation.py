import translationLayer
import transientSimulation

detector_period = translationLayer.detector_period
BCM_period = translationLayer.BCM_period
transient_rise_time = translationLayer.transient_rise_time
num_of_modules = translationLayer.num_of_modules

storage = transientSimulation.storage
generation_resolution = transientSimulation.generation_resolution

BCM_storage = [] #list used for BCM graph generation
detector_storage = [] #list used for detector graph generation

rads_in_wave = len(storage) * generation_resolution #total number of radians in the original wave

wave_period = translationLayer.switching_period + (transient_rise_time * num_of_modules) - 1 #period of the original wave

num_of_measurements_d = wave_period / detector_period #number of measurements that the detector takes of the original wave
num_of_measurements_b = wave_period / BCM_period #number of measurements that the BCM takes of the original wave

interval_d = rads_in_wave / num_of_measurements_d #interval that the detector uses to take measurements of the original wave
interval_b = rads_in_wave / num_of_measurements_b #interval that the BCM uses to take measurements of the original wave

time = 0
location = 0
while (time < num_of_measurements_d):

    time = time + interval_d
    location = location + interval_d

time = 0
location = 0
while (time < num_of_measurements_b):

    time = time + interval_b
    location = location + interval_b
import translationLayer
import transientSimulation

BCM_storage = []
detector_storage = []

storage = transientSimulation.storage
generation_resolution = transientSimulation.generation_resolution

detector_period = translationLayer.detector_period
BCM_period = translationLayer.BCM_period

transient_rise_time = translationLayer.transient_rise_time
num_of_modules = translationLayer.num_of_modules

rads_in_wave = len(storage) * generation_resolution

wave_period = translationLayer.switching_period + (transient_rise_time * num_of_modules) - 1

num_of_measurements_d = wave_period / detector_period
num_of_measurements_b = wave_period / BCM_period

interval_d = rads_in_wave / num_of_measurements_d
interval_b = rads_in_wave / num_of_measurements_b

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
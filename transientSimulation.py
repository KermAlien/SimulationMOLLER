import math
from math import sin
from math import pi
import matplotlib.pyplot as plt
import constants

import time

slope_multiplier = 0.005 #arbitrary multiple to set the agression of the slope of the linear decay function
increment_resolution = 0.1 #resolution with which the wave module is generated, measured in radians
transient_wave_voltage = 100 #transient voltage of the wave
nominal_wave_voltage = 20 #nominal voltage of the wave
nominal_wave_voltage_ripple = 1 #voltage ripple in the wave at nominal voltage
wave_frequency = 10 #wave frequency
switching_frequency = 2 #switching frequency
num_of_wave_modules = 10 #number of wave segments

storage = [] #list used for graph generation
wave_period = wave_frequency / (2 * pi) #calculate the period of the wave in radians
switching_period = switching_frequency / (2 * pi) #calculate the period of the switching in radians

def calc_decay_amplitude(time): #calculate the amplitude of the wave according to a decay funtion at a given time measured in radians
    decay_amplitude = -time/slope_multiplier + transient_wave_voltage #decay function, -x/slope_multiplier + transient_wave_voltage
    nominal_ripple = nominal_wave_voltage_ripple
    if (decay_amplitude >= nominal_ripple):
        return decay_amplitude
    else:
        return nominal_ripple

def calc_wave_amplitude(amplitude , time): #calculate the amplitude of the wave at a given time measured in radians
    current_amplitude = amplitude * math.sin(wave_frequency * time)
    return current_amplitude

def calc_wave_module(offset): #iterate calculating the current wave amplitude between switching occurances with a given resolution according to increment_resolution
    time = 0
    num_of_phases = 0
    while(num_of_phases < (wave_period / switching_period)):
        static_time = time
        decay_amplitude = calc_decay_amplitude(time + (wave_period / 4))
        while (time < (static_time + wave_period)):
            storage.append(calc_wave_amplitude(decay_amplitude , time) + offset)
            time = time + increment_resolution
            #time.sleep(0.1)
        num_of_phases = num_of_phases + 1

def calc_wave(): #iterate calculating wave modules according to num_of_wave_segments
    int_nominal_wave_voltage = nominal_wave_voltage
    num_of_segments = 0
    while(num_of_segments < num_of_wave_modules):
        calc_wave_module(int_nominal_wave_voltage)
        int_nominal_wave_voltage = -int_nominal_wave_voltage
        num_of_segments = num_of_segments + 1

calc_wave()

plt.plot(storage)
plt.show()
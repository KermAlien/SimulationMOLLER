import math
from math import cos
from math import pi
import matplotlib.pyplot as plt
import constants
import translationLayer

nominal_voltage = 5 #nominal voltage of the wave
transient_voltage = 10 #transient voltage of the wave
voltage_ripple = 0.5 #voltage ripple in the wave at nominal voltage
nominal_frequency = 3 #wave frequency
transient_frequency = 1 #transient frequency
switching_frequency = 2 #switching frequency
aggression = 0.7 #arbitrary value to set the agression of the transient decay, zero equals no decay and one equals immediate decay

num_of_phases = 3 #number of phases per wave module
num_of_wave_modules = 3 #number of wave modules
increment_resolution = 0.01 #resolution with which the wave module is generated, measured in radians

storage = [] #list used for graph generation

nominal_angular_frequency = nominal_frequency * (2 * pi) #calculate the period of the wave in radians
transient_angular_frequency = transient_frequency * (2 * pi) #calculate the period of the transient in radians
switching_angular_frequency = switching_frequency * (2 * pi) #calculate the period of the switching in radians

nominal_period = 1 / nominal_frequency
transient_period = 1 / transient_frequency
switching_period = 1 / switching_frequency

def calc_transient_decay(time): #calculate the decay of the transient according to a decay function
    decay_amplitude = transient_voltage * pow((1 - aggression) , time) #decay funtion, transient_voltage * (1-aggression)^x
    if (decay_amplitude > voltage_ripple):
        return decay_amplitude
    else: 
        return voltage_ripple

def calc_wave_amplitude(amplitude , frequency , time): #calculate the amplitude of the wave at a given time measured in radians
    current_amplitude = amplitude * math.cos(frequency * time)
    return current_amplitude

def calc_wave_module(offset , polarity): #iterate calculating the current wave amplitude between switching occurances with a given resolution according to increment_resolution
    int_num_of_phases = 0
    while(int_num_of_phases < num_of_phases):
        time = 0
        if (int_num_of_phases == 0):
            while (time < transient_period):
                storage.append(polarity * calc_wave_amplitude(transient_voltage , transient_frequency , time) + offset)
                time = time + increment_resolution
        else:
            while (time < nominal_angular_frequency):
                storage.append(calc_wave_amplitude(calc_transient_decay(int_num_of_phases) , nominal_frequency, time) + offset)  
                time = time + increment_resolution   
        int_num_of_phases = int_num_of_phases + 1

def calc_wave(): #iterate calculating wave modules according to num_of_wave_segments
    int_nominal_wave_voltage = nominal_voltage
    polarity = 1
    int_num_of_wave_modules = 0
    while(int_num_of_wave_modules < num_of_wave_modules):
        calc_wave_module(int_nominal_wave_voltage , polarity)
        int_nominal_wave_voltage = -int_nominal_wave_voltage
        polarity = -polarity
        int_num_of_wave_modules = int_num_of_wave_modules + 1

calc_wave()

plt.plot(storage)
plt.show()
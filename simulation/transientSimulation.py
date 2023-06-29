import math
from math import cos
import constants

nominal_voltage = constants.nominal_voltage
transient_voltage = constants.transient_voltage
voltage_ripple = constants.voltage_ripple
nominal_frequency = constants.nominal_frequency
transient_frequency = constants.transient_frequency
switching_frequency = constants.switching_frequency
aggression = constants.aggression

num_of_phases = constants.num_of_phases
num_of_wave_modules = constants.num_of_wave_modules
increment_resolution = constants.increment_resolution

nominal_angular_frequency = constants.nominal_angular_frequency
transient_angular_frequency = constants.transient_angular_frequency
switching_angular_frequency = constants.switching_angular_frequency

nominal_period = constants.nominal_period
transient_period = constants.transient_period
switching_period = constants.switching_period

storage = [] #list used for graph generation

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
import math
from math import pi
import translationLayer

nominal_voltage_positive = translationLayer.nominal_voltage_positve
nominal_voltage_negative = translationLayer.nominal_voltage_negative
nominal_frequency_positive = translationLayer.nominal_frequency_positive
nominal_frequency_negative = translationLayer.nominal_frequency_negative
voltage_ripple_positive = translationLayer.voltage_ripple_positive
voltage_ripple_negative = translationLayer.voltage_ripple_negative
transient_voltage_positive = translationLayer.transient_voltage_positive
transient_voltage_negative = translationLayer.transient_voltage_negative
transient_rt_voltage_positive = translationLayer.transient_rt_voltage_positive
transient_rt_voltage_negative = translationLayer.transient_rt_voltage_negative
transient_frequency_positive = translationLayer.transient_frequency_positive
transient_frequency_negative = translationLayer.transient_frequency_negative
switching_frequency = translationLayer.switching_frequency
time_constant = translationLayer.time_constant

num_of_phases_positive = translationLayer.num_of_phases_positive
num_of_phases_negative = translationLayer.num_of_phases_negative
num_of_modules = translationLayer.num_of_modules
generation_resolution = translationLayer.generation_resolution
graph_time_interval = translationLayer.graph_time_interval

nominal_period_positive = translationLayer.nominal_period_positive
nominal_period_negative = translationLayer.nominal_period_negative
transient_period_positive = translationLayer.transient_period_positive
transient_period_negative = translationLayer.transient_period_negative
switching_period = translationLayer.switching_period

nominal_angular_frequency_positive = translationLayer.nominal_angular_frequency_positive 
nominal_angular_frequency_negative = translationLayer.nominal_angular_frequency_negative
transient_angular_frequency_positive = translationLayer.transient_angular_frequency_positive
transient_angular_frequency_negative = translationLayer.transient_angular_frequency_negative
switching_angular_frequency = translationLayer.switching_angular_frequency

timer_lower_bound = translationLayer.timer_lower_bound
timer_upper_bound = translationLayer.timer_upper_bound

storage = [] #list used for graph generation

timer = 0

def calc_wave_amplitude(amplitude , frequency , time): #calculate the amplitude of the wave at a given time, argument amplitude in volts, frequency in hertz, time in radians, returns amplitude in volts
    current_amplitude = amplitude * math.cos(frequency * time)
    return current_amplitude

def calc_wave_amplitude_rt(amplitude , frequency , time): #calculate the amplitude of the wave at a given time, argument amplitude in volts, frequency in hertz, time in radians, returns amplitude in volts
    current_amplitude = -amplitude * math.cos(frequency * time + (pi / 2))
    return current_amplitude

def calc_wave_module(offset , polarity): #calculate the current wave amplitude between switching occurances with a given resolution according to increment_resolution, argument offset measured in volts, boolean polarity 
    time2 = 0
    global timer
    print(polarity)
    if (polarity == 1):
        while (time2 < (transient_period_positive / 2)):
            if (timer_lower_bound < timer < timer_upper_bound):
                storage.append(polarity * calc_wave_amplitude(transient_voltage_positive , transient_angular_frequency_positive / 2 , time2) + offset)
            time2 = time2 + generation_resolution
            timer = timer + generation_resolution
        time3 = 0
        while (time3 < (switching_period - transient_period_positive)):
            if (timer_lower_bound < timer < timer_upper_bound):
                storage.append(calc_wave_amplitude(voltage_ripple_positive , nominal_angular_frequency_positive , time3) + offset)
            time3 = time3 + generation_resolution
            timer = timer + generation_resolution
    else:
        while (time2 < (transient_period_negative / 2)):
            if (timer_lower_bound < timer < timer_upper_bound):
                storage.append(polarity * calc_wave_amplitude(transient_voltage_negative , transient_angular_frequency_negative / 2 , time2) + offset)
            time2 = time2 + generation_resolution
            timer = timer + generation_resolution
        time3 = 0
        while (time3 < (switching_period - transient_period_negative)): 
            if (timer_lower_bound < timer < timer_upper_bound):
                storage.append(calc_wave_amplitude(voltage_ripple_negative , nominal_angular_frequency_negative , time3) + offset)
            time3 = time3 + generation_resolution
            timer = timer + generation_resolution

def calc_rise_time_module(offset , polarity): #calculate the current voltage of the rise time linearly, argument boolean polarity
    time4 = 0
    global timer
    if (polarity == 1):
        while (time4 < (transient_period_positive / 2)):
            if (timer_lower_bound < timer < timer_upper_bound):
                storage.append(polarity * calc_wave_amplitude_rt(transient_rt_voltage_positive , transient_angular_frequency_positive / 2 , time4) - offset)
            time4 = time4 + generation_resolution
            timer = timer + generation_resolution
    else:
        while (time4 < (transient_period_negative / 2)):
            if (timer_lower_bound < timer < timer_upper_bound):
                storage.append(polarity * calc_wave_amplitude_rt(transient_rt_voltage_negative , transient_angular_frequency_negative / 2 , time4) - offset)
            time4 = time4 + generation_resolution
            timer = timer + generation_resolution

def calc_wave(): #iterate calculating wave modules according to num_of_modules
    int_nominal_wave_voltage = nominal_voltage_positive
    polarity = 1
    int_num_of_modules = 0
    while (int_num_of_modules < num_of_modules):
        calc_rise_time_module(int_nominal_wave_voltage , polarity)
        calc_wave_module(int_nominal_wave_voltage , polarity)
        if (int_nominal_wave_voltage == nominal_voltage_positive):
            int_nominal_wave_voltage = -nominal_voltage_negative
        else: 
            int_nominal_wave_voltage = nominal_voltage_positive
        polarity = -polarity
        int_num_of_modules = int_num_of_modules + 1
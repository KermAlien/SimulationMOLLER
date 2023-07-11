import math
from math import pi
import translationLayer

nominal_voltage = translationLayer.nominal_voltage
transient_voltage = translationLayer.transient_voltage
voltage_ripple = translationLayer.voltage_ripple
nominal_frequency = translationLayer.nominal_frequency
transient_frequency = translationLayer.transient_frequency
switching_frequency = translationLayer.switching_frequency
time_constant = translationLayer.time_constant

num_of_phases = translationLayer.num_of_phases
num_of_modules = translationLayer.num_of_modules
transient_resolution = translationLayer.transient_resolution
nominal_resolution = translationLayer.nominal_resolution
time_resolution = translationLayer.time_resolution

nominal_angular_frequency = translationLayer.nominal_angular_frequency
transient_angular_frequency = translationLayer.transient_angular_frequency
switching_angular_frequency = translationLayer.switching_angular_frequency

timer_lower_bound = translationLayer.timer_lower_bound
timer_upper_bound = translationLayer.timer_upper_bound

storage = [] #list used for data storage

timer = 0

# def calc_transient_decay(): #calculate the amplitude of the decay of the transient at a given time according to a decay function, argument time in radians, returns amplitude in volts
#     decay_amplitude = 0 #decay function, transient_voltage * e ^ -(x / time_constant), change the base to adjust the aggression of the decay
#     if (decay_amplitude > voltage_ripple):
#         return decay_amplitude
#     else:
#         return voltage_ripple

def calc_wave_amplitude(amplitude , frequency , time): #calculate the amplitude of the wave at a given time, argument amplitude in volts, frequency in hertz, time in radians, returns amplitude in volts
    current_amplitude = amplitude * math.cos(frequency * time)
    print(current_amplitude)
    return current_amplitude

def calc_wave_intersection(amplitude): #calculate the time in radians that the transient wave equals a given amplitude, argument amplitude in volts, returns time in radians
    time1 = 0
    acceptable_error = 30 #acceptable error between current amplitude and target amplitude in amplitude calculation, measured in volts
    while(1):
        current_amplitude = calc_wave_amplitude(transient_voltage , transient_angular_frequency / 2 , time1)
        if (current_amplitude > (amplitude + acceptable_error)):
            time1 = time1 + transient_resolution
        else:
            return time1

def calc_wave_module(offset , polarity): #calculate the current wave amplitude between switching occurances with a given resolution according to increment_resolution, argument offset measured in volts, boolean polarity 
    time2 = 0
    global timer
    while (time2 < calc_wave_intersection(nominal_voltage)): # type: ignore
        if (timer_lower_bound < timer < timer_upper_bound):
            storage.append(polarity * calc_wave_amplitude(transient_voltage , transient_angular_frequency / 2 , time2) + offset)
            time2 = time2 + transient_resolution
            timer = timer + transient_resolution
        else:
            time2 = time2 + transient_resolution
            timer = timer + transient_resolution

    time3 = 0
    while (time3 < (num_of_phases * (2 * pi))):
        if (timer_lower_bound < timer < timer_upper_bound):
            storage.append(polarity * calc_wave_amplitude(voltage_ripple , nominal_angular_frequency , time3) + offset)
            time3 = time3 + nominal_resolution
            timer = timer + nominal_resolution
        else:
            time3 = time3 + nominal_resolution
            timer = timer + nominal_resolution

def calc_rise_time_module(offset , polarity): #calculate the current voltage of the rise time linearly, argument boolean polarity
    time4 = 0
    global timer
    while (time4 < num_of_modules - 1):
        if (timer_lower_bound < timer < timer_upper_bound):
            if (polarity == 1):
                storage.append(calc_wave_amplitude(transient_voltage , transient_angular_frequency / 2 , time4) + offset)
            else:
                storage.append(calc_wave_amplitude(-transient_voltage , transient_angular_frequency / 2 , time4) + offset)
            time4 = time4 + transient_resolution
            timer = timer + transient_resolution
        else:
            time4 = time4 + transient_resolution
            timer = timer + transient_resolution

def calc_wave(): #iterate calculating wave modules according to num_of_wave_segments
    int_nominal_wave_voltage = nominal_voltage
    polarity = 1
    int_num_of_modules = 0
    while(int_num_of_modules < num_of_modules):
        if (int_num_of_modules < (num_of_modules - 1)):
            calc_rise_time_module(int_nominal_wave_voltage , polarity)
        calc_wave_module(int_nominal_wave_voltage , polarity)
        int_nominal_wave_voltage = -int_nominal_wave_voltage
        polarity = -polarity
        int_num_of_modules = int_num_of_modules + 1
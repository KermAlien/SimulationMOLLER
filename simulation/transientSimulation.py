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
transient_frequency_positive = translationLayer.transient_frequency_positive
transient_frequency_negative = translationLayer.transient_frequency_negative
switching_frequency = translationLayer.switching_frequency
time_constant = translationLayer.time_constant

transient_rise_time_positive = translationLayer.transient_rise_time_positive
transient_rise_time_negative = translationLayer.transient_rise_time_negative
transient_rise_time_radian_positive = translationLayer.transient_rise_time_radian_positive
transient_rise_time_radian_negative = translationLayer.transient_rise_time_radian_negative

num_of_phases_positive = translationLayer.num_of_phases_positive
num_of_phases_negative = translationLayer.num_of_phases_negative
num_of_modules = translationLayer.num_of_modules
generation_resolution = translationLayer.generation_resolution
graph_time_interval = translationLayer.graph_time_interval
lower_bound_limit = translationLayer.lower_bound_limit
upper_bound_limit = translationLayer.upper_bound_limit
lower_bound_limit_radian = translationLayer.lower_bound_limit_radian
upper_bound_limit_radian = translationLayer.upper_bound_limit_radian

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

storage = [] #list used for graph generation

global_timer = 0 #variable used to store the global time in calc_wave_module() and calc_rise_time_module()

def calc_transient_decay(time , polarity): #calculate the amplitude of the decay of the transient at a given time according to a decay function, argument time in radians, returns amplitude in volts
    if (polarity == 1):
        seconds_from_radians = time * (1 / nominal_angular_frequency_positive)
        decay_amplitude = transient_voltage_positive * pow(10000 , -(seconds_from_radians / time_constant)) #decay function, transient_voltage * e ^ -(x / time_constant), change the base to adjust the aggression of the decay
        if (decay_amplitude > voltage_ripple_positive):    
            return decay_amplitude
        else: 
            return voltage_ripple_positive
    else:
        seconds_from_radians = time * (1 / nominal_angular_frequency_negative)
        decay_amplitude = transient_voltage_negative * pow(10000 , -(seconds_from_radians / time_constant)) #decay function, transient_voltage * e ^ -(x / time_constant), change the base to adjust the aggression of the decay
        if (decay_amplitude > voltage_ripple_negative):    
            return decay_amplitude
        else: 
            return voltage_ripple_negative

def calc_wave_amplitude(amplitude , frequency , time): #calculate the amplitude of the wave at a given time, argument amplitude in volts, frequency in hertz, time in radians, returns amplitude in volts
    current_amplitude = amplitude * math.cos(frequency * time)
    return current_amplitude

def calc_wave_intersection(amplitude , polarity): #calculate the time in radians that the transient wave equals a given amplitude, argument amplitude in volts, returns time in radians
    time = 0
    acceptable_error = (0.01 * amplitude) #acceptable error between current amplitude and target amplitude in amplitude calculation, measured in volts
    if (polarity == 1):
        current_amplitude = transient_voltage_positive
        while(current_amplitude > (amplitude + acceptable_error)):
            current_amplitude = calc_wave_amplitude(transient_voltage_positive , transient_angular_frequency_positive , time)
            time = time + generation_resolution
        return time
    else: 
        current_amplitude = transient_voltage_negative
        while(current_amplitude > (amplitude + acceptable_error)):
            current_amplitude = calc_wave_amplitude(transient_voltage_negative , transient_angular_frequency_negative , time)
            time = time + generation_resolution
        return time

def calc_wave_module(offset , polarity , lower_bound_limit_radian , upper_bound_limit_radian): #calculate the current wave amplitude between switching occurances with a given resolution according to increment_resolution, argument offset measured in volts, boolean polarity 
    time = 0
    global global_timer
    if (polarity == 1):
        while (time < calc_wave_intersection(nominal_voltage_positive , polarity)):
            if (lower_bound_limit_radian < global_timer <= upper_bound_limit_radian):
                storage.append(polarity * calc_wave_amplitude(transient_voltage_positive , transient_angular_frequency_positive , time) + offset)
            time = time + generation_resolution
            global_timer = global_timer + generation_resolution
        time = 0
        while (time < (num_of_phases_positive * (2 * pi))):
            if (lower_bound_limit_radian < global_timer <= upper_bound_limit_radian):
                storage.append(calc_wave_amplitude(calc_transient_decay(time , polarity) , nominal_angular_frequency_positive, time) + offset)
            time = time + generation_resolution
            global_timer = global_timer + generation_resolution
    else: 
        while (time < calc_wave_intersection(nominal_voltage_negative , polarity)):
            if (lower_bound_limit_radian < global_timer <= upper_bound_limit_radian):
                storage.append(polarity * calc_wave_amplitude(transient_voltage_negative , transient_angular_frequency_negative , time) + offset)
            time = time + generation_resolution
            global_timer = global_timer + generation_resolution
        time = 0
        while (time < (num_of_phases_negative * (2 * pi))):
            if (lower_bound_limit_radian < global_timer <= upper_bound_limit_radian):
                storage.append(calc_wave_amplitude(calc_transient_decay(time , polarity) , nominal_angular_frequency_negative, time) + offset)
            time = time + generation_resolution
            global_timer = global_timer + generation_resolution

def calc_rise_time_module(polarity , lower_bound_limit_radian , upper_bound_limit_radian): #calculate the current voltage of the rise time linearly, argument boolean polarity
    int_num_of_steps = 0
    global global_timer
    if (polarity == 1):
        num_of_steps = (transient_rise_time_radian_positive / generation_resolution)
        delta_voltage = (nominal_voltage_positive + transient_voltage_positive)
        delta_voltage_per_step = (delta_voltage / num_of_steps)
        while (int_num_of_steps < num_of_steps):
            if (lower_bound_limit_radian < global_timer <= upper_bound_limit_radian):
                storage.append(nominal_voltage_positive - (delta_voltage_per_step * int_num_of_steps))
            int_num_of_steps = int_num_of_steps + 1
            global_timer = global_timer + generation_resolution
    else:
        num_of_steps = (transient_rise_time_radian_negative / generation_resolution)
        delta_voltage = (nominal_voltage_negative + transient_voltage_negative)
        delta_voltage_per_step = (delta_voltage / num_of_steps)
        while (int_num_of_steps < num_of_steps):
            if (lower_bound_limit_radian < global_timer <= upper_bound_limit_radian):
                storage.append(-nominal_voltage_negative + (delta_voltage_per_step * int_num_of_steps))
            int_num_of_steps = int_num_of_steps + 1
            global_timer = global_timer + generation_resolution

def calc_wave(lower_bound_limit_radian , upper_bound_limit_radian): #iterate calculating wave modules according to num_of_modules
    int_nominal_wave_voltage = nominal_voltage_positive
    polarity = 1
    int_num_of_modules = 0
    while(int_num_of_modules < num_of_modules):
        calc_wave_module(int_nominal_wave_voltage , polarity , lower_bound_limit_radian , upper_bound_limit_radian)
        if (int_num_of_modules < (num_of_modules - 1)):
            calc_rise_time_module(polarity , lower_bound_limit_radian , upper_bound_limit_radian)
        if (int_nominal_wave_voltage == nominal_voltage_positive):
            int_nominal_wave_voltage = -nominal_voltage_negative
        else: 
            int_nominal_wave_voltage = nominal_voltage_positive
        polarity = -polarity
        int_num_of_modules = int_num_of_modules + 1

#change num_of_phase * 2 * pi conditional to fix uneven compression
#same problem with transient frequency, compression
#weird spike following first transient
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
transient_resolution = translationLayer.transient_resolution
nominal_resolution = translationLayer.nominal_resolution
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
time2 = 0

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

def calc_wave_amplitude_rt(amplitude , frequency , time): #calculate the amplitude of the wave at a given time, argument amplitude in volts, frequency in hertz, time in radians, returns amplitude in volts
    current_amplitude = -amplitude * math.cos(frequency * time + (pi / 2)) - 3000
    return current_amplitude

def calc_wave_intersection(amplitude , polarity): #calculate the time in radians that the transient wave equals a given amplitude, argument amplitude in volts, returns time in radians
    time1 = 0
    acceptable_error = (0.01 * amplitude) #acceptable error between current amplitude and target amplitude in amplitude calculation, measured in volts
    if (polarity == 1):
        current_amplitude = transient_voltage_positive
        while (current_amplitude > (amplitude + acceptable_error)):
            current_amplitude = calc_wave_amplitude(transient_voltage_positive , transient_angular_frequency_positive / 2 , time1)
            time1 = time1 + transient_resolution
        return time1
    else: 
        current_amplitude = transient_voltage_negative
        while (current_amplitude > (amplitude + acceptable_error)):
            current_amplitude = calc_wave_amplitude(transient_voltage_negative , transient_angular_frequency_negative / 2 , time1)
            time1 = time1 + transient_resolution
        return time1

def calc_wave_module(offset , polarity): #calculate the current wave amplitude between switching occurances with a given resolution according to increment_resolution, argument offset measured in volts, boolean polarity 
    global time2
    time2 = 0
    global timer
    if (polarity == 1):
        while (time2 < calc_wave_intersection(nominal_voltage_positive , polarity)):
            if (timer_lower_bound < timer < timer_upper_bound):
                storage.append(polarity * calc_wave_amplitude(transient_voltage_positive , transient_angular_frequency_positive / 2 , time2))
                time2 = time2 + transient_resolution
                timer = timer + transient_resolution
            else:
                time2 = time2 + transient_resolution
                timer = timer + transient_resolution
        time3 = 0
        print('b')
        while (time3 < (num_of_phases_positive * (2 * pi))):
            if (timer_lower_bound < timer < timer_upper_bound):
                storage.append(calc_wave_amplitude(voltage_ripple_positive , nominal_angular_frequency_positive , time3) + offset)
                time3 = time3 + nominal_resolution
                timer = timer + nominal_resolution
            else:
                time2 = time2 + nominal_resolution
                timer = timer + nominal_resolution
    else:
        while (time2 < calc_wave_intersection(nominal_voltage_negative , polarity)):
            if (timer_lower_bound < timer < timer_upper_bound):
                storage.append(polarity * calc_wave_amplitude(transient_voltage_negative , transient_angular_frequency_negative / 2 , time2))
                time2 = time2 + transient_resolution
                timer = timer + transient_resolution
            else:
                time3 = time3 + transient_resolution
                timer = timer + transient_resolution
        time3 = 0
        while (time3 < (num_of_phases_negative * (2 * pi))):
            if (timer_lower_bound < timer < timer_upper_bound):
                storage.append(calc_wave_amplitude(voltage_ripple_negative , nominal_angular_frequency_negative, time3) + offset)
                time3 = time3 + nominal_resolution
                timer = timer + nominal_resolution
            else:
                time3 = time3 + nominal_resolution
                timer = timer + nominal_resolution

def calc_rise_time_module(polarity): #calculate the current voltage of the rise time linearly, argument boolean polarity
    time4 = 0
    global time2
    global timer
    if (polarity == 1):
        while (time4 < time2):
            if (timer_lower_bound < timer < timer_upper_bound):
                storage.append(-polarity * calc_wave_amplitude_rt(transient_rt_voltage_positive , transient_angular_frequency_positive / 2 , time4))
                time4 = time4 + transient_resolution
                timer = timer + transient_resolution
            else:
                time4 = time4 + transient_resolution
                timer = timer + transient_resolution
    else:
        while (time4 < time2):
            if (timer_lower_bound < timer < timer_upper_bound):
                storage.append(-polarity * calc_wave_amplitude_rt(transient_rt_voltage_negative , transient_angular_frequency_negative / 2 , time4))
                time4 = time4 + transient_resolution
                timer = timer + transient_resolution
            else:
                time4 = time4 + transient_resolution
                timer = timer + transient_resolution
        

def calc_wave(): #iterate calculating wave modules according to num_of_modules
    int_nominal_wave_voltage = nominal_voltage_positive
    polarity = 1
    int_num_of_modules = 0
    while (int_num_of_modules < num_of_modules):
        calc_wave_module(int_nominal_wave_voltage , polarity)
        calc_rise_time_module(polarity)
        if (int_nominal_wave_voltage == nominal_voltage_positive):
            int_nominal_wave_voltage = -nominal_voltage_negative
        else: 
            int_nominal_wave_voltage = nominal_voltage_positive
        polarity = -polarity
        int_num_of_modules = int_num_of_modules + 1

#change num_of_phase * 2 * pi conditional to fix uneven compression
#same problem with transient frequency, compression
#weird spike following first transient
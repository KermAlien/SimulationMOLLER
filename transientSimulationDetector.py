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

transient_rise_time = translationLayer.transient_rise_time
transient_radian_rise_time = translationLayer.transient_radian_rise_time

num_of_phases = translationLayer.num_of_phases
num_of_modules = translationLayer.num_of_modules
detector_resolution = translationLayer.detector_resolution
time_resolution = translationLayer.time_resolution

nominal_angular_frequency = translationLayer.nominal_angular_frequency
transient_angular_frequency = translationLayer.transient_angular_frequency
switching_angular_frequency = translationLayer.switching_angular_frequency

nominal_period = translationLayer.nominal_period
transient_period = translationLayer.transient_period
switching_period = translationLayer.switching_period

e = 2.7182818284590452353602874713527 #e constant

storage = [] #list used for graph generation

def calc_transient_decay(time): #calculate the amplitude of the decay of the transient at a given time according to a decay function, argument time in radians, returns amplitude in volts
    seconds_from_radians = time * (1 / nominal_angular_frequency)
    decay_amplitude = transient_voltage * (1 / pow(e , (seconds_from_radians / time_constant))) #decay function, transient_voltage * (1 / e ^ (x / time_constant))
    if (decay_amplitude > voltage_ripple):
        return decay_amplitude
    else:
        return voltage_ripple

def calc_wave_amplitude(amplitude , frequency , time): #calculate the amplitude of the wave at a given time, argument amplitude in volts, frequency in hertz, time in radians, returns amplitude in volts
    current_amplitude = amplitude * math.cos(frequency * time)
    return current_amplitude

def calc_wave_intersection(amplitude): #calculate the time in radians that the transient wave equals a given amplitude, argument amplitude in volts, returns time in radians
    time = (pi / 2)
    acceptable_error = 0.1 #acceptable error between current amplitude and target amplitude in amplitude calculation, measured in volts
    while(1):
        current_amplitude = calc_wave_amplitude(transient_voltage , transient_frequency , time)
        if (current_amplitude > (amplitude + acceptable_error)):
            time = time + detector_resolution
        else:
            return time

def calc_wave_module(offset , polarity): #calculate the current wave amplitude between switching occurances with a given resolution according to increment_resolution, argument offset measured in volts, boolean polarity 
    int_num_of_phases = 0
    while(int_num_of_phases < num_of_phases):
        time = 0
        if (int_num_of_phases == 0):
            while (time < calc_wave_intersection(nominal_voltage)): # type: ignore
                storage.append(polarity * calc_wave_amplitude(transient_voltage , transient_frequency , time) + offset)
                time = time + detector_resolution
        else:
            while (time < (2 * pi)):
                storage.append(calc_wave_amplitude(calc_transient_decay(time), nominal_frequency, time) + offset)
                time = time + detector_resolution
        int_num_of_phases = int_num_of_phases + 1

def calc_rise_time_module(polarity): #calculate the current voltage of the rise time linearly, argument boolean polarity
    num_of_steps = (transient_radian_rise_time / detector_resolution)
    delta_voltage = (nominal_voltage + transient_voltage)
    delta_voltage_per_step = (delta_voltage / num_of_steps)
    int_num_of_steps = 0
    while (int_num_of_steps < num_of_steps):
        if (polarity == 1):
            storage.append(nominal_voltage - (delta_voltage_per_step * int_num_of_steps))
        else:
            storage.append(-nominal_voltage + (delta_voltage_per_step * int_num_of_steps))
        int_num_of_steps = int_num_of_steps + 1

def calc_wave(): #iterate calculating wave modules according to num_of_wave_segments
    int_nominal_wave_voltage = nominal_voltage
    polarity = 1
    int_num_of_wave_modules = 0
    while(int_num_of_wave_modules < num_of_modules):
        calc_wave_module(int_nominal_wave_voltage , polarity)
        # calc_rise_time_module(polarity)
        int_nominal_wave_voltage = -int_nominal_wave_voltage
        polarity = -polarity
        int_num_of_wave_modules = int_num_of_wave_modules + 1
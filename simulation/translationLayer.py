import math
from math import pi
import constants

#transient simulation:
resistance = constants.resistance
capacitance = constants.capacitance

nominal_voltage = constants.nominal_voltage #nominal voltage of the wave, measured in volts
nominal_frequency = constants.nominal_frequency #wave frequency, measured in hertz
voltage_ripple = constants.voltage_ripple #voltage ripple in the wave at nominal voltage, measured in volts
transient_voltage = constants.transient_voltage #transient voltage of the wave, measured in volts
transient_frequency = constants.transient_frequency #transient frequency, measured in hertz
switching_frequency = constants.switching_frequency #switching frequency, measured in hertz
time_constant = resistance * capacitance #value to determine the rate of transient decay, full decay occurs after five time constants, measured in seconds

nominal_period = 1 / nominal_frequency #period of the wave, measured in seconds
transient_period = 1 / transient_frequency #period of the transient, measured in seconds
switching_period = 1 / switching_frequency #period of the switching, measured in seconds

nominal_angular_frequency = nominal_frequency * (2 * pi) #angular frequency of the wave, measured in radians
transient_angular_frequency = transient_frequency * (2 * pi) #angular frequency of the transient, measured in radians
switching_angular_frequency = switching_frequency * (2 * pi) #angular frequency of the switching, measured in radians

transient_rise_time = constants.transient_rise_time #transient rise time, measured in seconds
transient_radian_rise_time = transient_rise_time * nominal_angular_frequency #transient rise time, converted to radians according to the nominal angular frequency

#trigger pulse:
trigger_duty_cycle = constants.trigger_duty_cycle
trigger_nominal_voltage = constants.trigger_nominal_voltage
trigger_latency = constants.trigger_latency

trigger_rise_time = constants.trigger_rise_time
trigger_radian_rise_time = trigger_rise_time * nominal_angular_frequency

#systematic error:
percent_error = constants.percent_error

#general:
num_of_phases = (switching_period - transient_period) / nominal_period #number of nominal phases per wave module
num_of_modules = constants.num_of_modules #number of wave modules
generation_resolution = constants.generation_resolution #resolution with which the wave module is generated, measured in radians
graph_time_scale = constants.graph_time_scale #resolution for the x-axis on the graph, measured in seconds
graph_time_interval = constants.graph_time_interval #interval for the x-axis on the graph, measured in seconds

#need to change frequency for angular frequency in wave calculations
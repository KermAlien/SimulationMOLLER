import math
from math import pi
import constants

current_limit = constants.nominal_voltage / constants.resistance
beta = 1 / current_limit
deadtime = beta * constants.capacitance * constants.nominal_voltage

nominal_voltage = constants.nominal_voltage #5 #nominal voltage of the wave
transient_voltage = 0 #10 #transient voltage of the wave
voltage_ripple = constants.voltage_ripple #0.5 #voltage ripple in the wave at nominal voltage
nominal_frequency = 0 #3 #wave frequency
transient_frequency = 1 / deadtime #1 #transient frequency
switching_frequency = constants.switching_frequency #2 #switching frequency
time_constant = constants.resistance * constants.capacitance #0.75 #arbitrary value to set the agression of the transient decay, zero equals no decay and one equals immediate decay

nominal_angular_frequency = nominal_frequency * (2 * pi) #calculate the angular frequency of the wave in radians
transient_angular_frequency = transient_frequency * (2 * pi) #calculate the angular frequency of the transient in radians
switching_angular_frequency = switching_frequency * (2 * pi) #calculate the angular frequency of the switching in radians

nominal_period = 1 / nominal_frequency #calculate the period of the wave in radians
transient_period = 1 / transient_frequency #calculate the period of the transient in radians
switching_period = 1 / switching_frequency #calculate the period of the switching in radians

num_of_phases = (switching_period - transient_period) / nominal_period #3 #number of phases per wave module
num_of_modules = constants.num_of_modules #3 #number of wave modules
resolution = constants.resolution #0.01 #resolution with which the wave module is generated, measured in radians
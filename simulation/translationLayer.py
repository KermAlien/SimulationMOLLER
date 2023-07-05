import math
from math import pi
import constants

current_limit = constants.nominal_voltage / constants.resistance #current limit of the crystal system, measured in amps
beta = 1 / current_limit #coefficient of the formula T = (beta)cv, measured in amps
deadtime = beta * constants.capacitance * constants.nominal_voltage #measurment deadtime, calculation for the formula T = (beta)cv, measured in seconds

nominal_voltage = constants.nominal_voltage #nominal voltage of the wave, measured in volts
transient_voltage = constants.transient_voltage #transient voltage of the wave, measured in volts #--------------------------------------------------------------
voltage_ripple = constants.voltage_ripple #voltage ripple in the wave at nominal voltage, measured in volts
nominal_frequency = constants.nominal_frequency #wave frequency, measured in hertz
transient_frequency = 1 / deadtime #transient frequency, measured in hertz
switching_frequency = constants.switching_frequency #switching frequency, measured in hertz
time_constant = constants.resistance * constants.capacitance #value to determine the rate of transient decay, full decay occurs after five time constants, measured in seconds

nominal_angular_frequency = nominal_frequency * (2 * pi) #angular frequency of the wave, measured in radians
transient_angular_frequency = transient_frequency * (2 * pi) #angular frequency of the transient, measured in radians
switching_angular_frequency = switching_frequency * (2 * pi) #angular frequency of the switching, measured in radians

nominal_period = 1 / nominal_frequency #period of the wave, measured in seconds
transient_period = 1 / transient_frequency #period of the transient, measured in seconds
switching_period = 1 / switching_frequency #period of the switching, measured in seconds

rise_time = constants.rise_time #transient rise time, measured in seconds #-----------------------------------------------------------------
radian_rise_time = rise_time * nominal_angular_frequency #transient rise time, converted to radians according to the nominal angular frequency

num_of_phases = (switching_period - transient_period) / nominal_period #number of phases per wave module
num_of_modules = constants.num_of_modules #number of wave modules
resolution = constants.resolution #resolution with which the wave module is generated, measured in radians
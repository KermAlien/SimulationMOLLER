import math
from math import pi
import constants

#transient simulation:
nominal_voltage = constants.nominal_voltage #nominal voltage of the wave, measured in volts
transient_voltage = constants.transient_voltage #transient voltage of the wave, measured in volts #--TEMP------------------------------------------------------------
voltage_ripple = constants.voltage_ripple #voltage ripple in the wave at nominal voltage, measured in volts
nominal_frequency = constants.nominal_frequency #wave frequency, measured in hertz
transient_frequency = constants.transient_frequency #transient frequency, measured in hertz
switching_frequency = constants.switching_frequency #switching frequency, measured in hertz
time_constant = constants.resistance * constants.capacitance #value to determine the rate of transient decay, full decay occurs after five time constants, measured in seconds

nominal_angular_frequency = nominal_frequency * (2 * pi) #angular frequency of the wave, measured in radians
transient_angular_frequency = transient_frequency * (2 * pi) #angular frequency of the transient, measured in radians
switching_angular_frequency = switching_frequency * (2 * pi) #angular frequency of the switching, measured in radians

nominal_period = (1 / nominal_frequency) #period of the wave, measured in seconds
transient_period = (1 / transient_frequency) #period of the transient, measured in seconds
switching_period = (1 / switching_frequency) #period of the switching, measured in seconds

#trigger pulse:
trigger_radian_rise_time = 0

#general:
num_of_phases = (switching_period - transient_period) / nominal_period #number of phases per wave module
num_of_modules = constants.num_of_modules #number of wave modules

transient_resolution = constants.transient_resolution #resolution with which the transient wave is generated, measured in radians
nominal_resolution = constants.nominal_resolution

detector_period = 1 / constants.detector_resolution #period with which the wave is "measured" by the detector, measured in seconds
BCM_period = 1 / constants.BCM_resolution #period with which the wave is "measured" by the BCM, measured in seconds

time_resolution = constants.time_resolution #resolution for the x-axis on the graph, measured in seconds

#timer
timer_lower_bound = constants.timer_lower_bound
timer_upper_bound = constants.timer_upper_bound

print(num_of_phases)
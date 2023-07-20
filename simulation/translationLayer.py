import math
from math import pi
import constants

#transient simulation:
resistance = constants.resistance
capacitance = constants.capacitance

nominal_voltage_positve = constants.nominal_voltage_positve #positive nominal voltage of the wave, measured in volts
nominal_voltage_negative = constants.nominal_voltage_negative #negative nominal voltage of the wave, measured in volts
nominal_frequency_positive = constants.nominal_frequency_positive #positive wave frequency, measured in hertz
nominal_frequency_negative = constants.nominal_frequency_negative #negative wave frequency, measured in hertz
voltage_ripple_positive = constants.voltage_ripple_positive #positive voltage ripple in the wave at nominal voltage, measured in volts
voltage_ripple_negative = constants.voltage_ripple_negative #negative voltage ripple in the wave at nominal voltage, measured in volts
transient_voltage_positive = constants.transient_voltage_positive #positive transient voltage of the wave, measured in volts
transient_voltage_negative = constants.transient_voltage_negative #negative transient voltage of the wave, measured in volts
transient_rt_voltage_positive = constants.transient_rt_voltage_positive #positive voltage of the rise time for the transient of the wave, measured in volts
transient_rt_voltage_negative = constants.transient_rt_voltage_negative #negative voltage of the rise time for the transient of the wave, measured in volts
transient_frequency_positive = constants.transient_frequency_positive #positive transient frequency, measured in hertz
transient_frequency_negative = constants.transient_frequency_negative #negative transient frequency, measured in hertz
switching_frequency = constants.switching_frequency #switching frequency, measured in hertz
time_constant = resistance * capacitance #value to determine the rate of transient decay, full decay occurs after five time constants, measured in seconds

nominal_period_positive = 1 / nominal_frequency_positive #positive period of the wave, measured in seconds
nominal_period_negative = 1 / nominal_frequency_negative #negative period of the wave, measured in seconds
transient_period_positive = 1 / transient_frequency_positive #postive period of the transient, measured in seconds
transient_period_negative = 1 / transient_frequency_negative #negative period of the transient, measured in seconds
switching_period = 1 / switching_frequency #period of the switching, measured in seconds

nominal_angular_frequency_positive = int(nominal_frequency_positive * (2 * pi)) #positve angular frequency of the wave, measured in radians
nominal_angular_frequency_negative = int(nominal_frequency_negative * (2 * pi)) #negative angular frequency of the wave, measured in radians
transient_angular_frequency_positive = int(transient_frequency_positive * (2 * pi)) #positive angular frequency of the transient, measured in radians
transient_angular_frequency_negative = int(transient_frequency_negative * (2 * pi)) #negative angular frequency of the transient, measured in radians
switching_angular_frequency = int(switching_frequency * (2 * pi)) #angular frequency of the switching, measured in radians

#trigger pulse:
#trigger_duty_cycle = constants.trigger_duty_cycle
#trigger_nominal_voltage = constants.trigger_nominal_voltage
#trigger_latency = constants.trigger_latency

#trigger_rise_time = constants.trigger_rise_time
#trigger_radian_rise_time = trigger_rise_time * nominal_angular_frequency

#systematic error:
#percent_error = constants.percent_error

#general:
num_of_phases_positive = (switching_period - transient_period_positive) / nominal_period_positive #positive number of nominal phases per wave module
num_of_phases_negative = (switching_period - transient_period_negative) / nominal_period_negative #negative number of nominal phases per wave module
num_of_modules = constants.num_of_modules #number of wave modules
graph_time_interval = constants.graph_time_interval #interval for the x-axis on the graph, measured in seconds

generation_resolution = constants.generation_resolution

#sampling:
BCM_resolution = constants.BCM_resolution

#timer:
timer_lower_bound = constants.timer_lower_bound
timer_upper_bound = constants.timer_upper_bound
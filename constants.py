import math
#transient simulation:
nominal_voltage = 3000 #nominal voltage of the power circuitry, meansured in volts
nominal_frequency = 333333 #Roughly double transient frequency? #nominal frequency of the power circuitry, measured in hertz
voltage_ripple = 600 #voltage ripple of the power circuitry, measured in volts
switching_frequency = 1920 #1920 #switching frequency of the power circuitry, measured in hertz

#trigger pulse:
trigger_rise_time = 0
trigger_duty_cycle = 0
trigger_latency = 0

#general:
num_of_modules = 2 #number of simulated voltage transistions
time_resolution = 1 #resolution for the x-axis on the graph, measured in microseconds
transient_resolution = 0.00000001 #resolution with which the transient wave is generated, measured in radians
nominal_resolution = math.pi/32 #resolution with which the nominal wave is generated, measured in radians

BCM_resolution = 1000 #resolution with which the wave is "measured" by the BCM, measured in hertz
detector_resolution = 100000 #resolution with which the wave is "measured" by the detector, measured in hertz

#temp:
transient_frequency = 98039 #transient frequency, measured in hertz
transient_voltage = 11400 #volts

#timer
timer_lower_bound = 0#1068
timer_upper_bound = 10000000#1075

asymmetry = 0.000001

generation_resolution = (transient_resolution + nominal_resolution) / 2
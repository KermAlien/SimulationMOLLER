#transient simulation:
resistance = 730000000000 # resistance of the RTP crystal, measured in ohms
capacitance = 0.0000000000000006 # capacitance of the RTP crystal, measured in farads
nominal_voltage_positve = 3000 #positve nominal voltage of the power circuitry, measured in volts
nominal_voltage_negative = 3000 #negative nominal voltage of the power circuitry, measured in volts
nominal_frequency_positive = 500000 #positive nominal frequency of the power circuitry, measured in hertz
nominal_frequency_negative = 500000 #negative nominal frequency of the power circuitry, measured in hertz
voltage_ripple_positive = 600 #voltage ripple of the power circuitry, measured in volts
voltage_ripple_negative = 600 #voltage ripple of the power circuitry, measured in volts
transient_voltage_positive = 11400 #voltage of the transient, measured in volts
transient_voltage_negative = 11400 #voltage of the transient, measured in volts
transient_rt_voltage_positive = 17400 #voltage of the transient, measured in volts
transient_rt_voltage_negative = 17400 #voltage of the transient, measured in volts
transient_frequency_positive = 98039 #positive frequency of the transient, measured in hertz
transient_frequency_negative = 98039 #negative frequency of the transient, measured in hertz
switching_frequency = 1920 #switching frequency of the power circuitry, measured in hertz

#trigger pulse:
#trigger_duty_cycle = 0.5
#trigger_nominal_voltage = 5
#trigger_latency = 0
#trigger_rise_time = 0.001

#systematic error:
#percent_error = 0

#general:
generation_resolution = 0.000000001 #resolution with which the wave is generated, measured in radians

num_of_modules = 3 #number of simulated voltage transistions
graph_time_interval = 0.0001 #interval for the x-axis on the graph, measured in seconds

BCM_resolution = 10000 #frequency with which the BCM measures the wave aka samples per second, measured in hertz

#timer
timer_lower_bound = 0
timer_upper_bound = 10000000000 #1604.227 for the full wave
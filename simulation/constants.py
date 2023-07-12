#transient simulation:
resistance = 730000000000 #resistance of the RTP crystal, measured in ohms
capacitance = 0.0000000000000006 #capacitance of the RTP crystal, measured in farads
nominal_voltage_positve = 5000 #positve nominal voltage of the power circuitry, measured in volts
nominal_voltage_negative = 5000 #negative nominal voltage of the power circuitry, measured in volts
nominal_frequency_positive = 500000 #positive nominal frequency of the power circuitry, measured in hertz
nominal_frequency_negative = 500000 #negative nominal frequency of the power circuitry, measured in hertz
voltage_ripple_positive = 600 #voltage ripple of the power circuitry, measured in volts
voltage_ripple_negative = 600 #voltage ripple of the power circuitry, measured in volts
transient_voltage_positive = 14400 #voltage of the transient, measured in volts
transient_voltage_negative = 14400 #voltage of the transient, measured in volts
transient_frequency_positive = 28114 #positive frequency of the transient, measured in hertz
transient_frequency_negative = 28114 #negative frequency of the transient, measured in hertz
transient_rise_time_positive = 0.00000025 #positive period of the transient rise time, measured in seconds
transient_rise_time_negative = 0.00000025 #negative period of the transient rise time, measured in seconds
switching_frequency = 1920 #switching frequency of the power circuitry, measured in hertz

#trigger pulse:
#trigger_duty_cycle = 0.5
#trigger_nominal_voltage = 5
#trigger_latency = 0
#trigger_rise_time = 0.001

#systematic error:
#percent_error = 0

#general:
num_of_modules = 3 #number of simulated voltage transistions
generation_resolution = 0.1 #resolution with which the wave is generated, measured in radians
graph_time_interval = 0.0001 #interval for the x-axis on the graph, measured in seconds
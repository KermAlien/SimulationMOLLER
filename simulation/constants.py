#transient simulation:
resistance = 730000000 #resistance of the RTP crystal, measured in ohms
capacitance = 0.0000000000033 #capacitance of the RTP crystal, measured in farads
nominal_voltage = 30 #nominal voltage of the power circuitry, meansured in volts
nominal_frequency = 25 #1920 #nominal frequency of the power circuitry, measured in hertz
voltage_ripple = 5 #voltage ripple of the power circuitry, measured in volts
switching_frequency = 10 #switching frequency of the power circuitry, measured in hertz

#trigger pulse:
trigger_rise_time = 0
trigger_duty_cycle = 0
trigger_latency = 0

#general:
num_of_modules = 3 #number of simulated voltage transistions
generation_resolution = 0.01 #resolution with which the wave is generated, measured in radians
time_resolution = 0.25 #resolution for the x-axis on the graph, measured in seconds

#temp:
transient_voltage = 25
transient_rise_time = 0.01
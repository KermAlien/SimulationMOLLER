import translationLayer

switching_period = translationLayer.switching_period
switching_angular_frequency = translationLayer.switching_angular_frequency
num_of_modules = translationLayer.num_of_modules
generation_resolution = translationLayer.generation_resolution
trigger_duty_cycle = translationLayer.trigger_duty_cycle
trigger_nominal_voltage = translationLayer.trigger_nominal_voltage
trigger_latency = translationLayer.trigger_latency
trigger_rise_time = translationLayer.trigger_rise_time
trigger_radian_rise_time = translationLayer.trigger_radian_rise_time

trigger = [] #list used for triggerPulse generation

def calc_rise_time_module(polarity): #calculate the current voltage of the rise time linearly, argument boolean polarity
    num_of_steps = (trigger_radian_rise_time / generation_resolution)
    delta_voltage_per_step = ((2 *trigger_nominal_voltage) / num_of_steps)
    int_num_of_steps = 0
    while (int_num_of_steps < num_of_steps):
        if (polarity == 1):
            trigger.append(-trigger_nominal_voltage + (delta_voltage_per_step * int_num_of_steps))
        else:
            trigger.append(trigger_nominal_voltage - (delta_voltage_per_step * int_num_of_steps))
        int_num_of_steps = int_num_of_steps + 1

def calc_trigger(): #generate a trigger pulse according to a PWM waveform 
    int_num_of_modules = 0
    polarity = 1
    while (int_num_of_modules < num_of_modules):
        calc_rise_time_module(polarity)
        time = 0
        if (polarity == 1):
            while (time < (trigger_duty_cycle * (switching_period - trigger_rise_time))):
                trigger.append(polarity * trigger_nominal_voltage)
                time = time + (generation_resolution * (1 / switching_angular_frequency))
        else: 
            while (time < ((1 - trigger_duty_cycle) * (switching_period - trigger_rise_time))):
                trigger.append(polarity * trigger_nominal_voltage)
                time = time + (generation_resolution * (1 / switching_angular_frequency))
        polarity = -polarity
        int_num_of_modules = int_num_of_modules + 1

#generalize calc_rise_time_module() with transientSimulation?
#make triggerPulse wave start from zero
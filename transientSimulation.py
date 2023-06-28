import math
from math import sin
from math import pi
import time

import matplotlib.pyplot as plt

nominal_wave_voltage = 0.5
storage = []

def define_decay_curve(time):
    function_decay_amplitude = -time/0.25 + 3
    nominal_amplitude = nominal_wave_voltage
    if (function_decay_amplitude >= nominal_amplitude):
        return function_decay_amplitude
    else:
        return nominal_amplitude

def define_wave(amplitude , frequency , time):
    current_amplitude = amplitude * math.sin(frequency * time)
    return current_amplitude

increment_resolution = 0.1

def generate_wave(frequency , offset):
    period = frequency / (2 * pi) #calculate the period of the wave in seconds
    peak_time = 0
    x = 0
    while(x < 10):
        decay_peak = define_decay_curve(peak_time + (period / 4))
        int_peak_time = peak_time
        while (peak_time < (int_peak_time + (period / 2))):
            storage.append(define_wave(decay_peak , frequency , peak_time) + offset)
            peak_time = peak_time + increment_resolution
            #time.sleep(0.1)
        x = x + 1

y=0
while (y < 4):
    generate_wave(5 , 5)
    generate_wave(5 , -5)
    y = y + 1

plt.plot(storage)
plt.show()
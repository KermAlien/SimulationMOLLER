import transientSimulation
import translationLayer
import math

transient_voltage = translationLayer.transient_voltage
transient_frequency = translationLayer.transient_frequency
nominal_angular_frequency = translationLayer.nominal_angular_frequency
generation_resoltuion = translationLayer.generation_resolution
nominal_frequency = translationLayer.nominal_frequency

x = 0
while (x < 1):
    transientSimulation.calc_wave_amplitude(transient_voltage , transient_frequency , x)
    x = x + 0.000001

time = 0
while (time < (2 * math.pi)):
    print(transientSimulation.calc_wave_amplitude(transientSimulation.calc_transient_decay(time) , nominal_frequency , time))
    time = time + generation_resoltuion
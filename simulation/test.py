import transientSimulation
import translationLayer

transient_voltage = translationLayer.transient_voltage
transient_frequency = translationLayer.transient_frequency

x = 0
while (x < 1):
    print(transientSimulation.calc_wave_amplitude(transient_voltage , transient_frequency , x))
    x = x + 0.000001
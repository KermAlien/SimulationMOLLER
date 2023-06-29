import transientSimulation
import matplotlib.pyplot as plt

transientSimulation.calc_wave()

plt.plot(transientSimulation.storage)
plt.show()
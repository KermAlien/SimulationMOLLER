# import translationLayer
# import transientSimulation

# switching_angular_frequency = translationLayer.switching_angular_frequency
# generation_resolution = translationLayer.generation_resolution

# transientSimulation.calc_wave()

# storage = transientSimulation.storage

# BCM_storage = [] #list used for BCM graph generation

# rads_in_wave = len(storage) * generation_resolution #total number of radians in the original wave

# seconds_in_wave = rads_in_wave * (1 / switching_angular_frequency)

# print(seconds_in_wave)

# num_of_measurements_BCM = rads_in_wave / BCM_resolution #number of measurements that the BCM takes of the original wave

# def read_current_amplitude(radian_location): #returns the current amplitude of the wave at a given radian location, parameter radian_location in radians
#     current_amplitude = storage[int(radian_location / generation_resolution)]
#     return current_amplitude

# def calc_wave_BCM():
#     time = 0
#     while (time < num_of_measurements_BCM):
#         BCM_storage.append(read_current_amplitude(time))
#         time = time + BCM_resolution
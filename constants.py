# Deadtime constants
resistance = 5 # Measured in Megaohms ()
capacitance = 3 # Measured in picofarads (2-3 when 12x12x10)
voltage = 100 # Measured in kilovolts ()
currentLimit = voltage/resistance # Measured in kiloamperes

beta = 1/currentLimit

deadtime = beta * capacitance * voltage










driverFrequency = 1.92 # Measured in kilohertz

# Want to minimize aperture size
# Longer crystal = less V, more C
# Deadtime limited by current limit through optocouplers
# With solid-states drivers deadtime can be significantly reduced but peizoeletric ringing becomes an issue

# 12x12x10 mm crystals
# When deadtime < 7-8 microseconds some ringing is present
# Larger crystals = easier ringing

frequencyResonance = 250 # Measured in kilohertz (200-350)
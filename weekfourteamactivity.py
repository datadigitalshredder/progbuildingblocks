print('week4teamactivity')
# mass = float(input('What is the mass of the object in kilograms?'))
# gravity = float(input('What is the gravity? Note: earth is 9.8m/s squared and Jupiter is 24m/s squared.'))
# time = float(input('What is the time in seconds the rock will fall for?'))
# density = float(input('What is the fluid density? Note: water density is 1000kg/m cubed and air density is 1.3kg/m cubed'))
# area = float(input('What is the cross sectional area of the projectile in square meters?'))
# drag_constant = float(input('What is the drag constant? Note: constant for sphere is 0.5 and cylinder is 1.1'))
# drag_force = (density * area * drag_constant) / 2
# drag_force_3decimals = f'Drag force: {drag_force:.3f}'
# print(drag_force_3decimals)

# import math
# velocity = math.sqrt(mass * gravity / drag_force) * (1 - math.exp ((- math.sqrt(mass * gravity * drag_force) / mass) * time))
# output = f'The velocity in m/s after t seconds is: \n\nVelocity {velocity:.3f} m/s'
# print(output)

# stretch activity
# Bowling ball
# mass_bowling_ball = float(input('What is the mass of the bowling ball in kilograms?'))
# area_of_bowling_ball = float(input('What is the cross setional area of a bowling ball in square meters?'))
# gravity = float(input('What is the gravity? Note: earth is 9.8m/s squared and Jupiter is 24m/s squared.'))
# density = float(input('What is the fluid density? Note: water density is 1000kg/m cubed and air density is 1.3kg/m cubed'))
# time = float(input('What is the time in seconds of the object will fall for?'))
# drag_constant = float(input('What is the drag constant? Note: constant for sphere is 0.5 and cylinder is 1.1'))
# drag_force_bowling = (density * area_of_bowling_ball * drag_constant) / 2

# Loaf of bread
# mass_of_bread = float(input('What is the mass of a loaf of bread?'))
# area_of_bread = float(input('What is the cross sectional area of a loaf of bread?'))
# gravity = float(input('What is the gravity? Note: earth is 9.8m/s squared and Jupiter is 24m/s squared.'))
# density = float(input('What is the fluid density? Note: water density is 1000kg/m cubed and air density is 1.3kg/m cubed'))
# time = float(input('What is the time in seconds of the object will fall for?'))
# drag_constant = float(input('What is the drag constant? Note: constant for sphere is 0.5 and cylinder is 1.1'))
# drag_force_bread = (density * area_of_bread * drag_constant) / 2

# Skydiver
mass_of_skydiver = float(input('What is the mass of a sky diver?'))
area_of_skydiver = float(input('What is the cross sectional area of a skydiver?'))
gravity = float(input('What is the gravity? Note: earth is 9.8m/s squared and Jupiter is 24m/s squared.'))
density = float(input('What is the fluid density? Note: water density is 1000kg/m cubed and air density is 1.3kg/m cubed'))
time = float(input('What is the time in seconds of the object will fall for?'))
drag_constant = float(input('What is the drag constant? Note: constant for sphere is 0.5 and cylinder is 1.1'))
drag_force_skydiver = (density * area_of_skydiver * drag_constant) / 2

import math
# velocity = math.sqrt(mass_of_skydiver * gravity / drag_force_skydiver) * (1 - math.exp ((- math.sqrt(mass_of_skydiver * gravity * drag_force_skydiver) / mass_of_skydiver) * time))
# output = f'The velocity in m/s after t seconds is: \n\nVelocity {velocity:.3f} m/s'
# print(output)

#Terminal velocity
# Time at terminal velocity is 108 seconds and on
terminal_velocity = math.sqrt(mass_of_skydiver * gravity / drag_force_skydiver) 
output = f'The terminal velocity in m/s is: \n\nVelocity {terminal_velocity:.3f} m/s'
print(output)
# output terminal velocity of skydiver on earth in air is 82.784 m/s, Given weight of skydiver is 75kg, cross sectional area of human body 0.15 m^2, 
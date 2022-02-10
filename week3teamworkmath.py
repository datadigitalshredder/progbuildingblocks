print('teamworkweekthree')
# side = int(input('What is the length of the side of a square in meters?'))
# length = int(input('What is the lenght of a rectangle in meters?'))
# width = int(input('What is the width of a rectangle in meters?'))
# radius = int(input('What is the radius of a circle in meters?'))

# side = float(input('What is the length of the side of a square in meters?'))
# length = float(input('What is the length of a rectangle in meters?'))
# width = float(input('What is the width of a rectangle in meters?'))
# radius = float(input('What is the radius of a circle in meters?'))
# area_of_a_square = side ** 2
# area_of_a_rectangle = length * width

# Stretch activity
import math
# area_of_a_circle = (math.pi) * radius ** 2
# output = f'The area of a square is: {area_of_a_square} sqrm OR {area_of_a_square * 10000} sqrcm \nThe area of a rectangle is: {area_of_a_rectangle} sqrm OR {area_of_a_rectangle * 10000} sqrcm \nThe area of a cirlce is: {area_of_a_circle} sqrm OR {area_of_a_circle * 10000} sqrcm'
# print(output)

state_your_value = float(input('State any mumeric value'))
area_of_a_square = state_your_value ** 2
area_of_a_circle = (math.pi) * state_your_value ** 2
volume_of_a_cube = state_your_value ** 3
volume_of_a_sphere = 4 / 3 * (math.pi) * state_your_value ** 3
output = f'From the selected value: \n\nThe area of a squre is: {area_of_a_square} \nThe area of a circle is: {area_of_a_circle} \nThe volume of a cube is: {volume_of_a_cube} \nThe volume of a sphere is: {volume_of_a_sphere}'
print(output)


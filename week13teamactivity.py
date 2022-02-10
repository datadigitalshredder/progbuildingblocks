print('Week 13 team activity')

import math

#  Define the Functions

# def compute_area_square(side):
#     return side ** 2

# def compute_area_rectangle(length, width):
#     return length * width

# def compute_area_circle(radius):
#     return (math.pi) * radius ** 2

# CORE
# shape = ''
# while shape != 'quit':
#     shape = input('What shape would you like to analyze the area for (square or rectangle or circle): ')
#     # Create variables for the different shapes
#     if shape.lower() == 'square':
#         side = float(input('Enter the size of the side of the square: '))
#         # Call the functions into a variable and print
#         area_of_a_square = compute_area_square(side)
#         print(f'The area of the square is {area_of_a_square}')
    
#     elif shape.lower() == 'rectangle':
#         width = float(input('Enter the width of the rectangle: '))
#         length = float(input('Enter the height of the rectangle: '))

#         area_of_a_rectangle = compute_area_rectangle(length, width)
#         print(f'The area of the rectangle is {area_of_a_rectangle}')
    
#     elif shape.lower() == 'circle':
#         radius = float(input('Enter the radius of the circle: '))

#         area_of_a_circle = compute_area_circle(radius)
#         print(f'The area of a circle is {area_of_a_circle}')

# else:
#     print('Thank you!')

# STRETCH
def compute_area_square(side):
    return side ** 2

def compute_area_rectangle(length, width):
    return length * width

def compute_area_circle(radius):
    return math.pi * radius ** 2

# Stretch 2
def compute_area(shape, square = True):
    if square:
        area = side ** 2
    else:
        area = math.pi * radius ** 2
    return area
# Stretch 3 Function
def compute_area(shape, value1, value2 = False):
        area = -1
        if shape == 'square':
            area = compute_area_square(value1)
        elif shape  == 'rectangle':
            area = compute_area_rectangle(value1, value2)
        elif shape == 'circle':
            area = compute_area_circle(value1)
        return area


shape = ''
while shape != 'quit':
    shape = input('What shape would you like to analyze the area for (square or rectangle or circle): ').lower()
    # Create variables for the different shapes
    # if shape.lower() == 'square':
        # side = float(input('Enter the size of the side of the square: '))
        # # Call the functions into a variable and print
        # Stretch 1
        # area_of_a_square = compute_area_rectangle(side, side)
        # print(f'The area of the square is {area_of_a_square}')
    
    # if shape.lower() == 'rectangle':
    #     width = float(input('Enter the width of the rectangle: '))
    #     length = float(input('Enter the height of the rectangle: '))

    #     area_of_a_rectangle = compute_area_rectangle(length, width)
    #     print(f'The area of the rectangle is {area_of_a_rectangle}')
    
    # elif shape.lower() == 'circle':
    #     radius = float(input('Enter the radius of the circle: '))

    #     area_of_a_circle = compute_area_circle(radius)
    #     print(f'The area of a circle is {area_of_a_circle}')
    
    # Stretch 2
    # elif shape.lower() == 'square' or shape.lower() == 'circle':
    #     side = float(input('Enter the size of the side of the square: '))
    #     radius = float(input('Enter the radius of the circle: '))
    #     area_of_shape = compute_area(side)
    #     area_of_shape1 = compute_area(radius, False)
    #     print(f'The area of a the square is {area_of_shape}, and the area of circle is {area_of_shape1}.')
    
    # Stretch 3 continued
    
    if shape.lower() == 'square':
        side = float(input('Enter the size of the side of the square: '))
        area = compute_area(shape, side)
        print(f'The area of the square is {area}.')
    elif shape.lower() == 'rectangle':
        width = float(input('Enter the width of the rectangle: '))
        length = float(input('Enter the height of the rectangle: '))
        area1 = compute_area(shape, length, width)
        print(f'The area of the rectangle is {area1}.')
    elif shape.lower() == 'circle':
        radius = float(input('Enter the radius of the circle: '))
        area2 = compute_area(shape, radius)
        print(f'The area of the circle is {area2}.')
    # print(f'The area of a the square is {area}, the area of the rectangle is {area1} and the area of circle is {area2}.')
        
else:
    print('Thank you!')
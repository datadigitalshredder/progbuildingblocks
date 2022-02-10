import math
shape = ''

def compute_area_rectangle(b, c):
    return b * c
    
def compute_area_square(a):
    return compute_area_rectangle(a, a)

# a = int(input("What is the length of a side of the square? "))
# square_area = compute_area_square(a)
# print(f'Square area is: {square_area}')

# b = int(input('What is the length of rectangle? '))
# c = int(input('What is the width of the rectangle? '))
# rectangle_area = compute_area_rectangle(b, c)
# print(f'Rectangle area is: {rectangle_area}')

def compute_area_circle(r):
    return math.pi*r**2

# r = int(input('What is the radius of the circle? '))
# circle_area = compute_area_circle(r)
# print(f'Circle area is: {circle_area}')

def compute_area(shape, length, width=0):
    if shape == 'rectangle':
        rectangle_area = compute_area_rectangle(length, width)
        print(f'Rectangle area is: {rectangle_area}')
    if shape == 'square':
        square_area = compute_area_square(length)
        print(f'Square area is: {square_area}')
    if shape == 'circle':
        circle_area = compute_area_circle(length)
        print(f'Circle area is: {circle_area:.2f}')

while shape != 'quit':
    shape = input('What kind of shape do you have (square, rectangle, circle)? ')
    if shape == 'square' or shape == 'rectangle' or shape == 'circle':
        length = int(input('length? '))
        if shape == 'rectangle':
            width = int(input('width? '))
            compute_area(shape, length, width)
            # rectangle_area = compute_area_rectangle(length, width)
            # print(f'Rectangle area is: {rectangle_area}')
        # if shape == 'square':
        #     square_area = compute_area_square(length)
        #     print(f'Square area is: {square_area}')
        # if shape == 'circle':
        #     circle_area = compute_area_circle(length)
        #     print(f'Circle area is: {circle_area:.2f}')
        if shape == 'circle' or shape == 'square':    
            compute_area(shape, length)
else:
    print('Thank you!')

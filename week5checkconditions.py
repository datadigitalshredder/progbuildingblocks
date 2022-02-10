print('week5check')
first_num = int(input('What is the first number?'))
second_num = int(input('What is the second number?'))

if first_num > second_num:
    print('The first number is greater')
else:
    print('The first number is not greater')
if first_num == second_num:
    print('The numbers are equal')
else:
    print('The numbers are not equal')
if second_num > first_num:
    print('The second number is greater')
else:
    print('The second number is not greater')

animal = input('What is your favorite animal?')
if animal.lower() == 'horse':
    print("That's my favorite animal too!")
else:
    print("That's not my favorite animal")
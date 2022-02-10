print('week7checkloops')
## Requirement 1
number = float(input('Please tyoe a positive number '))
while number < 0:
    print('Sorry, that a negative number!')
    number = float(input('Please type a positive number '))
else: 
    print(f'The number is: {number}')

# ## Requirement 2
# candy = input('May I have candy? ')
# while candy.lower() == 'no':
#     candy = input('May I have candy? ')
# if candy.lower() == 'yes':
#     print('Thank you.')
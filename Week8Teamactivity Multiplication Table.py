print('Week 8 Team activity Multiplication Table')

number = int(input('How many rows and columns do you want on your multiplication table? ')) 
number_product = number ** 2
table = number + 1
    
# # First row
# for y in range(1, table):
#     product = y
#     print(product, end=' ')

# # Second row
# for y in range(1, table):
#     product = y * 2
#     print(product, end=' ')

# # Third row
# for y in range(1, table):
#     product = y * 3
#     print(product, end=' ')

# Multiple rows at once 
# Use for loop within a for loop
# for y in range(1, table):
#     for x in range(1, table):
#         product = y * x
#         # print(product, end=' ')
#         print(product, end=' ')
# #    After printing the rows and columns in one print statement ..., end=' ', start a new print statement with print(), and pay attention to how it's indented. Indenting back or further sown affects the output.
#     print()

# # Stretch requirement 1
# for y in range(1, table):
#     for x in range(1, table):
#         product = y * x
#         # print(product, end=' ')
#         print(f'{product:3}', end=' ')
#     print()

# # Stretch requirement 2
# for y in range(1, table):
#     for x in range(1, table):
#         product = y * x
#         if number ** 2 >= 100:
#             print(f'{product:3}', end=' ')
#         else:
#             print(f'{product:2}', end=' ')    
#     print()

# Stretch requirement 3

# Using the logarithm scale, every number has a constant: 1, 2,3, etc for 10s, 100s and 1000s resp.
# So by determining the log constant for a given number and adding 1, we can know the number of digits in the number.
# We use math.log as an integer from the math library 
# Note how to use a variable as a string format specifier
import math
digits = int(math.log10(number_product)) + 1
for y in range(1, table):
    for x in range(1, table):
        product = y * x
        print(f'{product:{digits}}', end=' ')
    print()

## Stretch requirement 3 Alternative Method

## Use a while loop to count the number of digits in a number. In this case the number is product of the rows and columns inputed by the user, which is the biggest number of the multiplication table.
# count = 0
# while number_product > 0:
#     # Iterate through out the number product from zero upwards
#     count = count + 1
#     # Divide the number product by 10 and drop the remainder and then loop until remainder is smaller than zero
#     number_product = number_product // 10
## The number of iterations will be the number of digits in the number
# print(count)

# # Use loops within loops to display the product of each column and row in one print statement
# for y in range(1, table):
#     for x in range(1, table):
#         product = y * x
#         print(f'{product:{count}}', end=' ')
#     # After displaying the one print statement, start a new print statement. Take note of the indentation.
#     print()

    
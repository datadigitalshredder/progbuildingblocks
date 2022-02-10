print('Week 9 Team activity number lists')

# CORE REQUIREMENTS
numbers = []

number = ()
while number != 0:
    number = int(input('Please enter a number: '))
    if number != 0:
        numbers.append(number)
print('This is your number list:')
for i in numbers:
    print(i)

sum = sum(numbers)
average = sum / len(numbers)
largest_number = max(numbers)
smallest_number = min(numbers)
print(f'The sum is: {sum}')
print(f'The average is: {average}')
print(f'The largest number is: {largest_number}')
print(f'The smallest number is: {smallest_number}')

# #Alternative for computing the average (needs: from statistics import mean library) and median (needs: import statistics library)
import statistics
from statistics import mean
avg = mean(numbers)
median_number = statistics.median(numbers)
print()
print(avg)
print(f'The median value is: {median_number}')

# STRETCH REQUIREMENTS
# numbers = []

# number = -1
# Note: () can be used instead of -1 in line above
# while number != 0:
#     number = int(input('Please enter a number: '))
#     if number != 0:
#         numbers.append(number)
# print('This is your number list:')
# for i in numbers:
#     print(i)

# small = min([i for i in numbers if i > 0])
# print(f'The smallest positive number is: {small}')

# new_list = numbers.sort()
# print('This is the sorted list:')
# for j in numbers:
#     print(j)
    # OR another approach (Take note of the variable used in the for loop)
# new_list = sorted(numbers)
# print('This is the sorted list:')
# for j in new_list:
#     print(j) 


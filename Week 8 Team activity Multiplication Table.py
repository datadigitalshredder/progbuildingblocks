print('Week 8 Team activity Multiplication Table')

number = int(input('How many rows and columns do you want in your multiplication table? '))
table = number + 1
    
## First row
# for y in range(1, table):
#     number = y
#     print(number, end=' ')

## Second row
# for y in range(1, table):
#     number = y * 2
#     print(number, end=' ')

## Third row
# for y in range(1, table):
#     number = y * 3
#     print(number, end=' ')

## Multiple rows at once 
for y in range(1, table):
    for x in range(1, table):
        number = y * x
        print(f'{number:3}', end=' ')
    print()
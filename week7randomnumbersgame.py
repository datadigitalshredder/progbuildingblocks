print('week7randomnumbersgame')

## 1st Core Requirement
# magic_number = int(input('What is the magic number? '))
# guess = int(input('What was your guess? '))
# if guess > magic_number:
#     print('lower')
# elif guess < magic_number:
#     print('higher')
# else:
#     print('You guessed it!')

## 2nd Core requirement
# magic_number = int(input('What is the magic number? '))
# guess = int(input('What was your guess? '))
# while guess != magic_number:
#     print()
#     print("That's not the number")
    
#     if guess > magic_number:
#         print()
#         print('Lower')
#     elif guess < magic_number:
#         print()
#         print('Higher')

#     guess = int(input('What was your guess? '))
# else:
#     print()
#     print('You guessed it!')

# ## 3rd Core Requirement
# import random
# number = random.randint(1,100)
# print(number)
# guess = int(input('What was your guess? '))
# while guess != number:
#     print()
#     print("That's not the number")
    
#     if guess > number:
#         print()
#         print('Lower')
#     elif guess < number:
#         print()
#         print('Higher')

#     guess = int(input('What was your guess? '))
#     print()
#     print('You guessed it!')
    
# else:
#     print()
#     print('You guessed it times!')

## Stretch requirements
## 2nd Stretch requirement
# import random
# number = random.randint(1,100)
# print(number)
# guess = int(input('What was your guess? '))
# count = 0
# while guess != number:
#     print()
#     print("That's not the number")
    
#     if guess > number:
#         print()
#         print('Lower')
#     elif guess < number:
#         print()
#         print('Higher')

#     guess = int(input('What was your guess? '))
#     count += 1
#     print()
#     # print(f'You guessed it {count + 1} times!')

# else:
#     print()
#     print(f'You guessed it ({count + 1}) times!')

## 3rd Stretch requirement 1st Approach (Longer version of code, my own approach.)
# import random
# number = random.randint(1,100)
# ## print(number)
# guess = int(input('What was your guess? '))
# count = 0
# while guess != number:
#     print()
#     print("That's not the number")
#     if guess > number:
#         print()
#         print('Lower')
#         print(f'That was guess number: {count + 1}.')
#     elif guess < number:
#         print()
#         print('Higher')
#         print(f'That was guess number: {count + 1}.')

#     guess = int(input('What was your guess? '))
#     count += 1
#     print()

# else:
#     print()
#     print(f'You guessed it ({count + 1}) times and got it right!')
# print()
# repeat = input('Do you want to play again (Yes or No)? ')

# while repeat.lower() == 'yes':
#     print()
#     number = random.randint(1,100)
#     ## print(number)
#     guess = int(input('What was your guess? '))
#     count = 0
#     while guess != number:
#         print()
#         print("That's not the number")
    
#         if guess > number:
#             print()
#             print('Lower')
#             print(f'That was guess number: {count + 1}.')
#         elif guess < number:
#             print()
#             print('Higher')
#             print(f'That was guess number: {count + 1}.')

#         guess = int(input('What was your guess? '))
#         count += 1
#         print()
        
#     else:
#         print(f'You guessed it ({count + 1}) times and got it right!')
#         print()
#         repeat = input('Do you want to play again (Yes or No)? ') 
#         print()
# else:
#     print()
#     over = input('Game over. Press ENTER to exit.')

## 3rd Stretch Requirement 2nd Approach (Shorter version of code.)
import random
number = random.randint(1,100)
keep_playing = input('Do you want to keep playing (Yes or No)? ')
print()
while keep_playing.lower() == 'yes':
    guess = int(input('What was your guess? '))
    count = 0
    while guess != number:
        print()
        print("That's not the number")
        if guess > number:
            print()
            print('Lower')
            print(f'That was guess number: {count + 1}.')
        elif guess < number:
            print()
            print('Higher')
            print(f'That was guess number: {count + 1}.')
        guess = int(input('What was your guess? '))
        count += 1
        print()

    else:
        print()
        print(f'You guessed it ({count + 1}) times and got it right!')
        # import random
        # number = random.randint(1,100)
        keep_playing = input('Do you want to keep playing (Yes or No)? ')

else:
    print()
    over = input('Game over. Press ENTER to exit.')



print('week6teamcomplexconditions')

# Amusement Park Conditions
# The local amusement park has just installed a new ride. Because of its speed and extreme twists and turns, it has very strict requirements for the riders, especially as it pertains to children or other shorter riders.
# To help the ride attendants follow the rules, you've been asked to write an app to help them know if the riders are acceptable for the car.
# The basic rules are as follows:
# 1. No one under 36 inches may ever ride, either by themselves or with another rider.
# 2. Normally, two riders sit in the car together. A single rider can only ride if they are at least 18 years old and are at least 62 inches tall.
# 3. If there are two riders and one of them is at least 18 years old, they may ride together.

## CORE REQUIREMENTS
# Initial requirements
# age = int(input('What is the age of the first rider? '))
# height = float(input('What is the height of the first rider? '))
# second_rider = input('Is there a second rider (Yes or No)? ')

# # 1st condition
# if height < 36 or age < 18 and second_rider.lower() == 'no':
#     print()
#     print('Sorry, you may not ride')
# # 2nd condition
# elif height >= 36:
#     print() 
#     if second_rider.lower() == 'no':
#         print()
#         if age >= 18 and height >= 62:
#             print()
#             print('Welcome to the ride. Please be safe and have fun!')
#         else:
#             print()
#             print('Sorry, you may not ride')
#     elif second_rider.lower() == 'yes':
#         print()
#         age_second = int(input('What is the age of the other rider? '))
#         height_second = float(input('What is the height of the other rider? '))
#         print()
#         if height >= 36 and height_second >= 36 and (age >= 18 or age_second >= 18):
#             print('Welcome to the ride. Please be safe and have fun!')
#         else:
#             print('Sorry, you may not ride.')

# # 3rd condition 
# elif height >= 36 and second_rider.lower() == 'yes':
#     print()
#     age_other_rider = int(input('What is the age of the other rider? '))
#     height_other_rider = float(input('What is the height of the other rider? '))
#     print()
#     if height_other_rider >= 36:
#         print('Welcome to the ride. Please be safe and have fun!')
#     else:
#         print('Sorry, you may not ride.')
    
# else:
#     print('Sorry, you may not ride.')

## CORE REQUIREMENTS and STRETCH REQUIREMENTS
# CORE
# 1. No one under 36 inches may ever ride, either by themselves or with another rider.
# 2. Normally, two riders sit in the car together. A single rider can only ride if they are at least 18 years old and are at least 62 inches tall.
# 3. If there are two riders and one of them is at least 18 years old, they may ride together.
# STRETCH
# 1. If there are two riders, but neither one is at least 18 years old, they may still ride as long as they are both at least 12 years old and at least 52 inches tall.
# 2. If a person is age 12–17, ask if that person has a golden passport. If they do, they should be treated as if they were 18 years old for the sake of all rules. (Don't forget to apply this to the single rider case.)
# 3. If there are two riders, but neither one is at least 18 years old, they may still ride if one rider is at least 16 years old and the other is at least 14. (Keep in mind that the first rider may be the younger of the two or they may be the older of the two.)

## Initial requirements
# age = int(input('What is the age of the first rider? '))
# height = float(input('What is the height of the first rider? '))
# second_rider = input('Is there a second rider (Yes or No)? ')

## 1st condition (No one under 36 inches may ride, either alone or with someone.)
# if second_rider.lower() == 'no':
#     print()
#     if height < 36 and age < 18:
#         print('Sorry, you may not ride')

## Stretch requirement 2 (A rider at least 12 but less than 18 years with a golden passport. Note: this condition somewhat contradicts or nullifies rule number 2 on line 87 to 97 as it will further ask a passport before the decision.)
    # elif 18 > age >= 12 and height >= 36:
    #     print()
    #     passport = input('Do you have a golden passport (Yes or No)? ')
    #     if passport.lower() == 'yes':
    #         print()
    #         print('Welcome to to the ride, please be safe and have fun!')
    #     else:
    #         print()
    #         print('Sorry, you may not ride.')
## 2nd condition (A single rider can only ride if they are at least 18 years old and are at least 62 inches tall.)
#     elif height >= 36:
#         print() 
#         if second_rider.lower() == 'no':
#             print()
#             if age >= 18 and height >= 62:
#                 print()
#                 print('Welcome to to the ride, please be safe and have fun!')
#             else:
#                 print()
#                 print('Sorry, you may not ride.')

# elif second_rider.lower() == 'yes':
#     print()
#     age_second = int(input('What is the age of the other rider? '))
#     height_second = float(input('What is the height of the other rider? '))
#     print()
#     if height >= 36 and height_second >= 36 and (age >= 18 or age_second >= 18):
#         print()
#         print('Welcome to the ride. Please be safe and have fun!')
        ## Stretch requirement 1 (If both riders are not 18 yrs old but are at least 12 and 52 inches tall.)
    # elif 18 > age >= 12 and 18 > age_second >= 12 and height >= 52 and height_second >= 52:
    #     print()
    #     print('Welcome to the ride. Please be safe and have fun!')

    ## Stretch requirement 3 (For riders less than 18, but are at least 16 and 14 and both are 36 inches tall.)
    # elif (18 > age >= 16 or 18 > age >= 14) and (18 > age_second >= 16 or 18 > age_second >= 14):
    #     print()
    #     print('Welcome to the ride. Please be safe and have fun!')
    # else:
    #     print()
    #     print('Sorry, you may not ride.')

## 3rd condition (If there are two riders and one of them is at least 18 years old, they may ride together.)
# elif height >= 36 and second_rider.lower() == 'yes':
#     print()
#     age_other_rider = int(input('What is the age of the other rider? '))
#     height_other_rider = float(input('What is the height of the other rider? '))
#     print()
#     if height_other_rider >= 36:
#         print('Welcome to the ride. Please be safe and have fun!')
    
# else:
#     print('Sorry, you may not ride.')   

## Alternative using Boolean Variables
## CORE REQUIREMENTS and STRETCH REQUIREMENTS
# CORE
# 1. No one under 36 inches may ever ride, either by themselves or with another rider.
# 2. Normally, two riders sit in the car together. A single rider can only ride if they are at least 18 years old and are at least 62 inches tall.
# 3. If there are two riders and one of them is at least 18 years old, they may ride together.
# STRETCH
# 1. If there are two riders, but neither one is at least 18 years old, they may still ride as long as they are both at least 12 years old and at least 52 inches tall.
# 2. If a person is age 12–17, ask if that person has a golden passport. If they do, they should be treated as if they were 18 years old for the sake of all rules. (Don't forget to apply this to the single rider case.)
# 3. If there are two riders, but neither one is at least 18 years old, they may still ride if one rider is at least 16 years old and the other is at least 14. (Keep in mind that the first rider may be the younger of the two or they may be the older of the two.)

# Initial requirements
age = int(input('What is the age of the first rider? '))
height = float(input('What is the height of the first rider? '))
second_rider = input('Is there a second rider (Yes or No)? ')

# 1st condition (No one under 36 inches may ride, either alone or with someone.)
if second_rider.lower() == 'no':
    print()
    if height < 36 and age < 18:
        ride = False

# Stretch requirement 2 (A rider at least 12 but less than 18 years with a golden passport. Note: this condition somewhat contradicts or nullifies rule number 2 on line 87 to 97 as it will further ask a passport before the decision.)
    elif 18 > age >= 12 and height >= 36:
        print()
        passport = input('Do you have a golden passport (Yes or No)? ')
        if passport.lower() == 'yes':
            print()
            ride = True
        else:
            print()
            ride = False
# 2nd condition (A single rider can only ride if they are at least 18 years old and are at least 62 inches tall.)
    elif height >= 36:
        print() 
        if second_rider.lower() == 'no':
            print()
            if age >= 18 and height >= 62:
                print()
                ride = True
            else:
                print()
                ride = False

elif second_rider.lower() == 'yes':
    print()
    age_second = int(input('What is the age of the other rider? '))
    height_second = float(input('What is the height of the other rider? '))
    print()
    if height >= 36 and height_second >= 36 and (age >= 18 or age_second >= 18):
        print()
        ride = True
        # Stretch requirement 1 (If both riders are not 18 yrs old but are at least 12 and 52 inches tall.)
    elif 18 > age >= 12 and 18 > age_second >= 12 and height >= 52 and height_second >= 52:
        print()
        ride = True

    # Stretch requirement 3 (For riders less than 18, but are at least 16 and 14 and both are 36 inches tall.)
    elif (18 > age >= 16 or 18 > age >= 14) and (18 > age_second >= 16 or 18 > age_second >= 14):
        print()
        ride = True
    else:
        print()
        ride = False

# 3rd condition (If there are two riders and one of them is at least 18 years old, they may ride together.)
elif height >= 36 and second_rider.lower() == 'yes':
    print()
    age_other_rider = int(input('What is the age of the other rider? '))
    height_other_rider = float(input('What is the height of the other rider? '))
    print()
    if height_other_rider >= 36:
        ride = True
    
else:
    ride = False      

if ride:
    print('Welcome to the ride. Please be safe and have fun!')
else:
    print('Sorry, you may not ride.')

## Test the above requirements using:
## CORE
## 1. Age is 12, height is 46, No second rider, and(No golden passport): Output is can't ride
## 2. Age 82, height 75, Second rider is available aged 14 and height is 35: Output is can't ride
## 3. Age 82, height 75, Second rider is available aged 14 and height is 36: Output is can ride
## 4. Age 82, height 75, NO second rider: Output is can ride
## STRETCH
## 1. Age is at least 12 and not 18 for both riders and both are at least 52inch tall: Output is can ride
## 2. A single rider at least 12 but less than 18 and at least 36 inches tall with a golden passport: Output is can ride
## 3. Two riders who are at least 14 but less than 18 and are 36 inches tall: Output is can ride 

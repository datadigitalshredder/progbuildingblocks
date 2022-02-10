print('week5teamactivity')
# grade = float(input('What is you your grade percentage?'))

# if grade >= 90:
#     print('A')
# elif grade >= 80:
#     print('B')
# elif grade >= 70:
#     print('C')
# elif grade >= 60:
#     print('D')
# else:
#     print('F')

# core requirement 2
# grade = float(input('What is your grade percentage?'))
# if grade >= 70:
#     actual_grade = input('What is your grade?')
#     if actual_grade in('A','B','C'):
#         print('Congratulations, you passed the test. Keep up the good work!')
#     else:
#         print('You did not quite make it. Do not worry, keep trying!')
# else:
#     print('You did not quite make it. Do not worry, keep trying!')

# core requirement 3
# letter = float(input('What is your grade percentage?'))
# if letter >= 90:
#     letter = 'A'      
# elif letter >= 80:
#     letter = 'B'
# elif letter >=70:
#     letter = 'C'
# elif letter >=60:
#     letter = 'D'
# else:
#     letter = 'F'
# # print(letter)
# # or 
# output = f'Your letter grade is {letter}.'
# print(output)
 
#Stretch requirement 1
# letter = float(input('What is your grade percentage?'))
# if letter >= 90:
#     letter_weight = int(input('What is the letter weight marker? Note: >= 7 is + and <3 is -'))
#     if letter_weight >= 7:
#         letter = 'A+'
#     elif letter_weight < 3:
#         letter = 'A-'
#     else:
#         letter = 'A'

# elif letter >= 80:
#     letter_weight = int(input('What is the letter weight marker? Note: >= 7 is + and <3 is -'))
#     if letter_weight >= 7:
#         letter = 'B+'
#     elif letter_weight < 3:
#         letter = 'B-'
#     else:
#         letter = 'B'   

# elif letter >= 70:
#     letter_weight = int(input('What is the letter weight marker? Note: >= 7 is + and <3 is -'))
#     if letter_weight >= 7:
#         letter = 'C+'
#     elif letter_weight < 3:
#         letter = 'C-'
#     else:
#         letter = 'C' 

# elif letter >= 60:
#     letter_weight = int(input('What is the letter weight marker? Note: >= 7 is + and <3 is -'))
#     if letter_weight >= 7:
#         letter = 'D+'
#     elif letter_weight < 3:
#         letter = 'D-'
#     else:
#         letter = 'D'   
# else:
#     letter_weight = int(input('What is the letter weight marker? Note: >= 7 is + and <3 is -'))
#     if letter_weight >= 7:
#         letter = 'F+'
#     elif letter_weight < 3:
#         letter = 'F-'
#     else:
#         letter = 'F'
# # print(letter)
# # or 
# output = f'Your letter grade is {letter}.'
# print(output)

#Stretch requirement 1 (alternative method)
# letter = float(input('What is your grade percentage?'))
# if letter >= 90:
#     letter_weight = letter % 10
#     if letter_weight >= 7:
#         letter = 'A+'
#     elif letter_weight < 3:
#         letter = 'A-'
#     else:
#         letter = 'A'

# elif letter >= 80:
#     letter_weight = letter % 10
#     if letter_weight >= 7:
#         letter = 'B+'
#     elif letter_weight < 3:
#         letter = 'B-'
#     else:
#         letter = 'B'   

# elif letter >= 70:
#     letter_weight = letter % 10
#     if letter_weight >= 7:
#         letter = 'C+'
#     elif letter_weight < 3:
#         letter = 'C-'
#     else:
#         letter = 'C' 

# elif letter >= 60:
#     letter_weight = letter % 10
#     if letter_weight >= 7:
#         letter = 'D+'
#     elif letter_weight < 3:
#         letter = 'D-'
#     else:
#         letter = 'D' 
    
# else:
#     letter_weight = letter % 10
#     if letter_weight >= 7:
#         letter = 'F+'
#     elif letter_weight < 3:
#         letter = 'F-'
#     else:
#         letter = 'F'

# Stretch requirement 2 (No grade A+, only A and A-)
# letter = float(input('What is your grade percentage?'))
# if letter >= 90:
#     letter_weight = letter % 10
#     if letter_weight >= 7:
#         letter = 'A'
#     else:
#         letter = 'A-'

# elif letter >= 80:
#     letter_weight = letter % 10
#     if letter_weight >= 7:
#         letter = 'B+'
#     elif letter_weight < 3:
#         letter = 'B-'
#     else:
#         letter = 'B'   

# elif letter >= 70:
#     letter_weight = letter % 10
#     if letter_weight >= 7:
#         letter = 'C+'
#     elif letter_weight < 3:
#         letter = 'C-'
#     else:
#         letter = 'C' 

# elif letter >= 60:
#     letter_weight = letter % 10
#     if letter_weight >= 7:
#         letter = 'D+'
#     elif letter_weight < 3:
#         letter = 'D-'
#     else:
#         letter = 'D' 
    
# else:
#     letter_weight = letter % 10
#     if letter_weight >= 7:
#         letter = 'F+'
#     elif letter_weight < 3:
#         letter = 'F-'
#     else:
#         letter = 'F'

# Stretch requirement 3 (No grade F+ or F-, only F)
letter = float(input('What is your grade percentage?'))
if letter >= 90:
    letter_weight = letter % 10
    if letter_weight >= 7:
        letter = 'A'
    else:
        letter = 'A-'

elif letter >= 80:
    letter_weight = letter % 10
    if letter_weight >= 7:
        letter = 'B+'
    elif letter_weight < 3:
        letter = 'B-'
    else:
        letter = 'B'   

elif letter >= 70:
    letter_weight = letter % 10
    if letter_weight >= 7:
        letter = 'C+'
    elif letter_weight < 3:
        letter = 'C-'
    else:
        letter = 'C' 

elif letter >= 60:
    letter_weight = letter % 10
    if letter_weight >= 7:
        letter = 'D+'
    elif letter_weight < 3:
        letter = 'D-'
    else:
        letter = 'D' 
    
else:
    letter = 'F'
# print(letter)
# or 
output = f'Your letter grade is {letter}.'
print(output)
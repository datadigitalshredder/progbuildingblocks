print('week two activity')
line = input('Please enter 30 dashes')
first = input('What is your first name?')
last = input('What is your last name?')
email = input('What is your email address?')
phone = input('What is your phone number?')
job = input('What is your job title?')
ID = input('What is your ID number?')
hair = input('What color is your hair?')
eyes = input('What color are your eyes?')
month = input('Which month did you start the training?')
completion = input('Did you finish the training?')
line = input('Please enter 30 dashes')
# output = f'Hello THERE! \n The ID card is: \n{line} \n{last.upper()}, {first.capitalize()} \n{job.title()} \n{ID.upper()} \n\n{email.lower()} \n{phone.lower()} \n\nHair: {hair.capitalize():30} Eyes: {eyes.capitalize()} \nMonth: {month.capitalize():29} Training: {completion.capitalize()} \n{line}'
output = f'Hello THERE! \n The ID card is: \n{line} \n{last.upper()}, {first.capitalize()} \n{job.title()} \n{ID.upper()} \n\n{email.lower()} \n{phone.lower()} \n\nHair: {hair.capitalize()} \tEyes: {eyes.capitalize()} \nMonth: {month.capitalize()} \tTraining: {completion.capitalize()} \n{line}'
print(output)

print('Week 13 Check Functions')

# def display_regular(display_style, force_uppercase = True):
#     if force_uppercase:
#         display = display_style.upper()
#     elif force_uppercase:
#         display = display_style.lowercase()
#     else:
#         display = display_style
#     return display

# message = input('Please enter a message: ')
# message_style = display_regular(message)
# message_style2 = display_regular(message, False)
# message_style3 = display_regular(message, True)

# print(message_style)
# print(message_style2)
# print(message_style3)

# Function for regular case
def display_regular(display_style):
    display = display_style.title()
    return display

# Function for uppercase
def display_uppercase(display_style):
    display = display_style.upper()
    return display

# Function for lowercase
def display_lowercase(display_style):
    display = display_style.lower()
    return display

message = input('Please enter a message: ')
message_style = display_regular(message)
message_style2 = display_uppercase(message)
message_style3 = display_lowercase(message)

print(message_style)
print(message_style2)
print(message_style3)



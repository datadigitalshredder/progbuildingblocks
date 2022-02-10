print('Week 9 Checkpoint')

# This did not work because variable name in print function is not correct
# your_friends = []
# friends = ''
# if friends != 'end':
#     friends = True
# while friends != 'end':
#     friends = input('What is the name of your friends? ')
#     if friends == 'end':
#         print()
#     else:
#         your_friends.append(friends)

# for friend in your_friends:
#     if friends:
#         # print(f'This is your friend list: \n {your_friends}', end=' ')
#         # print(f'This is your friend list: \n {your_friends}')
#         print(your_friends)
#     # else:
#     #     print()

# This worked
your_friends = []
friends = ''
while friends != 'end':
    friends = input('What is the name of your friend? ')
    if friends != 'end':
        your_friends.append(friends) 
print('This is your friends list:')      
for friend in your_friends:
        print(friend)


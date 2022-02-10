print('tests')
# x = 6
# y = 6
# if x == 5:
#     print('a')
#     if y == 6:
#         print('b')
# else:
#     print('c')
# if y == 6:
#     print('d')

# def dot_aligned(seq):
#     snums = [str(n) for n in seq]
#     dots = [s.find('.') for s in snums]
#     m = max(dots)
#     return [' '*(m - d) + s for s, d in zip(snums, dots)]

# nums = [400000000.8, 49.723, 456.781, -72.18]

# for s in dot_aligned(nums):
#     print(s)

#for loops
# for index in range(0,2):
#     print(index)
# for name in ['Christopher','Susan','Innocent']:
#     print(name)

# people = ['Innocent','Hove','Henry']

# for loop and while loop compared
# for name in people:
#     print(name)

# name = 0
# while name < len(people):
#     print(people[name])
#     name = name + 1

# print('Finished with loop')

# Adventure Game Markham Abor
# answer = input('You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. Which one do you want to pick up?')
# #Path 1.1
# if answer.upper() == 'MATCH':
#     answer = input('You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out. Do you want to RUN, or HIDE behind a tree? ')
#     if answer.upper() == 'RUN':
#        answer = input('As you ran, the large grizzly bear heard your footsteps and chased you. While running you saw an unfamiliar light in the forest. Do you want to RUN TOWARDS the light or CONTINUE RUNNING in the dark forest? ')
#        if answer.upper() == 'RUN TOWARDS':
#              print ('You saw the scout outside his cabin and he was able to save you from danger. Congratulations! You are now Safe! ')
#        elif answer.upper() == 'CONTINUE RUNNING':
#              answer = input('The grizzly bear stops chasing you and you are in the deeper part of the forest. Do you want to go back YES or NO?') 
#              if answer.upper() == 'YES':
#                 print("After walking for less than 30 minutes you've seen the light you've ignored while you were escaping from the grizzly bear. You saw the scout outside his cabin and he was able to help you. Congratulations! You are now Safe! ")
#              elif answer.upper() == 'NO':
#                 print("You went to the deeper part of the forest therefore you're lost. Better luck next time.")
#              else:
#                 print('You can only answer YES or NO.')
#        else:
#              print('You can only answer RUN TOWARDS or CONTINUE RUNNING.')
# # Path 1.2             
#     elif answer.upper() == 'HIDE':
#        answer = input("You moved discreetly behind the tree and the bear went to where it saw the light, you tried to calm and control your breathing so the bear won't notice where you've hid. After a few minutes the grizzly bear left. Do you want to STAY HIDDEN or START WALKING slowly? ")
#        if answer.upper() == 'STAY HIDDEN':
#           answer = input('You stayed behind the tree for about 30 minutes in order to make sure the bear was gone or asleep. Then you start walking slowly away from the bear. While walking you have noticed the flashlight beside you. Do you want to grab the flashlight YES or NO?')
#           if answer.upper() == 'YES':
#              print('You have grabbed and used the flashlight. While walking in the forest you saw the path leading to your campsite. You were able to meet your friends and share to them your experience. Congratulations! You are now Safe!')
#           elif answer.upper() == 'NO':
#              print('You are walking in the forest without light. Luckily, your friends have flashlights and they are finding you. Congratulations! You are now Safe!')
#           else:
#              print('You can only answer YES or NO.')
#        elif answer.upper() == 'START WALKING':
#             print("You immediately start walking slowly away from the area where the bear is located. While walking you've noticed that you're walking in a west direction. You remember that there is a beautiful lake there with a small village. You immediately went to the nearest house and asked for help. Congratulations! You are now Safe!")
#        else:
#             print('You can only answer STAY HIDDEN or START WALKING')
#     else:
#        print('You can only answer RUN or HIDE.')
# #Path 2.1
# elif answer.upper() == 'FLASHLIGHT':
#     answer = input('You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side. Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise? ')
#     if answer.upper() == 'FOLLOW':
#        answer = input('You followed the path and saw a crossroad, Left path leads you to a highway while the right path leads you to an unknown location. Which way will you choose, LEFT or RIGHT? ')
#        if answer.upper() == 'LEFT':
#           answer = input('You are now at the highway, you see a lot of cars. Do you want to WAVE and ask for help or CONTINUE WALKING on the highway. ')
#           if answer.upper() == 'WAVE':
#              print('You wave to a lot of upcoming cars on the highway. After a few seconds someone stopped their car and asked about your situation and you told him everything that happened. He was able to help you and you are now safe. Congratulations! You are now Safe!')
#           elif answer.upper() == 'CONTINUE WALKING':
#              print("After a few hours of walking a police officer noticed you and asked you if you're okay. You told them everything and you want to get home. The cops were able to help you. Congratulations! You are now Safe!")
#           else:
#              print('You can only answer WAVE or CONTINUE WALKING. ')
#        elif answer.upper() == 'RIGHT':
#             print("The path leads to the mountains. You decided to check the area and saw students who are watching the stars through their telescope. The students invited you and you decided to stay and enjoy God's creation. Congratulations! ")
#        else:
#           print('You can only answer LEFT or RIGHT. ')
#  #Path 2.2         
#     elif answer.upper() == 'LOOK':
#          answer = input ("As you looked at the trees you saw the grizzly bear because of the little noise that you've made the bear started to charge towards you. Do you want to PLAY DEAD or MAKE A STAND? ")
#          if answer.upper() == 'PLAY DEAD':
#             answer = input("You started to play dead. The bear started to check you out. It started to make contact with you. then after a few minutes it starts leaving the area. While playing dead, you've realized that you have your phone in your packet. Do you want to USE THE FLASHLIGHT and start walking or USE THE PHONE? ")
#             if answer.upper() == 'USE THE FLASHLIGHT':
#                 print("You started walking and saw a path after an hour of walking you saw a river and a group of people camping. You asked for help and they immediately contacted the authorities. Congratulations! You are now Safe! ")
#             elif answer == 'USE THE PHONE':
#                   print('After what happened you immediately contact 911 they immediately send a group of rangers to help and after a few hours they were able to save you. Congratulations! You are now Safe!')
#             else:
#                print('You can only answer USE THE FLASHLIGHT or USE THE PHONE.')
#          elif answer.upper() == 'MAKE A STAND':
#                answer = input("You started to compose yourself and make a stand while the bear is charging towards you. The bear stops and you start talking in a soft monotone voice to ease the bear's aggression and try to let the bear know that\n you are a human by waving to it. The bear's aggression started to ease and it walked away. After what happened you found yourself on a weird path. Do you want to continue YES or NO? ")
#                if answer.upper() == 'YES':
#                   print('After walking for a while you saw an old cabin in the woods. You started walking towards the door and opened it. You saw a young man with a bloody knife and he immediately ran towards you. You got stabbed. YOU DIED.')
#                elif answer.upper() == 'NO':
#                   print('You started to look at the stars and saw an abnormal change in the sky. A black saucer appeared and you saw an alien in front of you. They took you away. YOU ARE NOW GONE...NO ONE KNOW WHERE YOU ARE...')
#                else:
#                   print('You can only answer YES or NO.')
#          else:
#             print('You can only answer PLAY DEAD or MAKE A STAND.')
#     else:
#        print('You can only answer FOLLOW or LOOK. ')
# else:
#    print('You can only answer MATCH or FLASHLIGHT.') 

## Adventure game Camelle
#text base adventure game
# 'THE MYSTERIOUS ISLAND'
# by: Camelle Claro
# filename: adventure.py
# '''
# ​
# print () #this is a blank line
# import time
# ​
# print ('The Mysterious Island \nA text based adventure made by Camelle Claro \n\n
# ***Intruction: choices are printed in CAPITAL LETTERS***')#game title
# ​
# print () #this is a blank line
# ​
# start = input('Would you like to start?\n YES or NO\n')
# ​
# def start_game (): #function to start the game
#     if start.lower() == 'yes':
#         print ('\n...game starting...')
#         time.sleep(3)
#         shore()
#     elif start.lower() == 'no':
#         exit = input ('Do you want to exit the game? \n YES or NO \n>>> ')
#         if exit.lower() == 'yes':
#             print ('We are sad to let you go. Goodbye.')
#         elif exit.lower() =='no':
#             print ('\n...game starting...')
#             time.sleep(3)
#             shore()
#         else:
#             print ('Error. Please restart the game.')
#     else:
#         time.sleep (2)
#         print ('Error. Please restart the game.')
# ​
# #play again function
# def play_again(): #play again function
#   answer = input("\nDo you want to play again?\n YES or NO\n>>>")
#   if answer.lower() == 'yes':
#     start_game()
#   else:
#     exit()
# ​
# #level 1
# def shore():
#     name = input ('\n    Welcome to the Mysterious Island! What is your name? \n>>> ')
#     time.sleep (2)
#     print (f'    Welcome to the Mysterious Island, {name.capitalize()}! Explore the island and find out the mystery behind it. \n...game loading...')
#     time.sleep (3)
#     choice_1 = input(f'''\n    {name.capitalize()}, you are standing in the middle of the sea shore. 
#     There are three separate ways in front of you to explore the island. Please choose which way to go: STRAIGHT AHEAD to go to the ruins, 
#     go LEFT to explore the cave, or go RIGHT to explore the forest? \n>>> ''')
#     if choice_1.lower () == 'straight ahead':
#         time.sleep(2)
#         ruins ()
#     elif choice_1.lower () == 'left':
#         time.sleep(2)
#         cave ()
#     elif choice_1.lower () == 'right':
#         time.sleep(2)
#         forest ()
#     else:
#         print ('GAME OVER\nYou didn\'t move. Ancient spirits took you away and now you\'re gone.')
#         play_again ()
# ​
# #level 2
# def ruins (): #the straight path
#     ruins_choice = input ('''\n    You went straight ahead to the ruins. You saw ancient dilapidated buildings.
#     Rumors say that in these ruins dwells unwary souls, once you go in you'll never go back alive.
#     As you roam around in search of something unusual, you saw a crying child hiding inside the corner of a building. 
#     Are you going to IGNORE the child or REACH OUT to know the mystery behind the ruins?\n    >>> ''')
#     if ruins_choice.lower () == 'ignore':
#         time.sleep(2)
#         print ('''\n    The goddess of the ruins imposed as the child. She\'s looking for a kind-hearted soul to bless with abundance.
#         You ignored her so she turns you into a spirit. The reason why adventurers never came back was because of their worldly pursuit
#         for precious antiques ignoring her call for help.\n GAME OVER''')
#         play_again ()
#     elif ruins_choice.lower () == 'reach out':
#         time.sleep(2)
#         blessing ()
#     else:
#         print ('GAME OVER\nThe ancient spirits took you away and now you\'re gone.')
#         play_again ()
# ​
# def cave (): #left path
#     cave_choice = input('''\n    You went to your left and started exploring the mouth of the cave. You then saw a match and an oil lamp. 
#     Before exploring deeper into the cave, you decided to make use of the match to light the oil lamp. With the oil lamp in your hand,
#     you started walking inside the cave until pure darkness surrounds you. As you walk deeper inside the cave, you hear a loud groan a
#     few meters away from where you are standing at. You remembered about the rumors of the cave, some say that inside the cave dwells 
#     angry ancient souls. Are you going to LOOK where the sound comes from or RUN towards the entrance of the cave?\n    >>>''')
#     if cave_choice.lower() == 'look':
#         time.sleep(2)
#         look()
#     elif cave_choice.lower() == 'run':
#         time.sleep(2)
#         print ('''\n    The wounded dragon noticed you. The dragon wanted to ask for help but he accidentally breathed flames. 
#         You are burned to death.
        
#         GAME OVER\n ''')
#         play_again()
#     else:
#         print('GAME OVER\nThe darkness surrounded you. The ancient spirits possessed your body.')
#         play_again()
# ​
# def forest (): #right path
#     forest_choice = input('''\n    You went to your right and started exploring the forest. Big and enormous are the trees in the forest.
#     As you walk in amazement to the trees that surround you, you've stepped into a quicksand. You remembered the rumors about an enchanted forest
#     in the mysterious island where witches dwell. You freaked out as your body sinks in the clay. Are you going to scream for HELP or SINK to death? \n>>> ''')
#     if forest_choice.lower() == 'help':
#         time.sleep(2)
#         help ()
#     elif forest_choice.lower() == 'sink':
#         time.sleep(2)
#         print('\nGAME OVER\nYou let yourself sink in the clay which causes your death.')
#         play_again()
#     else:
#         print('\nGAME OVER\nYou let your fear control you. You died.')
#         play_again()
# ​
# ​
# ​
# #level 3
# ​
# #the ruins continuation
# def blessing():
#     blessing_choice = input('''\n    Even though confused about why a lone child is here, you approached her and reached out. You asked her what's wrong and the reason why she's crying.
#     You saw that her knees were bruised and you treated it. After treating the child's bruise, she transformed into her original form.
#     She's the goddess in the ruins and she wants to bless you with wealth because of your kindness. Do you ACCEPT it or REJECT it?\n    >>> ''')
#     if blessing_choice.lower() == 'accept':
#         time.sleep(2)
#         print('''\n    The goddess of the ruins imposed as the child. She\'s looking for a kind-hearted soul to bless with abundance.
#         She punishes those who are only after the treasures neglecting the call to help.
#         The goddess gave you a treasure chest and you solved the mystery behind the ruins.
        
#         Congratulations! You won the game.''')
#         play_again()
#     elif blessing_choice.lower() == 'reject':
#         time.sleep(2)
#         print('''\n    The goddess were moved because of your kindness. She insisted to bless you with protection and friendship.
        
#         Congratulations! You won the game and you solved the mystery.''')
#         play_again()
#     else:
#         print('''\n    Congratulations! You still solved the mystery.''')
#         play_again()
# ​
# #the cave continuation
# def look():
#     look_choice = input('''\n    As you draw closer, you noticed blood trails and feet with scales. Bravely, you looked up and found a dragon groaning in pain.
#     His body is wounded. You calmly talked to the dragon that you mean no harm so he let you treat his wound. The dragon felt better because of what you did.
#     The dragon then turned into a Guardian. He is the Guardian of the cave. He thanked you and let you choose a reward: FRIENDSHIP or a precious GEM. What will you choose?
#         >>>  ''')
#     if look_choice.lower() == 'friendship':
#         time.sleep(2)
#         print ('''\n    You became friends with the Guardian. Everything that he have is also yours.
        
#         Congratulations! You've got a friend and you solved the mystery.''')
#         play_again()
#     elif look_choice.lower() == 'gem':
#         time.sleep(2)
#         print('''\n    The guardian gave you the precious gem. He turned into a dragon then ate you.
#         When you help, don't expect anything in return.
        
#         GAME OVER''')
#         play_again()
#     else:
#         print('\nCongratulations! You are really kind. You won the game!')
#         play_again()
# ​
# #the forest continuation
# def help():
#     help_choice = input('''\n    The fairies and gnomes in the forest saw you and aided you into safety. 
#     Turns out, they are the guardians of the forest. You conversed with the fairies and gnomes. 
#     You've learned that they are kind and because of their kindness, earlier adventurers took advantage of it 
#     and captured some of them to sell. Now, you wonder why they helped you.
#     You either ASK them to know the answer or bid GOODBYE.\n    >>> ''')
#     if help_choice.lower () == 'ask':
#         time.sleep(2)
#         print('''\n    They told you that they believed in you that you won't betray their trust. You are moved with their trust in you and
#         brushed off all the ill intentions that you have. You decided to help them find the captured fairies. 
#         They blessed you with guidance.
        
#         Congratulations! You have earned their trust and learned the reality of the enchanted forest.''')
#         play_again()
#     elif help_choice.lower () == 'goodbye':
#         time.sleep(2)
#         print('''\n    They turned you into a frog because you forgot to thank them.
        
#         GAME OVER!''')
#         play_again()
#     else:
#         print('''\n    You disappeared.
        
#         GAME OVER!''')
#         play_again()
# ​
# start_game ()


# num =  int(input('Enter a number greater than or equal to 0: '))
# while num <0:
#     print("Sorry, that is a negative number. Please try again.")
#     num = int(input('Enter a number greater than or equal to 0: '))

## Weylin Douglas question
# if num >= 0:
#     print('nice number')
#     drinks = int(input('Enter the number of drinks: '))
#     while drinks < 0:
#         print("Sorry, that is a negative number. Please try again.")
#         drinks = int(input('Enter the number of drinks: '))
               
#     if drinks >= 0:
#         print('Enjoy rest of game.')

## Hayden Murphy question 
# import random
# output = random.randint(1,20)
# if output >= 11:
#     print('you failed')
#     pass_fail = True
# else:
#     print('you passed')
#     pass_fail = False

# layer_1 = int(input('1 or 2 '))
# if layer_1 == 1:
#     print('roll for stealth')
#     if pass_fail:
#         print('Success you rolled a'  +  str(output))
#     else:
#         print('Failure you rolled a'  +  str(output))

## Week 7 Check understanding
# animal = "rabbit"
# while animal == "dog":
#    print("a")
#    animal = "cat"
#    print("b")
# print("c")

# animal = "dog"
# while animal == "dog":
#    print("a")
#    animal = "cat"
#    print("b")
# print("c")

# animal = "dog"
# while animal != "dog":
#    print("a")
#    animal = "cat"
#    print("b")
# print("c")
        
# value = 10
# while value < 20:
#    value = value + 1
# print(value)

# while value < 20:
#    value = value + 1
# print(value)

# value = 20
# while value < 20:
#    value = value + 1
# print(value)

# Vadim game code
# import random

# number_magic = random.randint(1, 20)
# number_track = ""
# answer = 'yes'
# # number_magic = int(input('What is the magic number? '))
# while answer.lower() == 'yes':
#     number_track = 0
#     number_user = -1
#     while number_user != number_magic:
#         number_track = number_track+1
#         number_user = int(input('What is your guess? '))
#         if number_user > number_magic:
#             print('Lower')
#         elif number_user < number_magic:
#             print('Higher')
#         else:
#             print(f'You guessed it in {number_track} times!')
    
#     answer = input('Do you want to play again (yes/no)? ')
# print('Have a nice day!')

# Week 9 Check Understanding
# x = 5

# x + 1

# print(x)

# x = 5

# x =+ 1

# print(x)

# x = 5

# x += 4

# print(x)

# x = 5

# x += 1

# print(x)

# names = ['inno', 'tracey', 'jordan', 'jared']
# print(names[1])

# my_list = [1, 2, 4, 5]
# largest = 0

# for value in my_list:

#     if value > largest:

#         largest = value

# print(f"The largest is {largest}")

# smallest = 999999999999999999

# for value in my_list:

#     if value < smallest:

#         smallest = value

# print(f"The smallest is {smallest}")

# x = -1 + 1
# print(x)

# x = 3
# if x > -1 and x >= 4:
#     print('ok')

# add = input('What item would you like to add? ')

# print(len(add))

# sentence = "\t---

# colors = 'red green yellow blue'
# color = colors.split()
# print(color)
# for col in color:
#     print(col)

# import csv
# csv_file = open("life-expectancy.csv")
# recepten = csv.reader(csv_file)

# for line in recepten:
#     for item in line:
#         x = item.split(",")
#         for a in item:
#            float(a)
# print(x)
# csv_file.close()

# shopping_c

# lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# indices = [0, 2, 5]

# # Method: Using list comprehension
# removed = [lst[i] for i in range(len(lst)) if i not in indices]

# # Method: Using pop()
# for i in sorted(indices, reverse=True):
#     lst.pop(i)

# # Result
# print(removed)
# # [1, 3, 4, 6, 7, 8, 9]

# print(lst)
# # [1, 3, 4, 6, 7, 8, 9]

# Week 13 Check Understanding
# def display_numbers(x, y):

#     print(x)
# display_numbers(3, 3)

# def display_numbers(x, y):

#     print(x)
# display_numbers(3, 4)

# def display_numbers(x, y):

#     print(x)
# display_numbers(4, 3)

# def display_numbers(x, y):
#     print(x)

# x = 3
# y = 4

# display_numbers(x, y)

# def display_numbers(x, y):

#     print(x)

# x = 3

# y = 4

# display_numbers(y, x)

# def display_numbers(x, y):

#     x = 10

# x = 3

# y = 4

# display_numbers(x, y)

# print(x)

# def display_numbers(x, y):

#     x = 10

# x = 3

# y = 4

# print(display_numbers(x, y))

def display_numbers(x, y):
    return 10

x = 3
y = 4
x = display_numbers(x, y)

print(x)
print('Adventure Game \n\nBy Innocent Hove')

## Introduction of the adventure game
print('This is the game: \n\nYour are walking through a shopping mall and you see these shop logos: KFC, MCDONALDS, and ADIDAS. \n\nINSTRUCTIONS: Select answers from the provided options (in ALL CAPS) stated in the questions. ')
keep_playing = input('Would you like to keep playing (YES or NO)? ')
## Loop 1
while keep_playing.lower() =='yes':
    print()
    start = input('\n\nWould you enter any one shop (YES or NO)? ')

    ## Loop 2
    while start.lower() == 'no':
        print("\n\nPlease pick a shop, you don't want to miss on the fun, and don't worry today is not a Sabbath!")
        start = input('Would you enter any one shop (YES or NO)? ')

    # Level 1.1.0
    if start.lower() == 'yes':
        shop = input('\n\nWhich shop would you enter amongst KFC, MCDONALDS, and ADIDAS? ')
    else:
        
        print("\n\nYou don't want to miss on the fun, just give it a try!")
        print()
        shop = input('\n\nWhich shop would you enter amongst KFC, MCDONALDS, and ADIDAS? ')
    # Level 1.1.1
    if shop.lower() in('kfc','mcdonalds','adidas'):
        print('\n\nGame on! Get ready to start.')
        # Complex conditions/ decisions
        if start.lower() == 'yes' and (shop.lower() == 'kfc' or shop.lower() == 'mcdonalds' or shop.lower() == 'adidas'):
        # Boolean variables
            game_on = True
        else:
            game_on = False
        if game_on:
            print("Also, explore what happens if you enter an answer different from the options provided. \n\nNote there are some trick questions. \n\nYou're ready to start. Have fun!")
        else:
            print('\n\nYou needed to pick one of the shops after agreeing to enter one of the shops. Sorry, GAME OVER.')
        
        # if play_again:
        #     start = input('\n\nWould you enter any one shop (YES or NO)? ')
        # else:
        #     print('Game over, thank you for playing. Press ENTER to exist!')
    if shop.lower() == 'kfc':
        print('\n\nUpon entering Kfc you learn that they have two specials on offer, one is CHEAPER than the OTHER. Excited about the offers you dash to make your order without what the two meals are.')
    # Level 1.1.2
        kfc = input('Which meal will you take, CHEAPER or OTHER? ')
        if kfc.lower() == 'cheaper':
            print('\n\nWhen your place your perceived best DEAL, based on cost effectiveness, the cashier confirms your by repeating "Your order sir is a bucket of chicken wings". You realise, you are fed up with wings and need a DIFFERENT meal for a change.')
            order = input("It's not your favorite. Do you continue to place an order for the cheaper DEAL or you give it a try for something DIFFERENT? ")
    # Level 1.1.3
            if order.lower() == 'deal':
                print('\n\nAfter placing your order you wait to enjoy your meal. Something frustrating occurs and you overhear the chef say to the cahier are out of the ingredients for that order and you gonna have to wait and hour before the get the ingredients.')
                decision = input('Do you WAIT for the ingredients or your PROCEED to order the other more expensive deal? ')
    # Level 1.1.4
                if decision.lower() == 'wait':
                    print('\n\nAfter only waiting 20 minutes, your hear the cashier call your order number and you learn that the delivery truck with the ingredients was just around the corner to make the delivery. You learn that patience pays and you enjoy your meal!')
                    print()
                    play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                    if play_again.lower() == 'yes':
                        play_again = True
                    else:
                        play_again = False
                    if play_again:
                        keep_playing = input('Would you like to keep playing (YES or NO)? ')
                    else:
                        print()
                        print('Game over, thanks for playing. ')
                        exit = input('Type YES to exit! ')
                elif decision.lower() == 'proceed':
                    print('\n\nWhen you proceed to the more expensive deal, you realize you do not have enough cash and your credit is not working either. "Ohh, I should have just been patient!", you say.')
                    play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                    
                    if play_again:
                        keep_playing = input('Would you like to keep playing (YES or NO)? ')
                    else:
                        print('Game over, thanks for playing. ')
                        exit = input('Press ENTER to exit! ')
                else:
                    print('\n\nThe more you draw closer to placing the order, the more you need to follow instructions otherwise you miss your meal.')
                    play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                    
                    if play_again:
                        keep_playing = input('Would you like to keep playing (YES or NO)? ')
                    else:
                        print('Game over, thanks for playing. ')
                        exit = input('Press ENTER to exit! ')
            elif order.lower() == 'different':
                print('\n\nThe different deal is obviously the best because you can see other people collect their orders almost instantly. That leaves you no choice but to go for it!.')
                payment = input('Are you gonna pay with CASH or use your credit CARD? ')
                if payment.lower() == 'cash':
                    print('\n\nWala! You have enough cash. Order is confirmed')
                    play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                    
                    if play_again:
                        keep_playing = input('Would you like to keep playing (YES or NO)? ')
                    else:
                        print('Game over, thanks for playing. ')
                        exit = input('Press ENTER to exit! ')
                elif payment.lower() == 'card':
                    print('\n\nSorry! You credit card is not working. Looks like you will skip this one.')
                    play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                    
                    if play_again:
                        keep_playing = input('Would you like to keep playing (YES or NO)? ')
                    else:
                        print('Game over, thanks for playing. ')
                        exit = input('Press ENTER to exit! ')
                else:
                    print('\n\nSorry! Only cash or credit payments are available in this shop.')
                    play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                    if play_again:
                        keep_playing = input('Would you like to keep playing (YES or NO)? ')
                    else:
                        print('Game over, thanks for playing. ')
                        exit = input('Press ENTER to exit! ')
            else:
                print('\n\nThe other meals include chicken combos, family meals, kids meals, and sandwiches. Unfortunately, these are beyond the scope of the game and it looks like you are going to starve.')
        elif kfc.lower() == 'other':
            print('\n\nThe other deal is not your favorite. Then what?')
            next = input('Do you CONTINUE with that or WALK to next shop? ')
            if next.lower() == 'continue':
                print('\n\nYour order is ready and because you are famished, you can not wait to have your first bite. After a few bites you feel sick and you rush to the nearest emergency room and regret falling for the deal.')
                play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                if play_again:
                    keep_playing = input('Would you like to keep playing (YES or NO)? ')
                else:
                    print('Game over, thanks for playing. ')
                    exit = input('Press ENTER to exit! ')
            elif next.lower() == 'walk':
                print('\n\nYou walk to the next shop (your favorite fast food shop) wondering if there would be any deals on promotion. Upon entering the next shop, you realize they have no specials and you regret not taking the deal in the previous shop. Because you will run late for work, you just buy the expensive order and dash to work.')
                play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                if play_again:
                    keep_playing = input('Would you like to keep playing (YES or NO)? ')
                else:
                    print('Game over, thanks for playing. ')
                    exit = input('Press ENTER to exit! ')
            else:
                print("\n\nIt's most likely that you will walk out of this mall without having decided what you will eat.")
                play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                if play_again:
                    keep_playing = input('Would you like to keep playing (YES or NO)? ')
                else:
                    print('Game over, thanks for playing. ')
                    exit = input('Press ENTER to exit! ')
        else:
            print('\n\nThe other meal deals are not on special and will be costly. Not too worried about that, select your order from this page: https://www.fastfoodmenuprices.com/kfc-prices/')
            play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
            if play_again:
                keep_playing = input('Would you like to keep playing (YES or NO)? ')
            else:
                print('Game over, thanks for playing. ')
                exit = input('Press ENTER to exit! ')

    # Level 1.2
    elif shop.lower() == 'mcdonalds':
        print("\n\nMcDonalds is your favorite fast food shop! It's almost certain you will grab an order.")
        order1 = input("It's in the morning, so the EGG McMuffin sounds good, but what about HOT cakes? ")
        if order1.lower() == 'egg':
            print('\n\nThe egg McMuffin would be good with hot CHOCOLATE shake. Other options include the VANILLA shake and the STRAWBERRY shakes.')
            shake = input('Which shake will have amongnst: Hot CHOCOLATE, VANILLA or STRAWBERRY shakes? ')
            if shake.lower() == 'chocolate':
                print('\n\nGreat choice! But are you going to be full?')
                sides = input('\n\nWhat sides are going to take? APPLE slices or world famous FRIES? ')
                if sides.lower() == 'apple':
                    print('\n\nIt looks like you are balancing your meal. You may also add blueberry muffins. Just suggesting!')
                elif sides.lower() == 'fries':
                    print("\n\nI wouldn't recommend fries in the morning, but if you're craving go for it")
                    fiber = input('You definitely need cabs and fiber. Would you go for the apple FRITTER or cinammon ROLL? ')
                    if fiber.lower() == 'fritter':
                        print('\n\nThere you have it, you will absolutely get that energy for a busy day!')
                        play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                        if play_again:
                            keep_playing = input('Would you like to keep playing (YES or NO)? ')
                        else:
                            print('Game over, thanks for playing. ')
                            exit = input('Press ENTER to exit! ')
                    elif fiber.lower() == 'roll':
                        print('\n\nThe spicy cinammon sounds good.')
                        play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                        if play_again:
                            keep_playing = input('Would you like to keep playing (YES or NO)? ')
                        else:
                            print('Game over, thanks for playing. ')
                            exit = input('Press ENTER to exit! ')
                    else:
                        print("\n\nI guess you don't consider our bakery attractive.")
                        play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                        if play_again:
                            keep_playing = input('Would you like to keep playing (YES or NO)? ')
                        else:
                            print('Game over, thanks for playing. ')
                            exit = input('Press ENTER to exit! ')
                else:
                    print('\n\nYour needed to be more specific. Your order is complete.')
            elif shake.lower() == 'vanilla':
                print('\n\nVanilla is my favorite too. I prefer it with sausage deals.')
                sides1 = input('Would you prefer a sausage BISCUIT or a sausage MCGRIDDLES? ')
                if sides1.lower() == 'biscuit':
                    print('\n\nYummy! Are you gonna get the same order for your wife when you meet up in a few minutes after her morning routine?')
                    others = input('Are you gonna get her the SAME meal or the sausage BURRITO? ')
                    if others.lower() == 'same':
                        print('\n\nEnjoy your breastfast together guys.')
                        play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                        if play_again:
                            keep_playing = input('Would you like to keep playing (YES or NO)? ')
                        else:
                            print('Game over, thanks for playing. ')
                            exit = input('Press ENTER to exit! ')
                    elif others.lower() == 'burrito':
                        print('\n\nThanks for being considerate, she will appreciate that.')
                        play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                        if play_again:
                            keep_playing = input('Would you like to keep playing (YES or NO)? ')
                        else:
                            print('Game over, thanks for playing. ')
                            exit = input('Press ENTER to exit! ')
                    else:
                        print('\n\nShe would have loved your company before you head for work.')
                        play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                        if play_again:
                            keep_playing = input('Would you like to keep playing (YES or NO)? ')
                        else:
                            print('Game over, thanks for playing. ')
                            exit = input('Press ENTER to exit! ')
                elif sides1.lower() == 'mcgriddles':
                    print('\n\nVery good right. You will absolutely enjoy your bites.')
                    drink = input('But it looks like you might need an extra drink. Would take the strawberry WATERMELON slushie or the pink LEMONADE slushie? ')
                    if drink.lower() == 'watermelon':
                        print("\n\nYour order looks very good, it's no wonder you love McDonalds!")
                        play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                        if play_again:
                            keep_playing = input('Would you like to keep playing (YES or NO)? ')
                        else:
                            print('Game over, thanks for playing. ')
                            exit = input('Press ENTER to exit! ')
                    elif drink.lower() == 'lemonade':
                        print('\n\nFantastic, lemon juice is rich in vitamin C for a healthy start of your day.')
                        play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                        if play_again:
                            keep_playing = input('Would you like to keep playing (YES or NO)? ')
                        else:
                            print('Game over, thanks for playing. ')
                            exit = input('Press ENTER to exit! ')
                    else:
                        print("\n\nI guess you're not thirsty.")
                        play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                        if play_again:
                            keep_playing = input('Would you like to keep playing (YES or NO)? ')
                        else:
                            print('Game over, thanks for playing. ')
                            exit = input('Press ENTER to exit! ')
                else:
                    print('\n\nUnfortunately, your order is complete, you could have enjoyed some of our finest deals.')
                    play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                    if play_again:
                        keep_playing = input('Would you like to keep playing (YES or NO)? ')
                    else:
                        print('Game over, thanks for playing. ')
                        exit = input('Press ENTER to exit! ')
            elif shake.lower() == 'strawberry':
                print('\n\nStrawberry shakes are famous.')
                sides3 = input('You look like you might need a burger. Would you go for the CHEESE burger or the HAM burger? ')
                if sides3.lower() == 'cheese':
                    print('\n\nThat cheddar flavor is irresistable.')
                    extras = input('I would suggest the CINNAMON roll or the BLUEBERRY muffin as an extra. Make you pick. ')
                    if extras.lower() == 'cinnamon':
                        print('\n\nYour order is looking good.')
                        play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                        if play_again:
                           keep_playing = input('Would you like to keep playing (YES or NO)? ')
                        else:
                            print('Game over, thanks for playing. ')
                            exit = input('Press ENTER to exit! ')
                    elif extras.lower() == 'blueberry':
                        print('\n\nYour order is ready.')
                        play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                        if play_again:
                            keep_playing = input('Would you like to keep playing (YES or NO)? ')
                        else:
                            print('Game over, thanks for playing. ')
                            exit = input('Press ENTER to exit! ')
                    else:
                        print("\n\nIt's ok not to have extras, it just depends on your diet plan.")
                elif sides3.lower() == 'ham':
                    print('\n\nHam is a light meat, good for the morning.')
                    desserts = input('Such an amazing meal you are putting together. Would you take the McFlurry with OREOS or the McFlurry with MM? ')
                    if desserts.lower() == 'oreos':
                        print('\n\nThat most certainly taste great!')
                        play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                        if play_again:
                            keep_playing = input('Would you like to keep playing (YES or NO)? ')
                        else:
                            print('Game over, thanks for playing. ')
                            exit = input('Press ENTER to exit! ')
                    elif desserts.lower() == 'mm':
                        print('\n\nYou will most certainly love it when the M&Ms melt in your mouth.')
                        play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                        if play_again:
                            keep_playing = input('Would you like to keep playing (YES or NO)? ')
                        else:
                            print('Game over, thanks for playing. ')
                            exit = input('Press ENTER to exit! ')
                    else:
                        print('\n\nAny other choice should work as well!')
                        play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                        if play_again:
                            keep_playing = input('Would you like to keep playing (YES or NO)? ')
                        else:
                            print('Game over, thanks for playing. ')
                            exit = input('Press ENTER to exit! ')
                else:
                    print('\n\nI guess your are on a strick diet. Your order is ready.')
                    play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                    if play_again:
                        keep_playing = input('Would you like to keep playing (YES or NO)? ')
                    else:
                        print('Game over, thanks for playing. ')
                        exit = input('Press ENTER to exit! ')
            else:
                print('\n\nYour order is ready for check out. There were good shakes you missed though. Try next time.')
        elif order1.lower() == 'hot':
            print('\n\nThe hot cakes would be good with a soda drink.')
            shake1 = input('Which soda drink will you have between COCA-COLA and SPRITE? ')
            if shake1.lower() == 'coca-cola':
                print('\n\nGreat choice! But are you going to be full?')
                sides1 = input('What sources are going to take? SPICY Buffalo Sauce or CREAMY Ranch Sauce? ')
                if sides1.lower() == 'spicy':
                    print('\n\nHot cakes, coca-cola and spicy buffalo sauce does not look like a good combination. Tricked you. This is the end of this trial, otherwise the order keep getting worse.')
                    play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                    if play_again:
                        keep_playing = input('Would you like to keep playing (YES or NO)? ')
                    else:
                        print('Game over, thanks for playing. ')
                        exit = input('Press ENTER to exit! ')
                elif sides1.lower() == 'creamy':
                    print("\n\nI wouldn't recommend fries in the morning, only if you're craving them.")
                    fiber = input('You definitely need fruit or cabs. Would you go for the apple SLICES or the world famous FRIES? ')
                    if fiber.lower() == 'slices':
                        print('\n\nThere you have it, you will absolutely get that energy for a busy day!')
                        play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                        if play_again:
                            keep_playing = input('Would you like to keep playing (YES or NO)? ')
                        else:
                            print('Game over, thanks for playing. ')
                            exit = input('Press ENTER to exit! ')
                    elif fiber.lower() == 'fries':
                        print('\n\nThe world famous fries sound good.')
                        play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                        if play_again:
                            keep_playing = input('Would you like to keep playing (YES or NO)? ')
                        else:
                            print('Game over, thanks for playing. ')
                            exit = input('Press ENTER to exit! ')
                    else:
                        print('\n\nPlease choose from the available responses to enjoy the game further.')
                else:
                    print("\n\nGood choice, I wouldn't recommend extra sauce on this meal.")
            elif shake1.lower() == 'sprite':
                print('\n\nSprite is my favorite too. I prefer it with sausage deals')
                sides1 = input('Would you prefer a sausage BISCUIT or a sausage MCGRIDDLES? ')
                if sides1.lower() == 'biscuit':
                    print('\n\nYummy! Are you considering getting the same order for your sister?')
                    others = input('Are you gonna get her the Chicken MCNUGGETS or the Filet-o-FISH? ')
                    if others.lower() == 'mcnuggets':
                        print('\n\nEnjoy your breastfast together guys.')
                        play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                        if play_again:
                            keep_playing = input('Would you like to keep playing (YES or NO)? ')
                        else:
                            print('Game over, thanks for playing. ')
                            exit = input('Press ENTER to exit! ')
                            # play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                            if play_again:
                                keep_playing = input('Would you like to keep playing (YES or NO)? ')
                            else:
                                print('Game over, thanks for playing. ')
                                exit = input('Press ENTER to exit! ')
                    elif others.lower() == 'fish':
                        print('\n\nThanks for being considerate, she will appreciate that.')
                        play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                        if play_again:
                            keep_playing = input('Would you like to keep playing (YES or NO)? ')
                        else:
                            print('Game over, thanks for playing. ')
                            exit = input('Press ENTER to exit! ')
                    else:
                        print("\n\nAre you sure you don't want any extras? Anyways, that's your choice.")
                        play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                        if play_again:
                            keep_playing = input('Would you like to keep playing (YES or NO)? ')
                        else:
                            print('Game over, thanks for playing. ')
                            exit = input('Press ENTER to exit! ')
                elif sides1.lower() == 'mcgriddles':
                    print('\n\nThis is tasty. You will absolutely enjoy your bites.')
                    drink = input('\n\nBut it looks like you might need an extra drink. Would take the strawberry WATERMELON slushie or the pink LEMONADE slushie?')
                    if drink.lower() == 'watermelon':
                        print("\n\nYour order looks very good, it's no wonder you love McDonalds!")
                        play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                        if play_again:
                            keep_playing = input('Would you like to keep playing (YES or NO)? ')
                        else:
                            print('Game over, thanks for playing. ')
                            exit = input('Press ENTER to exit! ')
                    elif drink.lower() == 'lemonade':
                        print('\n\nFantastic, lemon juice is rich in vitamin C for a healthy start of your day.')
                        play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                        if play_again:
                            keep_playing = input('Would you like to keep playing (YES or NO)? ')
                        else:
                            print('Game over, thanks for playing. ')
                            exit = input('Press ENTER to exit! ')
                    else:
                        print('\n\nI think extra fluids in the mornings is good, but anyways, I respect your choice.')
                        play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                        if play_again:
                            keep_playing = input('Would you like to keep playing (YES or NO)? ')
                        else:
                            print('Game over, thanks for playing. ')
                            exit = input('Press ENTER to exit! ')
                else:
                    print('\n\nYou may consider ordering the sausage McMuffin with egg, sausage biscuit with egg, or the bacon, egg and cheese biscuit next time.')
            else:
                print('\n\nUnfortunately, my responses are limited. Please start allover and select from the provided choices.')
        else:
            print('\n\nYou are off to a bad start on your order. Please see what else McDonalds has to offer. Bye.')

    # Level 1.3                   
    elif shop.lower() == 'adidas':
        print('\n\nYou remember seeing a commercial on trending adidas fashion. While walking past the shop, you decide to go in and have a look.')
        clothing = input('There are nice SNEAKERS and track SUITS in store. What you are drawn to? ')
        if clothing.lower() == 'sneakers':
            print('\n\nAdidas sneakers are one of the best.')
            type = input('Would you choose POLYESTER over NYLON material? ')
            if type.lower() == 'polyester':
                print('\n\nI think Polyester shoes are good for leisure activities')
                color = input('What color is best for recreational activities from the two, GREEN and YELLOW, available in the shop? ')
                if color.lower() == 'green':
                    print('\n\nThe green sneaker is nice')
                    play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                    if play_again:
                        keep_playing = input('Would you like to keep playing (YES or NO)? ')
                    else:
                        print('Game over, thanks for playing. ')
                        exit = input('Press ENTER to exit! ')
                elif color.lower() == 'yellow':
                    print('\n\nYellow is very attractive, also good for leisure.')
                    cost = input('The green polyester sneaker is LESS expensive than the other sneaker. Would you take the LESS expensive or the MORE expensive one? ')
                    if cost.lower() == 'less':
                        print('\n\nJust be warned, cheap does not always mean less expensive. They might not last as long.')
                        play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                        if play_again:
                            keep_playing = input('Would you like to keep playing (YES or NO)? ')
                        else:
                            print('Game over, thanks for playing. ')
                            exit = input('Press ENTER to exit! ')
                    elif cost.lower() == 'more':
                        print('\n\nMore expensive is usually daunting, but it is usually the best option in terms of durability and quality.')
                        play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                        if play_again:
                            keep_playing = input('Would you like to keep playing (YES or NO)? ')
                        else:
                            print('Game over, thanks for playing. ')
                            exit = input('Press ENTER to exit! ')
                    else:
                        print('\n\nYou definitely need to make up your mind when shopping.')
                        play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                        if play_again:
                            keep_playing = input('Would you like to keep playing (YES or NO)? ')
                        else:
                            print('Game over, thanks for playing. ')
                            exit = input('Press ENTER to exit! ')
                else:
                    print('\n\nOh sorry, are you color blind?')
                    play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                    if play_again:
                        keep_playing = input('Would you like to keep playing (YES or NO)? ')
                    else:
                        print('Game over, thanks for playing. ')
                        exit = input('Press ENTER to exit! ')
            elif type.lower() == 'nylon':
                print('\n\nNylon sneakers are for professional sports.')
                color1 = input('Imagine your are professional racer. What color is best for a racer from the two, RED and BLUE, available in the shop? ')
                if color1.lower() == 'red':
                    print('\n\nFYI: The color of the sneaker comes best with type of material.')
                    play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                    if play_again:
                        keep_playing = input('Would you like to keep playing (YES or NO)? ')
                    else:
                        print('Game over, thanks for playing. ')
                        exit = input('Press ENTER to exit! ')
                elif color1.lower() == 'blue':
                    print('\n\nFYI: The color of the sneaker comes best with type of material.')
                    type1 = input('What material to you deem best for your color between FIBER and POLYSTRENE? ')
                    if type1.lower() == 'fiber':
                        print('\n\nA combination of red and fibre gives the racer a cool look.')
                        play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                        if play_again:
                            keep_playing = input('Would you like to keep playing (YES or NO)? ')
                        else:
                            print('Game over, thanks for playing. ')
                            exit = input('Press ENTER to exit! ')
                    elif type1.lower() == 'polystrene':
                        print("\n\nPolystrene is not popular yet, but hey it's good to give it a try.")
                        play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                        if play_again:
                            keep_playing = input('Would you like to keep playing (YES or NO)? ')
                        else:
                            print('Game over, thanks for playing. ')
                            exit = input('Press ENTER to exit! ')
                    else:
                        print('\n\nI would still go for fiber or polystrene.')
                else:
                    print('\n\nSorry if you are color blind. Please ask for assistance.')
                    play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                    if play_again:
                        keep_playing = input('Would you like to keep playing (YES or NO)? ')
                    else:
                        print('Game over, thanks for playing. ')
                        exit = input('Press ENTER to exit! ')
            else:
                print('\n\nPolyester and nylon are usually two of the great materials.')
        elif clothing.lower() == 'suits':
            print('\n\nThere are track pants and shorts available.')
            cut = input('Would you go for PANTS or SHORTS? ')
            if cut.lower() == 'pants':
                print('\n\nThere is no wrong choice as long as it is your choice. Pants are good for swimming')
                sport = input('What sport do you prefer between RUNNING and SWIMMING? ')
                if sport.lower() == 'running':
                    print('\n\nAdidas pants can work for both running and leisure.')
                    play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                    if play_again:
                        keep_playing = input('Would you like to keep playing (YES or NO)? ')
                    else:
                        print('Game over, thanks for playing. ')
                        exit = input('Press ENTER to exit! ')
                elif sport.lower() == 'swimming':
                    print('\n\nMost world record swimming champions wear pants as their swimming outfits.')
                    play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                    if play_again:
                        keep_playing = input('Would you like to keep playing (YES or NO)? ')
                    else:
                        print('Game over, thanks for playing. ')
                        exit = input('Press ENTER to exit! ')
                else:
                    print("\n\nOh, you are cyclist aren't you. Cyclist use material similar to what swimmers use.")
                    play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                    if play_again:
                        keep_playing = input('Would you like to keep playing (YES or NO)? ')
                    else:
                        print('Game over, thanks for playing. ')
                        exit = input('Press ENTER to exit! ')
            elif cut.lower() == 'shorts':
                print('\n\nShorts are best suited for running.')
                sport = input('What sport do you prefer, RUNNING or SWIMMING? ')
                if sport.lower() == 'running':
                    print('\n\nWhen running, it is best to have your shorts very short and loose rather than tight.')
                    play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                    if play_again:
                        keep_playing = input('Would you like to keep playing (YES or NO)? ')
                    else:
                        print('Game over, thanks for playing. ')
                        exit = input('Press ENTER to exit! ')
                elif sport.lower() == 'swimming':
                    print('\n\nA swim suit that is tight and has less surface tension is best.')
                    play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                    if play_again:
                        keep_playing = input('Would you like to keep playing (YES or NO)? ')
                    else:
                        print('Game over, thanks for playing. ')
                        exit = input('Press ENTER to exit! ')
                else:
                    print("\n\nYou don't need to be a professional athlete to select from these offers.")
                    play_again = input('Game over, thanks for playing. Do you want to play again (YES or NO)? ')
                    if play_again:
                        keep_playing = input('Would you like to keep playing (YES or NO)? ')
                    else:
                        print('Game over, thanks for playing. ')
                        exit = input('Press ENTER to exit! ')
            else:
                print('\n\nI think you can only have pants or shorts. Sorry you have terminated your game. Next time try to choose from given choices.')
        else:
            print('\n\nYou could try looking into jackets available at Adidas Stores. Please visit their website.')
     
    # Level 1.4
else:
    print()
    over = input('Game over, you missed on the fun. Press ENTER to exit.')

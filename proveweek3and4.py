print('proveweek3and4')
child_meal = float(input("What is the price for a child's meal?"))
# mealc = child_meal * 1
adult_meal = float(input("What is the price for an adult's meal?"))
# meala = adult_meal * 1
children = int(input('What is the number of children?'))
# numberofchildren = children * 1
adults = int(input('What is the number of adults?'))
# numberofadults = adults * 1
fancy_drink = float(input('What is the price for a fancy drink?'))
regular_drink = float(input('Waht is the price for a regular drink?'))
greek_salad = float(input('What is the price of greek salad?'))
icecream = float(input('What is the price of icecream?'))
fancy_drinks = int(input('What is the number of fancy drinks with your order?'))
regular_drinks = int(input('What is the number of regular drinks on your order?'))
salads = int(input('How many salads would you like?'))
dessert = int(input('How many icecreams would you like?'))

tax = float(input('What is the sales tax rate?'))
# salestax = tax * 1
# subtotal = f'Subtotal (Excluding tax): {child_meal * children + adult_meal * adults}'
# subtotal = f'Subtotal (Excluding tax): {mealc * numberofchildren + meala * numberofadults}'
# print(subtotal)

# Subcartegories
adult_meals = adult_meal * adults
# adult_meals_2f = f'${adult_meals:.2f}'
child_meals = child_meal * children
# child_meals_2f = f'${child_meals:.2f}'
salad = greek_salad  * salads
# salad_2f = f'${salad:.2f}'
desserts = icecream * dessert
# desserts_2f = f'${desserts:.2f}'
fancy_drinks = fancy_drink * fancy_drinks
# fancy_drinks_2f = f'${fancy_drinks:.2f}'
regular_drinks = regular_drink * regular_drinks
# regular_drinks_2f = f'${regular_drinks:.2f}'

subtotals = adult_meals + child_meals + salad + desserts + fancy_drinks + regular_drinks
# print(subtotals)
# subtotals_2f = f'{subtotals:.2f}'
sales_tax = float(subtotals) * tax / 100
# print(sales_tax)
# print(subtotals)
# sales_tax_2f = f'${sales_tax:.2f}'

# print(sales_tax)

total_payment = float(subtotals) + float(sales_tax)
# print(total_payment)
# total_amount = f'Grand total (Including tax): ${total_payment}'
# print(total_amount)

payment = float(input('What is the payment amount?'))
# payment_2f = f'${payment:.2f}'
change = float(payment) - float(total_payment)
# change_2f = f'{change:.2f}'
# change_to_customer = f'Change: {change}'
# print(change_to_customer)

output = f'\nThis is your order in USD: \nAdult meals                    ${adult_meals * adults:.2f} \nChildren meals                 $ {child_meals * children:.2f} \nSalads                         $  {salad:.2f} \nIcecream                       $ {desserts:.2f} \nFancy drinks                   $  {fancy_drinks:.2f} \nRegular drinks                 $  {regular_drinks:.2f} \n\nSUBTOTAL (Excluding tax)       $ {subtotals:.2f} \nTAX                            $  {sales_tax:.2f} \nGRAND TOTAL (Including tax)    $ {total_payment:.2f} \nPAYMENT                        ${payment:.2f} \nCHANGE                         $ {change:.2f} \n\nThank you for shopping with us. Have a nice day!'
print(output)
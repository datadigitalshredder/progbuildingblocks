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

subtotals = adult_meal * adults + child_meal * children + greek_salad * salads + icecream * dessert + fancy_drink * fancy_drinks + regular_drink * regular_drinks
sales_tax = subtotals * tax / 100
# print(sales_tax)

total_payment = subtotals + sales_tax
# total_amount = f'Grand total (Including tax): {total_payment}'
# print(total_amount)

payment = float(input('What is the payment amount?'))
change = payment - total_payment
# change_to_customer = f'Change: {change}'
# print(change_to_customer)

output = f'\nThis is your order in USD: \nAdult meals {adult_meal * adults:79} \nChildren meals {child_meal * children:76} \nSalads {greek_salad * salads:84} \nIcecream {icecream * dessert:82} \nFancy drinks {fancy_drink * fancy_drinks:78} \nRegular drinks {regular_drink * regular_drinks:76} \n\nSUBTOTAL (Excluding tax) {subtotals:66} \nTAX {sales_tax:87} \nGRAND TOTAL (Including tax) {total_payment:63} \nPAYMENT {payment:83} \nCHANGE {change:84} \n\nThank you for shopping with us. Have a nice day!'
print(output)
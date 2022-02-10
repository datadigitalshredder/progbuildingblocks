print('proveweek3and4')
child_meal = float(input("What is the price for a child's meal?"))

adult_meal = float(input("What is the price for an adult's meal?"))

children = int(input('What is the number of children?'))

adults = int(input('What is the number of adults?'))

fancy_drink = float(input('What is the price for a fancy drink?'))
regular_drink = float(input('Waht is the price for a regular drink?'))
greek_salad = float(input('What is the price of greek salad?'))
icecream = float(input('What is the price of icecream?'))
fancy_drinks = int(input('What is the number of fancy drinks with your order?'))
regular_drinks = int(input('What is the number of regular drinks on your order?'))
salads = int(input('How many salads would you like?'))
dessert = int(input('How many icecreams would you like?'))

tax = float(input('What is the sales tax rate?'))

subtotals = float(adult_meal * adults + child_meal * children + greek_salad * salads + icecream * dessert + fancy_drink * fancy_drinks + regular_drink * regular_drinks)
print(f'Subtotal (Excluding tax): US$ {subtotals}')

sales_tax = float(subtotals * tax / 100)
print(f'Sales tax: US$ {sales_tax}')

total_payment = float(subtotals + sales_tax)
print(f'Grand total (Including tax): US$ {total_payment}')

payment = float(input('What is the payment amount?'))
change = payment - total_payment

output = f'\nThis is your order in USD: \nAdult meals $ {adult_meal * adults:39.2f} \nChildren meals $ {child_meal * children:36.2f} \nSalads $ {greek_salad * salads:44.2f} \nIcecream $ {icecream * dessert:42.2f} \nFancy drinks $ {fancy_drink * fancy_drinks:38.2f} \nRegular drinks $ {regular_drink * regular_drinks:36.2f} \n\nSUBTOTAL (Excluding tax) $ {subtotals:26.2f} \nTAX $ {sales_tax:47.2f} \nGRAND TOTAL (Including tax) $ {total_payment:23.2f} \n\nPAYMENT $ {payment:43.2f} \nCHANGE $ {change:44.2f} \n\nThank you for shopping with us. Have a nice day!'
print(output)

# The above print statement does not have the $ sign symbol right next to the amount and doesn't look elegant. Import the below library to solve that.

import locale
# Note: Use locale='en_US' for the $ symbol only or locale='' for the US$ symbol
locale.setlocale(locale.LC_ALL, '')
symbol = locale.currency(adult_meal * adults, grouping=True)
symbol1 = locale.currency(child_meal * children, grouping=True)
symbol2 = locale.currency(greek_salad * salads, grouping=True)
symbol3 = locale.currency(icecream * dessert, grouping=True)
symbol4 = locale.currency(fancy_drink * fancy_drinks, grouping=True)
symbol5 = locale.currency(regular_drink * regular_drinks, grouping=True)
symbol6 = locale.currency(subtotals, grouping=True)
symbol7 = locale.currency(sales_tax, grouping=True)
symbol8 = locale.currency(total_payment, grouping=True)
symbol9 = locale.currency(payment, grouping=True)
symbol10 = locale.currency(change, grouping=True)

# print(locale.currency(symbol, grouping=True))

# Note: the ':number' within a place holder is for a number variable. Use .rjust() to specify number of spaces for a string variable, which is the case here. locale.currency() is a string
output1 = f'\nThis is your order in USD: \nAdult meals {symbol.rjust(39)} \nChildren meals {symbol1.rjust(36)} \nSalads {symbol2.rjust(44)} \nIcecream {symbol3.rjust(42)} \nFancy drinks {symbol4.rjust(38)} \nRegular drinks {symbol5.rjust(36)} \n\nSUBTOTAL (Excluding tax) {symbol6.rjust(26)} \nTAX {symbol7.rjust(47)} \nGRAND TOTAL (Including tax) {symbol8.rjust(23)} \n\nPAYMENT {symbol9.rjust(43)} \nCHANGE {symbol10.rjust(44)} \n\nThank you for shopping with us. Have a nice day!'
print(output1)

# A simpler approach would have been making the dollar sign a variable, but it doesn't solve the problem. The dollar sign is not next to the amount
# But by using the variables below: spaces after period must be determined manually from the print statement code and that will align the sym variable.
# The last variable have additional spaces in case the amount is large.
sym = '$'
period = '...'
output2 = f'\nThis is your order in USD: \nAdult meals{period:39}{sym} {adult_meal * adults:10,.2f} \nChildren meals{period:36}{sym} {child_meal * children:10,.2f} \nSalads{period:44}{sym} {greek_salad * salads:10,.2f} \nIcecream{period:42}{sym} {icecream * dessert:10,.2f} \nFancy drinks{period:38}{sym} {fancy_drink * fancy_drinks:10,.2f} \nRegular drinks{period:36}{sym} {regular_drink * regular_drinks:10,.2f} \n\nSUBTOTAL (Excluding tax){period:26}{sym} {subtotals:10,.2f} \nTAX{period:47}{sym} {sales_tax:10,.2f} \nGRAND TOTAL (Including tax){period:23}{sym} {total_payment:10,.2f} \n\nPAYMENT{period:43}{sym} {payment:10,.2f} \nCHANGE{period:44}{sym} {change:10,.2f} \n\nThank you for shopping with us. Have a nice day!'
print(output2)


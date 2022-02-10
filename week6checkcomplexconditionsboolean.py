print('week6complexconditionscheck')

# Approch 1 without Boolean variable.
# loan = int(input('How large is the loan? '))
# history = int(input('How good is your credit history? '))
# income = int(input('How high is your income? '))
# payment = int(input('How large is your down payment? '))
# # if (history >= 7 and income >= 7) or ((history >= 7 or income >= 7) and payment >= 5) or ((loan < 5 and history >= 4) and (income >= 7 or payment >= 7)) or ((loan < 5 and history >= 4) and (income >= 4 and payment >= 4)):
# #     loan = True
# # else:
# #     loan = False 
# if loan >= 5:
#     print()
#     if history >= 7 and income >= 7:
#         print('Decision is: Yes, you will get the loan.')
#     elif history >= 7 or income >= 7:
#         print()
#         if payment >= 5:
#             print('Decision is: Yes, you will get the loan.')
#         # Alternatively combine line 16 to 18:
#         # elif (history >= 7 or income >= 7) and if payment >= 5:
#         #       print('Decision is: Yes, you will get the loan.')
            
#         else:
#             print('Decision is: No, you cannot have the loan.')

# elif loan < 5:
#     print()
#     if history < 4:
#         print('Decision is: No, you cannot have the loan.')
#     elif history >= 4:
#         print()
#         if income >= 7 or payment >= 7:
#             print('Decision is: Yes, you will get the loan.')
#         elif income >= 4 and payment >= 4:
#             print('Decision is: Yes, you will get the loan.') 
#         else:
#             print('Decision is: No, you cannot have the loan.')


# # Approch 2 with Boolean variable.
loan = int(input('How large is the loan? '))
history = int(input('How good is your credit history? '))
income = int(input('How high is your income? '))
payment = int(input('How large is your down payment? '))

if (loan >= 5 and (history >= 7 and income >= 7)) or (loan >= 5 and (history >= 7 or income >= 7) and payment >= 5) or (loan < 5 and (history >= 4 and (income >= 7 or payment >= 7))) or (loan < 5 and (history >= 4 and (income >= 4 and payment >= 4))):
    loan_ok = True
else:
    loan_ok = False 

if loan >= 5:
    if history >= 7 and income >= 7:
        print()
    elif history >= 7 or income >= 7:
        print()
        if payment >= 5:
            print()
    else:
        print()


elif loan < 5:
    print()
    if history < 4:
        print()
    elif history >= 4:
        if income >= 7 or payment >= 7:
            print()
        elif income >= 4 and payment >= 4:
            print()
        else:
            print()

if loan_ok:
    print('Decision is: Yes, you will get the loan')
else:
    print('Decision is: No, you cannot have the loan.')
 
# Both approaches give same results.
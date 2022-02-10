print('Week 10 Team Activity')

# Core requirement 1 Create two lists
bank_accounts = []
balances = []

account_name = ''
account_balances = -1
while account_name.lower() != 'quit':
    account_name = input('What is the name of this account? ').capitalize()
    if account_name.lower() != 'quit':
        bank_accounts.append(account_name)
        account_balances = float(input('What is the balance on the account? '))
        balances.append(account_balances)

# Core requirement 2 Diplay the account and the balance next to it.
print('Accounts Information:')
for i in range(len(bank_accounts)):
    accounts = bank_accounts[i]
    balance = balances[i]
    print(f'{i}. {accounts} - ${balance:.2f}')

# Core requirement 2 Diplay account and balance next to it (Approach 2)
print('Account Information Approach 2:')
for i in range(len(bank_accounts)):
    print(f'{i}. {bank_accounts[i]} - ${balances[i]:.2f}')

# Core requirement 3 Compute and display total in all accounts and the average.
# Total (Approach 1)
running_total = 0
for j in balances:
    running_total += j
print(f'The total balance in all accounts is: ${running_total:.2f}')

# Total (Approach 2)
total = sum(balances)
print(f'The total balance in all accounts is: ${total:.2f}')

# Average 
average = total / len(balances)
print(f'The average in all accounts is: ${average:.2f}')

# Stretch requirement 1 Determine the account with the largest and display the account and balance next to it.
largest_balance = max(balances)
print(f'The largest balance is: ${largest_balance}')
     
    # Set a new variable (i.e. index) for the index of the largest balance
index = balances.index(largest_balance)
print(f'The index of ${largest_balance} in the list is: {index}.')
     
    # Set new variables of the index of account and balances for the largest balance, referenced by variable index
index_accounts = bank_accounts[index]
index_balances = balances[index]
print(f'The account with the largest balance is: \n{index}. {index_accounts} - ${index_balances:.2f}')

# Stretch requirement 2 uses if account_update.lower() == 'yes': and stretch requirement 3 uses the while loop
# uses account_update.lower() != 'no':
account_update = input('Would you like to update an account (YES/ NO)? ')
index_number = -1
while account_update.lower() != 'no':
    index_number = int(input('Please enter the index number you would like to update.'))
    account_balance = float(input('Please enter the new balance.'))
    balances[index_number] = account_balance
    print('Accounts Information:')
    for i in range(len(bank_accounts)):
        accounts = bank_accounts[i]
        balance = balances[i]
        print(f'{i}. {accounts} - ${balance:.2f}')
    account_update = input('Would you like to update an account (YES/ NO)? ')
else:
    # Core requirement 3 Compute and display total in all accounts and the average.
    # Total Approach 1
    running_total = 0
    for j in balances:
        running_total += j
    print(f'The total balance in all accounts is: ${running_total:.2f}')

    # Total Approach 2
    total = sum(balances)
    print(f'The total balance in all accounts is: ${total:.2f}')

    average = total / len(balances)
    print(f'The average in all accounts is: ${average:.2f}')
    

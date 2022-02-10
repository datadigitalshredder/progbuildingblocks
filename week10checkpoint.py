print('Week 10 Check Point')

# Create empty list
groceries = []
item = ''

# Use a while loop to keep asking for a items and add to the list
while item.lower() != 'quit':
    item = input('What are the items on the shopping list? ')
    if item.lower() != 'quit':
        groceries.append(item)

# Print the list items with the index number on the left
for i in range(len(groceries)):
    grocery = groceries[i]
    print(f'{i} - {grocery}')

# Change an item on a given spot and replace it with another at the same spot
change = int(input('Which item number would you like to change? '))
add = input('What new item would you like to add? ')

# Display the new list
groceries[change] = add
for i in range(len(groceries)):
    grocery = groceries[i]
    print(f'{i} - {grocery}')

print('Week 12 Check- Finding things in a list.')

# # My own approach
# people = [
#     "Stephanie 36",
#     "John 29",
#     "Emily 24",
#     "Gretchen 54",
#     "Noah 12",
#     "Penelope 32",
#     "Michael 2",
#     "Jacob 10"
# ]

# # print(people)

# ages = []
# names = []

# for lines in people:
#     parts = lines.split()
#     parts1 = parts[0]
#     parts2 = int(parts[1])
#     print(parts1)
#     # print(parts2)

#     if parts2 != 0:
#         ages.append(parts2)
#         names.append(parts1)

# # Finding the smallest age and keeping track of the name too using the index.
# smallest_age = 9999999999999999
# youngest_person = ''
# for age in ages:
#     if age > 0 and age < smallest_age:
#         smallest_age = age
#         age_index = ages.index(smallest_age)
# print(f'Smallest age is {smallest_age}, the individual is named {names[age_index]}.')

# oldest_age = ages[1]
# oldest_person = ''
# for age in ages:
#     name = parts1
#     if age > oldest_age:
#         oldest_age = age
#         oldest_age_index = ages.index(oldest_age)
# print(f'Largest age is {oldest_age}, the individual is named {names[oldest_age_index]}.')

# Lesson Approach
people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

smallest_age = 99999999999999
name_smallest_age = ''

for lines in people:
    parts = lines.split()
    name = parts[0]
    age = int(parts[1])

    if age < smallest_age:
        smallest_age = age
        name_smallest_age = name
print(f'The youngest person is {name_smallest_age} aged {smallest_age}')

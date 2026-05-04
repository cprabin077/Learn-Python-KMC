import csv  # CSV files
import os  # Remove files

# stduent = ('Ramesh', 'ktm', 22)
# with open('student.csv', 'w') as f:
#     writer = csv.writer(f) # tuple write
#     writer.writerow(stduent)

# -----------------------------------------------------------------------------

# students = [
#     ("Prabin", "Kathmandu", 21),
#     ("Sita", "Pokhara", 19),
#     ("Ram", "Biratnagar", 25),
#     ("Gita", "Lalitpur", 22),
#     ("Hari", "Bhaktapur", 24),
#     ("Maya", "Butwal", 20),
#     ("Krishna", "Dharan", 23),
#     ("Anita", "Hetauda", 21),
#     ("Ramesh", "Nepalgunj", 26),
#     ("Sunita", "Janakpur", 22)
# ]

# with open('students.csv', 'w') as f:
#     writer = csv.writer(f) # tuple inside list
#     for student in students:
#         writer.writerow(students)

# -----------------------------------------------------------------------------

# students = [
#     ("Prabin", "Kathmandu", 21),
#     ("Sita", "Pokhara", 19),
#     ("Ram", "Biratnagar", 25),
#     ("Gita", "Lalitpur", 22),
#     ("Hari", "Bhaktapur", 24),
#     ("Maya", "Butwal", 20),
#     ("Krishna", "Dharan", 23),
#     ("Anita", "Hetauda", 21),
#     ("Ramesh", "Nepalgunj", 26),
#     ("Sunita", "Janakpur", 22)
# ]

# with open('students.csv', 'w') as f:
#     writer = csv.writer(f) # tupe in the list
#     writer.writerows(students)

# -----------------------------------------------------------------------------

# people ={"name": "Prabin", "address": "Kathmandu", "age": 21}
# with open("person.csv","w") as f:
#     writer = csv.DictWriter(f, fieldnames=people.keys())
#     writer.writeheader() # dictionary in the list
#     writer.writerow(people)

# -----------------------------------------------------------------------------

# peoples = [
#     {"name": "Prabin", "address": "Kathmandu", "age": 21},
#     {"name": "Sita", "address": "Pokhara", "age": 19},
#     {"name": "Ram", "address": "Biratnagar", "age": 25},
#     {"name": "Gita", "address": "Lalitpur", "age": 22},
#     {"name": "Hari", "address": "Bhaktapur", "age": 24},
#     {"name": "Maya", "address": "Butwal", "age": 20},
#     {"name": "Krishna", "address": "Dharan", "age": 23},
#     {"name": "Anita", "address": "Hetauda", "age": 21},
#     {"name": "Ramesh", "address": "Nepalgunj", "age": 26},
#     {"name": "Sunita", "address": "Janakpur", "age": 22}
# ]

# with open('peoples.csv','w') as f:
#     writer = csv.DictWriter(f, fieldnames=['name', 'address', 'age'])
#     writer.writeheader() # dictionary in the list
#     for people in peoples:
#         writer.writerow(people) # Single write at once


# -----------------------------------------------------------------------------
# peoples = [
#     {"name": "Prabin", "address": "Kathmandu", "age": 21},
#     {"name": "Sita", "address": "Pokhara", "age": 19},
#     {"name": "Ram", "address": "Biratnagar", "age": 25},
#     {"name": "Gita", "address": "Lalitpur", "age": 22},
#     {"name": "Hari", "address": "Bhaktapur", "age": 24},
#     {"name": "Maya", "address": "Butwal", "age": 20},
#     {"name": "Krishna", "address": "Dharan", "age": 23},
#     {"name": "Anita", "address": "Hetauda", "age": 21},
#     {"name": "Ramesh", "address": "Nepalgunj", "age": 26},
#     {"name": "Sunita", "address": "Janakpur", "age": 22}
# ]

# with open('peoples1.csv','w', newline='', encoding='utf-8') as f:
#     writer = csv.DictWriter(f, fieldnames=['name', 'address', 'age'])
#     writer.writeheader() # dictionary in the list
#     writer.writerows(peoples) # write data in the bulk

# -----------------------------------------------------------------------------


# try:
#     os.remove('people.csv') # delete files
# except FileNotFoundError:
#     print("File does not exist")
# except Exception as e:
#     print("File does not exist")


# -----------------------------------------------------------------------------

# file1 = os.path.exists('people.csv')
# print(file1)

# -----------------------------------------------------------------------------
# file1 = os.path.exists('peoples1.csv')
# print(file1)


# -----------------------------------------------------------------------------
# if os.path.exists('people.csv'):
#     os.remove('people.csv')
# elif os.path.exists('peoples1.csv'):
#     os.remove('peoples1.csv')
# else:
#     print("File does not exist")

# -----------------------------------------------------------------------------
# To make folder
# os.mkdir("hello")

# -----------------------------------------------------------------------------
# help(os)

# -----------------------------------------------------------------------------
# To rename the folder
# os.rename("hello",'hi')

# -----------------------------------------------------------------------------
# To remove the folder
# os.rmdir('hi')

# -----------------------------------------------------------------------------
# List Comprehension
# ls=[1,2,3,4,5]
# # Non-pythonic way
# output = []
# for i in ls:
#     output.append(i**2)
# print(output) # [1, 4, 9, 16, 25]

# # Comprehension => Pythonic way
# output = [i**2 for i in ls]
# print(output) # [1, 4, 9, 16, 25]

# -----------------------------------------------------------------------------
# age = 17
# # Ternary operator
# is_authorized = "Unauthorized" if age < 18 else "Authorized"
# print(is_authorized)

# -----------------------------------------------------------------------------
# Find the numbers in the list is even or odd
# numbers = [1,23,4,3,4,2,2]
# Non-pythonic method
# output = []
# for i in numbers:
#     if i % 2==0:
#         output.append('even')
#     else:
#         output.append('odd')
# print(output) # ['odd', 'odd', 'even', 'odd', 'even', 'even', 'even']

# List comprehension method
# output = ["even" if i%2==0 else "odd" for i in numbers ]
# print(output) # ['odd', 'odd', 'even', 'odd', 'even', 'even', 'even']

# -----------------------------------------------------------------------------
# find only the positive numbers in the list
# numbers = [-9, -7, 3, -1, 0, 1, 3, 4, 5, -7, 6, 8, 10]
# # Pythonic method
# output = [i for i in numbers if i > 0]
# print(output)  # [3, 1, 3, 4, 5, 6, 8, 10]

# -----------------------------------------------------------------------------

# Dictionary Comprehension
us_price = {"milk": 2.05, "bread": 2.6, "butter": 2.6}
# Non-pythonic
# nep_price = {}
# for k,v in us_price.items():
#     nep_price.update({k: v*145})
# print(nep_price) # {'milk': 297.25, 'bread': 377.0, 'butter': 377.0}

# Non-pythonic
nep_price = {k: v * 145 for k, v in us_price.items()}
print(nep_price)  # {'milk': 297.25, 'bread': 377.0, 'butter': 377.0}

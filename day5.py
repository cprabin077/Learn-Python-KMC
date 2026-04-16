# list1 = [1,2,3,4,5,6,7,8]

# print(type(list1))

# print(list1) # [1,2,3,4,5,6,7,8]
# print(list1[0]) # [1]
# print(list1[-8]) # [1]

# print(list1[7]) # [8]
# print(list1[-7]) # [2]

# # print(list1[9]) # IndexError: list index out of range

# print(len(list1))

# #  List can accept multiple data types
# lst2 = [1,3,"Ram", 4.6, "Orange", True, False, 3.14]
# print(isinstance(lst2[-1], float)) # True

# print(isinstance(lst2[len(lst2)-1], float)) # True


#  Slicing in python -> has start and end index
# a = [1,2,3,4,5,6,7]

# print(a[0:4])

# print(a[1:6])

# print(a[:4])

# print(a[0:])

# print(a[-1:])

# print(a[-4:])

# print(a[-7:-3])

# list is a mutable data type

# Append
# a = [1,2,3,4,5,6,7]
# b = [8,9,10]
# a.append("Hello")
# print(a) # [1, 2, 3, 4, 5, 6, 7, 'Hello']
# a.append(2)
# print(a) # [1, 2, 3, 4, 5, 6, 7, 'Hello', 2]
# a.append(b)
# print(a) # [1, 2, 3, 4, 5, 6, 7, 'Hello', 2, [8, 9, 10]]


# Insert
# a = [1,2,3,4,5,6,7]
# a.insert(60,"hello")
# print(a) # [1, 2, 3, 4, 5, 6, 7, 'hello']
# a.insert(0,0)
# print(a) # [0, 1, 2, 3, 4, 5, 6, 7, 'hello']
# a.insert(2,7181)
# print(a)


# Extend
# a = [1,2,3,4,5,6,7]
# b = ["hello", "world"]

# b.extend(a)
# print(b)

# a.extend(b)
# print(a)

# Concat
# a = [1,2,3,4,5,6,7]
# b = ["hello", "wolrd"]
# c = a + b
# print(a, b)
# print(c)

# Index Method -> replaces the original value with new one
# a = [1,2,3,4,5,6,7,"hello", "wolrd"]
# a[7] = "updated"
# print(a) # [1, 2, 3, 4, 5, 6, 7, 'updated', 'wolrd']

# list5 = [3.14,9349, 0.8984, "hello", "hey", True, 10]
# list6 = [45, "Bye", "Python", False]
# # Append
# list5.append("Love")
# print(list5) # [3.14, 9349, 0.8984, 'hello', 'hey', True, 10, 'Love']

# #Insert
# list5.insert(0, "Python")
# print(list5) # ['Python', 3.14, 9349, 0.8984, 'hello', 'hey', True, 10, 'Love']

# # Extend
# list5.extend(list6)
# print(list5) # ['Python', 3.14, 9349, 0.8984, 'hello', 'hey', True, 10, 'Love', 45, 'Bye', 'Python', False]

# # Concat

# list3 = list5 + list6
# print(list3) # ['Python', 3.14, 9349, 0.8984, 'hello', 'hey', True, 10, 'Love', 45, 'Bye', 'Python', False]

# # Index
# list3[0]="Prabin"
# print(list3) # ['Prabin', 3.14, 9349, 0.8984, 'hello', 'hey', True, 10, 'Love', 45, 'Bye', 'Python', False]


# #  Delete -> delete value of index and we cannot recover the data
# del list3[2]
# print(list3) # ['Prabin', 3.14, 0.8984, 'hello', 'hey', True, 10, 'Love', 45, 'Bye', 'Python', False, 45, 'Bye', 'Python', False]

# # Remove -> remove the value of data for first value only
# list3.remove("Bye")
# print(list3) # ['Prabin', 3.14, 0.8984, 'hello', 'hey', True, 10, 'Love', 45, 'Python', False, 45, 'Bye', 'Python', False]

# # Pop -> we can recover/restore the poped value
# list3.pop()
# print(list3)  # ['Prabin', 3.14, 0.8984, 'hello', 'hey', True, 10, 'Love', 45, 'Python', False, 45, 'Bye', 'Python']

# list3.pop(0)
# print(list3) # [3.14, 0.8984, 'hello', 'hey', True, 10, 'Love', 45, 'Python', False, 45, 'Bye', 'Python']

# Clear -> Removes entire data of the list
# a4 = [1,2,3,4,5,6,7,"hello", "wolrd"]
# a4.clear()
# print(a4)

# Count
a3 = [1, 2, 3, 4, 5, 6, 7, "hello", "wolrd"]
count_data = a3.count("hello")
print(count_data)  # 1


# Reverse
a3.reverse()
print(a3)  # ['wolrd', 'hello', 7, 6, 5, 4, 3, 2, 1]

# Sort
a6 = [7, 6, 3, 7, 8, 1, 5, 0, 3, 5]
a6.sort()
print(a6)  # [0, 1, 3, 3, 5, 5, 6, 7, 7, 8]
a6.reverse()
print(a6)  # [8, 7, 7, 6, 5, 5, 3, 3, 1, 0]

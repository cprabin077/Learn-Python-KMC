# Tuples -> immutable, duplicancy

# a = (1,2,3,4)
# print(type(a)) # <class 'tuple'>
# # print(a[100]) # IndexError: tuple index out of range

# print(a[1]) # 2

# b = list(a)
# print(b)
# b[0]=100
# a = tuple(b)
# print(a)

# Set -> immutable but non duplicancy
# data = {1, 2, 3, "surya", True, 4.5, 5, 1, 5, 3, "hello"}
# print(data)


# function -> block of code
# def test():
#     a = 600
#     print("The value of a is",a)
#     return(a)
# test() #The value of a is 600

# def test():
#     print("The value of a is")
    
# print(test()) #None

# return multiple data -> in tuple
# def test1():
#     return (1,2,3,4) 
# print(test1()) # (1, 2, 3, 4)

# return multiple data -> in list
# def test1():
#     return [1,2,3,4],[4,5,6] 
# print(test1()) # ([1, 2, 3, 4], [4, 5, 6])


# # sum of numbers in list using funtion
# def sum_of_list():
#     a = [1,2,3,4,5]
#     sum = 0
#     for i in a:
#         sum += i
#     return sum
# print("Sum: ", sum_of_list()) # Sum: 15


# # sum of numbers in list using funtion
# def sum_of_list():
#     a = [1,2,3,4,5]
#     sum = 0
#     for i in a:
#         sum += i
#         return sum
# print("Sum: ", sum_of_list()) # Sum: 1 i.e. first number only

# sum of numbers in tuple using funtion
# def sum_of_tuple():
#     a = (1,2,3,4,5)
#     sum = 0
#     for i in a:
#         sum += i
#     return sum
# print("Sum: ", sum_of_list()) # Sum: 15

# passing arguments
# def user_info():
#     fname = "prabin"
#     lname = "chy"
#     return f"my name is {fname} {lname}"
# print(user_info())

# fname = input("Enter first name: ")
# lname = input("Enter last name: ")
# def user_info(fname, lname):
#     return f"My name is {fname} {lname}"

# print(user_info(fname, lname)) # My name is prabin chy

# check odd or even
# def check_number(num):
#     if num % 2== 0:
#         return "even"
#     else:
#         return "odd"
# print(check_number(10)) # even
# print(check_number(5)) # odd

# find maximum number from the list
# a = [1,2,3,5]
# def list1(a):  
#     max = a[0]
#     for i in a:
#         if max < i : 
#             max = i
#     return max 

# print(list1(a))

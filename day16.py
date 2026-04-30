# Multiple Inheritance -> Twio base class and one child class
# Example-1:
class Parent1():
    a = 10
    b = 11

class Parent2():
    c = 100
    d = 10

class Child(Parent1, Parent2):
    a = 2

obj = Child()
print(obj.a) # 2
print(Child.__mro__) # (<class '__main__.Child'>, <class '__main__.Parent1'>, <class '__main__.Parent2'>, <class 'object'>)
print(obj.b) # 11
print(obj.d) # 10

# Lambda Function: 
# def add(x,y):
#     return x+y
# print(add(1,2)) # 1+2 = 3

data = lambda x,y : x+y
print(data(1,2)) # 3


# List Comprehension
data = [1,2,3,4,5]
a = [i**2 for i in data]
print(a) # [1, 4, 9, 16, 25]


# Lambda function and List comprehension
square = lambda *args: [i**2 for i in args]
print(square(1,2,3,4,5,6,7,8,9)) # [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(square(15,16)) # [225, 256]

# List Comprehension probem
list1 = [1,2,3,4,5]
a = [i for i in list1]
print(f"The list of numbers are:\n{a}")
a = [i**2 for i in list1]
print(f"The list of square numbers are:\n{a}")
a = [i**3 for i in list1]
print(f"The list of cubic numbers are:\n{a}")

list2 = [i for i in range(1,20) if i % 2 == 0]
print(f"The list of even numbers are:\n{list2}")
list2 = [i for i in range(1,20) if i % 2 != 0]
print(f"The list of odd numbers are:\n{list2}")


list3 = [1,2,3,4,5]
data = [i+10 for i in list3]
print(f"The required output is:\n{data}")


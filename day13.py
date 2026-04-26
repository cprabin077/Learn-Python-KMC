# Example 1
class Person:
    a = 10
    b = 100

    def test(self):
        a = "testing from method"
        print("this is class attribute", self.a)
        print("testing from method", a)


obj = Person()
print(obj)
print(obj.a)  # 10
print(obj.b)  # 100

obj.c = 1000
print(obj.c)  # 1000

print(obj.test())

print("------" * 20)


# Example-2
class Person:
    b = 100

    def test(self):
        self.a = "testing from method"
        print(self.b)  # 100
        print(
            "this is class attribute", self.a
        )  # this is class attribute testing from method
        # print("testing from method", a)

        def add(self):
            return self.b * 100


obj = Person()
print(obj)  # <__main__.Person object at 0x000002648C97A4B0>
# print(obj.b) # 100
print(obj.test())  # None -> since there is no return
print(obj.a)  # testing from method

print("------" * 20)


# Example-3
class Person:
    b = 30

    def test(self):
        self.a = 20
        print(self.b)  # 30

        return self.a

    def multi(self):
        return self.b * self.test()  # 30 * 20 = 600


obj = Person()
print(obj)  # <__main__.Person object at 0x000002648C97A4B0>
print(obj.multi())  # 600

print("------" * 20)


# ------------ Consructor --------------
class Math:
    def __init__(self, a, b, c):
        print(a, b, c)  # 1 2 3
        self.a = a
        self.b = b
        self.c = c
        print(
            "This is __init__"
        )  # This is __init__ is called, when we create an object of a class

    def add(self):
        return self.a + self.b + self.c


obj = Math(1, 2, 3)
print(obj.add())  #

print("------" * 20)


# Find the area of rectangle
class Rectangle:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b


a = Rectangle(4, 5)
print("Area = ", a.area())  # Area =  20

print("------" * 20)
# Employee Salary Problem
class Employee():
    def __init__(self, name, salary="00000"):
        self.name = name
        self.salary = salary

    def details(self):
        return f"\nName = {self.name}\nSalary = {self.salary}"

e  = Employee("Prabin Chaudhary")
e1 = Employee("Prabin Kushmi", 4000)
print(e.details())
print(e1.details())

print("------" * 20)


# Student Result
class StudentResult:
    def __init__(self, name, *marks):
        self.name = name
        self.marks = list(marks)

    def average(self):
        return sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.average()
        if 80 < avg <= 100:
            return "A Grade"
        elif 60 < avg < 80:
            return "B Grade"
        else:
            return "C Grade"

    def display(self):
        return f"Name:{self.name}\nMarks:{self.marks}\nAverage:{self.average()}\nGrade:{self.grade()}\n"


s = StudentResult("Sudan", 90, 90, 80)
s1 = StudentResult("Roman", 89, 83, 56, 78)
print(s.display())
print(s1.display())

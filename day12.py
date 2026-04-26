# Python Object-Oriented Programming (OOP) Covepts

# Class and object
class Person():  # This is creating a class
    a = 10 # defining attribute
    b = 1000  # defining attribute


data = Person()  # THis is creating the object
print(data.a) # 10 
print(data.b) # 1000

data.door = "main door"
data2 = Person()
print(data2.a) # 10
print(data2.b) # 1000

print("------"*20)
class Arko:
    a = 5555
arko = Arko()
print(arko.a) # 5555


print("------"*20)   
# Find the sum, difference using class and object
class Test():
    a = 567
    b = 400

    def add (self):
        return self.a + self.b
    
    def sub(self):
        return self.a - self.b
    
    def result(self):
        return self.add() , self.sub()
    
obj1 =  Test()
print(obj1.a) # 567
print(obj1.b) # 400
print(obj1.add()) # 967
print(obj1.sub())   # 167
print(obj1.result()) # (967, 167)

print("------"*20) 
# find the grade of a student
class Student():
    name = "Hello"
    marks = [100, 20]

    def grade(self):
        total = 0
        for i in self.marks: # self.marks fetch all the values of the list
            total += i

        average = total / len(self.marks) # finding the average

        if average >= 80:
            return "A grade"
        elif 60 <= average < 80:
            return "B grade"
        elif 40 <= average < 60:
            return "C grade"
        else:
            return "Fail"

obj1 = Student() # Object definition
print(f"Name: {obj1.name}") # Hello
print(f"Marks: {obj1.marks}") # [100, 20]
print(f"Grade: {obj1.grade()}") # B grade


print("------"*20)
# Add multiple students
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def grade(self):
        average = sum(self.marks) / len(self.marks)

        if average >= 80:
            return "A grade"
        elif 60 <= average < 80:
            return "B grade"
        elif 40 <= average < 60:
            return "C grade"
        else:
            return "Fail"
        
students = [
    Student("Ram", [80, 90, 85]),
    Student("Shyam", [50, 60, 55]),
    Student("Hari", [30, 40, 35])
    ]

for s in students:
    print(f"Name: {s.name}")
    print(f"Marks: {s.marks}")
    print(f"Grade: {s.grade()}\n")

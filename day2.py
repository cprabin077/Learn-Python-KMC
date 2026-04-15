#  Typecasting and type conversion are same

a= input("Enter the valueof a..")
b= input("Enter the valueof b..")

print(a+b)

print("The value of a is",a)
print(type(a))

a1="123"
print("before type casting",type(a1))

b1=int(a1)
print("After type casting",type(b1))

a1= input("Enter the valueof a1..")
b1= input("Enter the valueof b1..")

print(int(a1)+int(b1))

a2="python"

# # isinstance
print(isinstance(a2,int)) # False 

print(isinstance(a2,str)) # True

name="Suman"
age=14
address="Dang"

# # My name is Suman and age is 14 and address is  Dang
print(f"My name is {name} and age is {age} and address is {address}")

# If Statement
if(1==1):
    print("this is true condition")


# If-else Statement

if(1==1):
    print("this is true condition")

if("test"!="hello"):
    print("This is str compare")
else:
    print("this is else condition")

# If-elif-else Statement

if(1==1):
    print("this is true condition")
elif("test"!="hello"):
    print("This is str compare")
else:
    print("this is else condition")

#Find the Grade after entering the GPA using if-elif-else

gpa=float(input("Enter the grade: "))

if(gpa>4.0 or gpa<=0):
    print(gpa,"is inavlid GPA")    
if(gpa<=4.0 and gpa>3.6):
    print(gpa,"is A+")
elif(gpa<=3.6 and gpa>3.2):
    print(gpa,"is A")
elif(gpa<=3.2 and gpa>2.8):
    print(gpa,"is B+")
elif(gpa<=2.8 and gpa>2.4):
    print(gpa,"is B")
elif(gpa<=2.4 and gpa>2.0):
    print(gpa,"is C+")
elif(gpa<=2.0 and gpa>1.6):
    print(gpa,"is C")
elif(gpa<=1.6 and gpa>1.2):
    print(gpa,"is D+")
else:
    print("You are failed")



#Find the Grade after entering the gp using nested-if-else

gp=float(input("Enter the grade: "))

if(gp>4.0 or gp<=0):
    print(gp,"is inavlid GPA")
else:    
    if(gp<=4.0 and gp>3.6):
        print(gp,"is A+")
    elif(gp<=3.6 and gp>3.2):
        print(gp,"is A")
    elif(gp<=3.2 and gp>2.8):
        print(gp,"is B+")
    elif(gp<=2.8 and gp>2.4):
        print(gp,"is B")
    elif(gp<=2.4 and gp>2.0):
        print(gp,"is C+")
    elif(gp<=2.0 and gp>1.6):
        print(gp,"is C")
    elif(gp<=1.6 and gp>1.2):
        print(gp,"is D+")
    else:
        print("You are failed")



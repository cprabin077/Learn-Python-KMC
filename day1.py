# print("Hello wolrd ", 1, 2+1)

# Data type or variable declaration
a4=None
b4=False
c4="class"
d4=10
e4=10.94

print(type(a4))
print(type(b4))
print(type(c4))
print(type(d4))
print(type(e4))


c=100
d=c

print(c)
print(d)


# Arithmetic Operators (+ - * /)
p=10
q=40
print(p+q,p-q,p*q,p/q) # directly divide garda jaile pani value float ma aauxa

# Others operators

a=10
b=2
print(a%b) # 0
print(a**b) # 100
print(a/b) # 5.0 -- print divided value into float
print(a//b) # 5 -- print divided value into integer

# String allows (+ *) operators

a0= "test "
b0="hari"
print(a0+b0) # test hari

a1= "20"
b1="30"
print(a1+b1) # 2030

a2= "test"
b2= 3
print(a2*b2) # test test test 

# Comparison operator

print(1==1) # True
print(1==2) # False
print(1!=2) # True
print(1!=1) # False
print(1>4) # False
print(1<4) # True
print(1>=5) # False
print(5>=6) # False
print(5>=5) # True
print(5<=6) # True
print(5<=5) # True


# Logical operators (AND, OR, NOT) works in boolean form

print(True and True) # True
print(1==1 and "test"!="hello") # True
print(1==1 and "test"=="hello") # Flase

print(True or True) # True
print(1==1 or "test"!="hello") # True
print(1==1 or "test"=="hello") # True

logged_in=True
print(not(logged_in)) # False


# Type casting
x = int("5")
y = float("3.14")
z = str(100)

print(type(x))  # <class 'int'>
print(isinstance(x, int))  # True

print(type(y))  # <class 'float'>
print(isinstance(y, float))  # True

print(type(z))  # <class 'str'>
print(isinstance(z, str))  # True


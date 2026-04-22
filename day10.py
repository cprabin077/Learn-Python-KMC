# keyword argument -> 
def user_info(fname, lname, age):
    return f"My name is {fname} {lname} and age is {age}"
print(user_info("prabin",12,"chaudhary")) # My name is prabin 12 and age is chaudhary
print(user_info(fname ="prabin", age=23, lname="chaudhary")) # My name is prabin chaudhary and age is 23

print("-------"*10)
# Arbitrary positional argument
# def sum_number(*num):
#     print(num)
#     print(type(num))

# sum_number(1)
# sum_number(1,2,3)
# sum_number()

print("-------"*10)

# def sum_num(*num):
#     print("----->",len(num))
#     sum = 0 
#     if len(num) > 1:
#         for i in num:
#             sum += i
#         return f"Total sum = {sum}"
#     else:
#         return("Length must be more than 1")
        
# print(sum_num(1,2))
# print(sum_num(1,2,3))
# print(sum_num())   

print("-------"*10)
# sum_number(1,"test",12,13,"hello")
# def sum_number(*num):
#     sum = 0
#     for i in num:
#         if not isinstance(i, str):
#             sum += i
#         else:
#             continue
#     return f"The sum is {sum}"
    
# print(sum_number(1,"test",12,13,"hello"))

print("-------"*10)
#  Arbitrary keyword argument
# def per(**mdata):
#     print(mdata)
#     print("eng", mdata['eng'])
#     print("math", mdata['math'])
#     print("comp", mdata['comp'])

# per(eng = 100, math = 20, comp = 40)

print("-----"*20)
# def per(**mdata):

#     if 'eng' not in mdata or'math' not in mdata or 'comp' not in mdata: 
#         print("error")
#     else:
#         print("eng", mdata['eng'])
#         print("math", mdata['math'])
#         print("comp", mdata['comp'])
        

# per(eng = 100, math = 20, comp = 40)
# per(eng = 100, math = 20)

print("-----"*20)
# using loop and list
def per(**mdata):
    choice = ["eng","math","comp"]
    for key in choice:
        if key not in mdata:
            return f"{key} is missing"
    return f"Eng = {mdata['eng']},\nNep = {mdata['eng']}, \nComp = {mdata['comp']}"

print(per(eng = 100, math = 20, comp = 40))
print(per(eng = 100, math = 20))



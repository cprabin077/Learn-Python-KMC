# '''
# # Looping -> Iteration -> repitition
# # For loop -> finite loop
# '''

# # for loop
# for i in [1,2,3,4,5,1]:
#     print(i)
#     print("Python")

# # Odd even
# for i in [12,13,22,15,67]:
#     if(i%2 == 0):
#         print(f"{i} even")
#     else:
#         print(f"{i} odd")

# for i in "prabin":
#     print(i)

# #  for loop in dictionaries
# a ={
#     "name":"hari",
#     "college":"kmc"
# }
# for i in a:
#     print(f"{i} = {a[i]}")

# for i in a.values():
#     print(i)

# for i in a.keys():
#     print(i)

# print odd even number in list
# odd = []
# even = []
# for i in range(1,100):
#     if(i%2==0):
#         even.append(i)
#     else:
#         odd.append(i)
# print(f"even num = {even}")
# print(f"odd num = {odd}")

# a = [1, 2, 3, "hello", "test", 1, 2, 4, 7.3, True]
# num = []
# for i in a:
#     if isinstance(i, int):
#         print(i)


# find the sum of number inside loop
# a = [10,20,30,40]
# sum = 0
# for i in a:
#     sum =+ i
# print(sum)


# # nested for loop
# for i in [1, 2, 3]:
#     for j in [4, 5, 6, 7]:
#         print(i, j)

# # while loop
# while(True):
#     print("this is while loop")
#     break

# i = 0
# while(i<10):
#     i = i+1
#     print(i)

# a = [1.2,2,3,4, "test", "hello", True]
# i = 0
# while(i<len(a)):
#     print(a[i])
#     i = i+1
   
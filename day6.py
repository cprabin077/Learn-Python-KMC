# Dictionaries -> is also looked as JSON -> key should be unique but value may be same or different

# a={
#     "name" :"Hari",
#     "address":"Nepal",
#     "age":12,
#     "phone":[123,456],
#     "Address":"Kathmandu"
# }

# print(type(a)) # <class 'dict'>
# print(a) # {'name': 'Hari', 'address': 'Nepal', 'age': 12, 'phone': [123, 456], 'Address': 'Kathmandu'}
# print(a["address"],a["age"]) # Nepal 12
# print(len(a)) # 5
# print(a.keys()) # dict_keys(['name', 'address', 'age', 'phone'])
# print(a.values()) # dict_values(['Hari', 'Nepal', 12, [123, 456]])
# # print(a['Addresss']) # KeyError: 'Addresss'

# print(a["phone"][-1]) # 456


# Add new data (key: values) to the dictionaries
# user_info ={
#     "name":"Sudan",
#     "age": 22,
# }
# # print(user_info) # {'name': 'Sudan', 'age': 22}
# # user_info["name"]="Hari"
# # print(user_info) # {'name': 'Hari', 'age': 22}
# # user_info["age"]=45
# # print(user_info) # {'name': 'Hari', 'age': 45}
# # user_info["phone"] = 123
# # print(user_info)  # {'name': 'Hari', 'age': 22, 'phone': 123}

# # Dictionaries work on write or modify concept 
# user_info.update({
#     "name":"Hari",
#     "age":123,
#     "phone":123,
#     "role":"teacher"
# })
# print(user_info) # {'name': 'Hari', 'age': 123, 'phone': 123, 'role': 'teacher'}


# data = {
#     "name":"Hari",
#     "age":123,
#     "phone":123,
#     "role":"teacher"
# }

# Delete -> del -> if not found the key it will show keyerror -> it won't store the key value pairs 
# del data["role"]
# print(data) # {'name': 'Hari', 'age': 123, 'phone': 123}

#  pop -> it will store the key value pairs
# data.pop("age") 
# print(data) # {'name': 'Hari', 'phone': 123, 'role': 'teacher'}

# pop item -> removes the last value
# data.popitem()
# print(data) # {'name': 'Hari', 'phone': 123}

# a ={}
# a.popitem()
# print(a) # KeyError: 'popitem(): dictionary is empty'

# data.clear()
# print(data) # {}


# user_info = {
#     "name":"Hari",
#     "age":123,
#     "phone": [
#         {
#             "type":"NTC",
#             "num":9844
#         },
#         {
#             "type":"Ncell",
#             "num": 980
#         },
#         {
#            "type":"Jio",
#             "num":722 
#         }
#     ],
#     "role":"teacher"
# }

# print(f"{user_info['name']}, {user_info['phone'][0]['type']} number is {user_info['phone'][0]['num']}")

# print(f"{user_info['name']}, {user_info['phone'][1]['type']} number is {user_info['phone'][1]['num']}")

# print(f"{user_info['name']}, {user_info['phone'][2]['type']} number is {user_info['phone'][2]['num']}")


# nested dictionaries
# user_info = {
#     "name":"Hari",
#     "address":{
#         "per":"Kailali",
#         "temp":"Kirtipur"
#     }
# }
# print(user_info['address']['temp']) # Kirtipur

# Looping -> Iteration 
# for loop -> finite loop
# while loop -> infinite loop 
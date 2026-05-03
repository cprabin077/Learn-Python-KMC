# with open("sample.txt", "w") as f:
#     f.write("Hello sample text svKADJAkh hgAKJH kuhwi hei lhqep   j   ;obsja  I OIHQDHDKLHOIE,MN OH   IH")

# print(f.closed)


# with open("sample.txt", "r") as f:
#     print(f.read())

# with open("sample.txt", "r") as f:
#     print(f.read(10)) # read the first 10 characters
#     print(f.tell()) # 10 i.e. we are at the 10th position
#     f.seek(0) # bring the cursor to the first position
#     print(f.tell()) # 0


# with open("sample.txt", "r") as f:
#     # print(f.read())
#     f.seek(12)
#     print(f.read(4))

# with open("sample.txt", "r") as f:
#     print(f.readline())
#     print(f.readline())

# with open("sample.txt", "r") as f:
#     for i in f:
#         print(i)

# with open("sample.txt", "rt") as f:
#     print(f.read())

# with open("sample.txt") as f:
#     print(f.read())


# Binary file read and write
# with open("download.jfif","rb") as f: # r read the file in text mode
#     print(f.read())

# # JSON String
# import json

# person = {
#         "username": "prabin123",
#         "email": "prabin@example.com",
#         "hobbies": ["coding", "music"],
#         "attributes": {
#             "age": 22,
#             "location": "Kathmandu"
#         },
#         "is_active": True,
#         "phone": None,
#     }

# print(person, type(person))
# person_json = json.dumps(person) # dictionary -> JSON string
# # print(person_json)
# print(person_json, type(person_json))


# # JSON to Dictionary
# import json

# json_string = """{
#     "username": "prabin123",
#     "email": "prabin@example.com",
#     "hobbies": ["coding", "music"],
#     "attributes":{
#                     "age": 22,
#                     "location": "Kathmandu"
#                 },
#     "is_active": true,
#     "phone": null
#     }
#     """

# x = json.loads(json_string)  # json string -> dictionary
# print(x, type(x))

# # write json string to json file
# import json

# person = {
#         "username": "prabin123",
#         "email": "prabin@example.com",
#         "hobbies": ["coding", "music"],
#         "attributes": {
#             "age": 22,
#             "location": "Kathmandu"
#         },
#         "is_active": True,
#         "phone": None,
#     }

# # print(person, type(person))
# person_json = json.dumps(person) # dictionary -> JSON string
# with open("person.json", "w") as f:
#     f.write(person_json) # json string -> json file


import json

# person1 = {
#         "username": "prabin123",
#         "email": "prabin@example.com",
#         "hobbies": ["coding", "music"],
#         "attributes": {
#             "age": 22,
#             "location": "Kathmandu"
#         },
#         "is_active": True,
#         "phone": None,
#     }

# with open("person1.json", "w") as f:
#     json.dump(person1, f, indent=4) # direct convert dictionary -> json file without converting dict into json string using dump


# person1 = {
#         "username": "prabin123",
#         "email": "prabin@example.com",
#         "hobbies": ["coding", "music"],
#         "attributes": {
#             "age": 22,
#             "location": "Kathmandu"
#         },
#         "is_active": True,
#         "phone": None,
#     }

# with open("person1.json", "w") as f:
#     json.dump(person1, f, indent=4) # direct convert dictionary -> json file without converting dict into json string using dump
#     print(person1, type(person1))
# with open("person1.json", "r") as f:
#     data = f.read() # json file -> json string
#     json_data = json.loads(data) # json to dictionary
#     print(json_data, type(json_data))

# with open("person1.json", "r") as f:
#     json_data = json.load(f) # json file to dictionary
#     print(json_data, type(json_data))


# CSV -> (Comma Separated Values) File
import csv

# with open("sample_users.csv", "r") as f:
#     # print(f.read())
#     data = csv.reader(f)
#     for i in data:
#         print(i[0], i[3])


with open("sample_users.csv", "r") as f:
    # print(f.read())
    data = csv.DictReader(f)
    for i in data:
        print(i["first_name"], i["address"])

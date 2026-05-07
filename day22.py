# import mysql.connector

# db = mysql.connector.connect(
#     host = "localhost",
#     username = "root",
#     password = "root"
# )
# print(db)


# CRUD
import sqlite3


connection = sqlite3.connect('students.sqlite3')
terminal = connection.cursor()

#INSERT Query
query = "INSERT INTO students (name, age, course, marks, email) VALUES ('Rita Chaudhary', 23, 'BCA', 65, 'ritachy@gmail.com')"

terminal.execute(query)
connection.commit()
print(connection)


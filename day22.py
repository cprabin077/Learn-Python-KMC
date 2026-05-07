# import mysql.connector

# db = mysql.connector.connect(
#     host = "localhost",
#     username = "root",
#     password = "root"
# )
# print(db)


# CRUD
import sqlite3

# Connect database
connection = sqlite3.connect('students.sqlite3')

# Create cursor
terminal = connection.cursor()

# Create table
terminal.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    course TEXT NOT NULL,
    marks INTEGER NOT NULL,
    email TEXT NOT NULL
)
""")

# Insert query
query = """
INSERT INTO students (name, age, course, marks, email)
VALUES (?, ?, ?, ?, ?)
"""

data = ('Rita Chaudhary', 23, 'BCA', 65, 'ritachy@gmail.com')

terminal.execute(query, data)

# Save changes
connection.commit()

print("Data inserted successfully")

# Display data
terminal.execute("SELECT * FROM students")

rows = terminal.fetchall()

for row in rows:
    print(row)

# Close connection
connection.close()


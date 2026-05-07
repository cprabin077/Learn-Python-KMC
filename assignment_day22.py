import mysql.connector

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="student_db"
)

# Create cursor
terminal = connection.cursor()

# Create table
terminal.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    course VARCHAR(100) NOT NULL,
    marks INT NOT NULL,
    email VARCHAR(100) NOT NULL
)
""")

# Insert query
query = """
INSERT INTO students (name, age, course, marks, email)
VALUES (%s, %s, %s, %s, %s)
"""

data = ('Sandesh Chaudhary', 25, 'B.Sc. CSIT', 90, 'sandesh@gmail.com')

terminal.execute(query, data)

print("Data inserted successfully")

# Display records
terminal.execute("SELECT * FROM students")

result = terminal.fetchall()
print(result)

# Update Records 
terminal.execute("UPDATE students SET name = 'Prajwal Chaudhary', age = 24, course = 'BE Computer', marks = 70, email = 'prajwal@nast.edu.np' WHERE id = 2")
print("Data updated successfully!!")

# Delete Records
terminal.execute("DELETE FROM students where id = 6")
print("Data deleted successfully!!")

# Save changes
connection.commit()

# Close connection
terminal.close()
connection.close()
import sqlite3
import random

# Create Database
connection = sqlite3.connect("student.db")

# Create cursor
cursor = connection.cursor()

# Create Table
create_table_query = """
CREATE TABLE IF NOT EXISTS STUDENT (
    NAME    VARCHAR(25),
    COURSE  VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS   INT
);
"""

cursor.execute(create_table_query)

# Sample Data
names = ["Nishant", "Subodh", "Shanu", "Chinmay", "Nikhil", "Amit", "Raj", "Neha", "Sonia", "Vikas"]
courses = ["Data Science", "AI", "Cyber Security", "Cloud Computing", "DevOps", "Software Engineering"]
sections = ["A", "B", "C"]

# Insert 100 Records
sql_query = """INSERT INTO STUDENT (NAME, COURSE, SECTION, MARKS) VALUES (?, ?, ?, ?)"""

values = [
    (random.choice(names), random.choice(courses), random.choice(sections), random.randint(30, 100))
    for _ in range(100)
]

cursor.executemany(sql_query, values)
connection.commit()

# Fetch and Display Data
data = cursor.execute("""SELECT * FROM STUDENT""")

for row in data:
    print(row)

# Close Connection
if connection:
    connection.close()

import sqlite3

# Create the python_programming table and create connection to the database.

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS python_programming (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    grade INT NOT NULL
);''')

# Insert multiple rows into the python_programming table.

cursor.executemany('''
INSERT INTO python_programming (id, name, grade)
VALUES(?, ?, ?);
''', [
    (55, 'Carl Davis ', 61),
    (66, 'Dennis Fredrickson', 88),
    (77, 'Jane Richards', 78),
    (12, 'Peyton Sawyer', 45),
    (2, 'Lucas Brooke', 99)
])

# Retrieve all rows where the grade is between 60 and 80 (inclusive).

cursor.execute('''
SELECT * FROM python_programming
WHERE grade >= 60 
AND grade <= 80;
''')
print("Students with grades between 60 and 80:", cursor.fetchall())

# Update Carl Davis’s grade to 65.

cursor.execute('''
UPDATE python_programming SET grade = 65 WHERE name = 'Carl Davis';
''')

# Delete Dennis Fredrickson’s row. 

cursor.execute('''
DELETE FROM python_programming 
WHERE name = 'Dennis Fredrickson';
''')

# Update the grade of all students with an id greater than 55 to 80

cursor.execute('''
UPDATE python_programming SET grade = 80 WHERE id > 55;
''')

# Commit the changes and close the connection.
conn.commit()
conn.close()

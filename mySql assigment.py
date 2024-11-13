# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vF0dQawF4fbJH70mw77OOl-CEwjVplYy
"""

"""
Ans 1.

A database is an organized collection of structured data stored electronically for efficient retrieval and management.

SQL Databases:
- Use SQL for defining and manipulating data.
- Store data in tables with rows and columns.
- Ideal for structured data and transactional systems.
- Examples: MySQL, PostgreSQL, Oracle.

NoSQL Databases:
- Use various data models like document, key-value, wide-column, or graph.
- Provide flexibility in handling unstructured data.
- Suitable for large-scale, distributed systems.
- Examples: MongoDB, Cassandra, Redis.
"""

"""
Ans 2.

DDL (Data Definition Language) is used to define and manage database schema structures.

- CREATE: Creates a new table or database.
  Example:
    CREATE TABLE Students (ID INT, Name VARCHAR(100));

- DROP: Deletes a table or database.
  Example:
    DROP TABLE Students;

- ALTER: Modifies an existing table's structure, such as adding/removing columns.
  Example:
    ALTER TABLE Students ADD COLUMN Age INT;

- TRUNCATE: Deletes all rows from a table without deleting the table structure.
  Example:
    TRUNCATE TABLE Students;
"""

"""
Ans 3.

DML (Data Manipulation Language) is used to manipulate data within tables.

- INSERT: Adds new rows of data to a table.
  Example:
    INSERT INTO Students (ID, Name, Age) VALUES (1, 'John Doe', 20);

- UPDATE: Modifies existing data within a table.
  Example:
    UPDATE Students SET Age = 21 WHERE ID = 1;

- DELETE: Removes rows from a table based on a condition.
  Example:
    DELETE FROM Students WHERE ID = 1;
"""

"""
Ans 4.

DQL (Data Query Language) is used to query and retrieve data from a database.

- SELECT: Retrieves specified columns or all columns from a table.
  Example:
    SELECT Name, Age FROM Students WHERE Age > 18;
"""

"""

Ans 5.

- Primary Key: A unique identifier for each record in a table, ensuring that no two rows have the same primary key value.
  Example: 'ID' column in a 'Students' table.

- Foreign Key: A field in one table that references the primary key of another table, creating a relationship between the tables.
  Example: 'StudentID' in an 'Enrollments' table that refers to 'ID' in the 'Students' table.
"""

"""
Ans 6.
"""
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)

cursor = connection.cursor()  # Creates a cursor object that allows interaction with the database
cursor.execute("SELECT * FROM Students")  # Executes a SQL command using the cursor

results = cursor.fetchall()
for row in results:
    print(row)

connection.close()

"""
Ans 7.
1. FROM – Identifies the table to be queried.
2. WHERE – Filters rows based on conditions.
3. GROUP BY – Groups rows based on specified columns.
4. HAVING – Filters groups based on conditions.
5. SELECT – Selects columns to display.
6. ORDER BY – Orders the result set.
7. LIMIT – Limits the number of rows returned.
"""
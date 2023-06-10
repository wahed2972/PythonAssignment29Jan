# Q.1
# Database is a structured collection of data which is stored in table consists of rows and columns, 
# which is used to store,retrieve and manipulate data.
# Difference between SQL and NoSQL
# SQL is used to store the relational data in structured form 
# NOSQL is used to store non-structured , semi-structured data


# Q.2
# # DDL stands for Data Definition Language which is used to create, modify or delete the table. 
# Create: Create is used to create a table with column attributes with their data types
# Example : create table student(roll_no int , name varchar(255), marks int);

# Drop: Drop is used to delete the table and its data permanently 
# Example: drop table student;
 
# Alter: Alter is used to modify the table , it is used to add,update or delete the columns.
# Example: alter table student add column phone_num INT(20);
 
# Truncate: Truncate is used to remove the data of table, but its structure is not deleted
# Example: truncate table student;


# Q.3
# DML stands for Data Manipulation Language which is used to insert, update and delete data.
# Insert: Insert is used to insert the required data into the table
# Example: Insert into table student values (39, 'AW', 99 , 78946623);

# Update: Update is used to modify which data we want to update, it can be updated by giving a condition.
# Example: Update student
#           set roll_no = 44
#           where name = 'AW'
 
# Delete: Delete is used to remove one or more rows from the table
# Example: Delete from student where marks>50


# Q.4

# DQL stand for Data Query Langauge which is generally used to retrieve one or more rows from the table using select
# Select: Select is used to select the one or more rows based on condition, * means it select whole table
# Example: Select roll_no from student where marks>85

# Q.5

# Primary Key: It is the unique key which used to identify the row like roll no is unique which is used to identify a specific student
# Foreign Key: It is a key which refers to the primary key or unique key of another table, it is used to have a relationship between two tables


# Q.6
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()

# cursor() - It creates a cursor object which acts as a handle or a control structure for executing SQL statements and managing the result sets returned by those statements.
# execute() - It is used to execute SQL statements through cursor objects. It takes SQL statements as a parameter and executes on connected database


# Q.7

# Order of execution of SQL clauses in an SQL query

# FROM - The table from which to retrieve the data. 
# WHERE - Filters based on condition. 
# GROUP BY - Groups rows and columns , used for aggregate functions.
# HAVING - It filters the groups created by group by.
# SELECT - Retrives the required data from the table,
# DISTINCT - Eliminates the duplicate values.
# ORDER BY - Sorts the result based on ascending or descending order.
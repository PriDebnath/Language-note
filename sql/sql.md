
   SQL note

    SQL is a domain-specific language for managing and querying relational databases. 



SQL datatypes


CHAR(100)  =>  to store characters / string of fixed length . 


VARCHAR(100)  =>  to store  characters/string upto given length .


BLOB(100)  =>  to store binary large object 


INT => to store number

BOOLEAN => to store true or false


FLOAT  => to store decimal number

DATE  => to store date in (YYYY-MM-DD) format 

YEAR => to store year 






Types of SQL commands


DDL ( Data Definition Language) : create, alter, rename, truncate and drop

DQL ( Data Query Language ) : select


DML ( Data Manipulation Language ) : insert, update and delete

DCL ( Data Control Language ) : grant and revoke permission to users

TCL ( Transaction Control Language ) : start transaction, commit, rollback







SQL commands



Create database 
CREATE DATABASE db_name



Show  database
SHOW DATABASES



Delete database
DROP DATABASE db_name

or

DROP DATABASE IF EXISTS db_name



Create table

CREATE TABLE table_name(
  column_name1  datatype  constraint,
  column_name2  datatype  constraint,
)



CREATE TABLE student (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    school_name VARCHAR(50),
    FOREIGN KEY school_name REFERENCES school(school_name)
);

Or

CREATE TABLE student IF NOT EXISTS



Inserting Data to table
INSERT INTO student (student_id, first_name, last_name)

VALUES (1, 'John', 'Doe');



Selecting Data

SELECT col1, col2 FROM table_name


SELECT * FROM student  // * means all columns

SELECT  col DISTINCT FROM table // will give only unique values from table



Filtering

SELECT *  FROM student WHERE firsrt_name = Jhon;

SELECT first_name  FROM student WHERE firsrt_name = 'Jhon' AND last_name = 'Doe';


SELECT * FROM student WHERE first_name LIKE '%pri%';




Sorting 
SELECT * FROM student ORDER BY student_id DESC



Updating Data
UPDATE student SET first_name = 'Jonny' WHERE student_id = 1



Deleting row data
DELETE FROM student WHERE student_id = 1



Delete table
DROP TABLE table_name 



Delete database
DROP DATABASE db_name

Or

DROP DATABASE IF EXISTS db_name



ALTER 

*Add new field/column to existing table

ALTER TABLE student
ADD COLUMN phone_number VARCHAR(15)


*change column 

ALTER TABLE student CHANGE COLUMN old_name new_column_name new_datatype new_constraint




*modify column

ALTER TABLE table_name  MODIFY column_name   new_daratype  new_constraint




*Delete  field/column from existing table

ALTER TABLE student
DELETE COLUMN phone_number 




*change table name

ALTER   table_name 
RENAME TO  new_table_name






Constraints 

SQL constraints are used to specify rule for data in a table

NOT NULL  - column cannot have null value

UNIQUE - all values in column should be different 

PRIMARY KEY - column value should be unique and not null

FOREIGN KEY -  primary key of other table . In a table Foreign key can or cannot be repeated

  DEFAULT - we can set default value for a column, so that if a user do not put something in it . Value will be set to default value . Eq: ( age INT DEFAULT 1 )

CHECKS - we can add checks before inserting a data . Eq : age INT CHECK ( age >= 18 )







Operators


Arithmetic => +(Addition), -(subtraction), * ( multiplication), / (division), % ( modulus)


Comparison => =(equal to), != (not equal to), <, >, <=, =>


Logical operator=> OR, NOT, ALL, IN , AND, BETWEEN, LIKE, ANY


Bitwise => &(bitwise AND), |(bitwise OR)






Uses of operator



SELECT * FROM student WHERE mark BETWEEN 80 AND 90


SELECT * FROM student WHERE city IN('Mumbai', 'Delhi') ; // it look for a list of values if it found it then returns the matched rows . We can also limit the length of rows using LIMIT 


SELECT * FROM student WHERE city NOT IN('Mumbai', 'Delhi') LIMIT 3







Aggregate function

Aggregate functions perform a calculation on a set of values and return a single value . like COUNT, AVG, MAX, MIN  and SUM
Aggregate functions work single column

Eq:

SELECT MAX(mark) FROM student

SELECT COUNT(mark) FROM student  // will return count of rows









General order 

SELECT column(s)
FROM table_name
WHERE condition
GROUP BY column(s)
HAVING condition
ORDER BY column(s) ASC









Clause

GROUP BY 
   Group rows that have the same values into summary rows . It collects data from multiple records and groups the result by one or more columns .
*Generally we use group by with some aggregation  function .


SELECT city COUNT(mark) FROM student GROUP BY city





Having
Similar to where clause , applies some conditions on rows . Used when we want to apply any condition after grouping

Count number of students in each city where max marks cross 80

SELECT city, count(rollno) FROM student GROUP BY city HAVING MAX(mark) > 80









Join 

Join in SQL is used to combine two or more tables based on a related column between them 



INNER JOIN
Returns records that has matching values in both table

SELECT * FROM student 
INNER JOIN course 
ON student.id = course.student_id





LEFT JOIN
Returns all records from the left table and matched from right table

SELECT * FROM student 
LEFT JOIN course 
ON student.id = course.student_id



RIGHT JOIN
Returns all records from the right table and matched from left table

SELECT * FROM student 
RIGHT JOIN course 
ON student.id = course.student_id



FULL JOIN
Returns all records when there is a match in either left table or right table

SELECT * FROM student 
LEFT JOIN course 
ON student.id = course.student_id
UNION
RIGHT JOIN course 
ON student.id = course.student_id



Union

  Union used to combine the result-set of two or more SELECT statements . 
UNION  returns only unique values 
UNION ALL returns all values

SELECT * from table_a 
UNION 
SELECT * from table_b




Sub query

*find the students who scored more then class's average score 

SELECT name, mark FROM student
WHERE mark > ( SELECT AVG(mark) FROM student)



*find highest number scored by delhi's students

SELECT MAX(mark) FROM ( SELECT * FROM student WHERE city = 'delhi') as temp_student



*Another one

SELECT employee_id, first_name
FROM employees
WHERE department_id IN (SELECT department_id FROM departments WHERE location = 'New York');






Relationship 

One-to-One (1:1) Relationship:

In a one-to-one relationship, each record in the first table is related to only one record in the second table, and vice versa.

Example: Consider a table of employees where each employee has a unique social security number (SSN). You could have another table linking employees to their SSNs.

Table representation


Employee table =>

| EmployeeID | EmployeeName | SSN           |
|------------------|-----------------------|----------------|
| 1                  | John Doe          | 123-45-6789|
| 2                  | Jane Smith    | 987-65-4321   |


SSN table =>

| SSN                 | EmployeeID |
|---------------------|------------------|
| 123-45-6789    | 1                  |
| 987-65-4321    | 2                  |


One-to-Many (1:N) Relationship

In a one-to-many relationship, each record in the first table can be related to multiple records in the second table, but each record in the second table is related to only one record in the first table.

Example: Employees work in departments, so one department can have multiple employees.

Table representation


Department Table:

| DepartmentID | DepartmentName |
|--------------------|--------------------------|
| 101                 |            HR              |
| 102                 |            IT                |



Employees Table:

| EmployeeID | EmployeeName | DepartmentID |
|---------------|--------------------|-----------------|
| 1               | John Doe        | 101             |
| 2               | Jane Smith      | 101            |
| 3               | Bob Johnson   | 102            |




Many-to-Many (N:N) Relationship:

In a many-to-many relationship, records in both tables can be related to multiple records in the other table.

Example: Students can enrol in multiple courses, and each course can have multiple students.

Table representation:

Students Table:

| StudentID | StudentName |
|---------------|--------------------|
| 1               |         Alice       |
| 2               |        Bob         |
| 3               |        Carol       |


Courses Table:

| CourseID | CourseName    |
|--------------|----------------------|
| A             |         Math          |
| B             |       Science       |


Enrollment Table (Linking Table):

| StudentID | CourseID |
|---------------|--------------|
| 1               |      A        |
| 1               |      B        |
| 2               |      A        |
| 3               |      B        |


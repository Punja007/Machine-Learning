USE pre_sep;

SELECT * FROM student;

-- Aggregate Functions

SELECT COUNT(*) FROM student;

SELECT COUNT(*) AS No_of_rows FROM student;

SELECT MIN(marks) AS min_marks FROM student;

SELECT MAX(marks) AS max_marks FROM student;

SELECT AVG(marks) AS avg_marks FROM student;

SELECT SUM(marks) FROM student;

SELECT * FROM student WHERE marks = (SELECT MIN(marks) FROM student);


-- Clauses

SELECT * FROM student WHERE marks < 90;

SELECT * FROM student WHERE age <= 23;

SELECT * FROM student WHERE city = 'Noida' AND marks >= 80;

SELECT * FROM student WHERE city = 'Noida' OR marks >= 80;

SELECT * FROM student WHERE marks BETWEEN 80 AND 90;


-- LIMIT

SELECT * FROM student WHERE city = 'Noida' OR marks >= 80; 

SELECT * FROM student WHERE city = 'Noida' OR marks >= 80 LIMIT 3; 

SELECT * FROM student 
WHERE city = 'Pune' OR marks >= 80 
LIMIT 3; 

-- ORDER BY 

















 



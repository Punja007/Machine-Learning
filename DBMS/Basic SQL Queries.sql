CREATE DATABASE pre_sep;

CREATE DATABASE IF NOT EXISTS tb_batch_2;

CREATE DATABASE tb_batch_2;

CREATE DATABASE IF NOT EXISTS sourav;

DROP DATABASE sourav1;

DROP DATABASE IF EXISTS sourav1;

DROP DATABASE IF EXISTS sourav;


SHOW DATABASES;

SHOW TABLES;

USE pre_sep;


-- Table Creation

CREATE TABLE student(

id TINYINT PRIMARY KEY,
name VARCHAR(30),
age INT, CHECK (age >= 18),
city VARCHAR(20) NOT NULL,
marks INT UNIQUE,
course VARCHAR(30) DEFAULT 'AI'

);


SELECT * FROM student;















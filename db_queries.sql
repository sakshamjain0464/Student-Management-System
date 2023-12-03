-- Creating Users Table
CREATE TABLE users (
    user_name VARCHAR(50) PRIMARY KEY,
    password VARCHAR(50) UNIQUE NOT NULL
);


-- Creating Course Table
CREATE TABLE courses (
    Course_ID VARCHAR(5) PRIMARY KEY,
    Course_Name VARCHAR(100) NOT NULL
);


-- Creating Student Table
CREATE TABLE student_details (
    Roll_NO VARCHAR(5) PRIMARY KEY,
    First_name VARCHAR(50),
    Last_name VARCHAR(50),
    Course_ID VARCHAR(5),
    CGPA INT CHECK (CGPA >= 0 AND CGPA <= 10),
    FOREIGN KEY (Course_ID) REFERENCES courses(Course_ID)
);




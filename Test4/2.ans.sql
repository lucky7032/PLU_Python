CREATE TABLE Student (
    StudentID INT PRIMARY KEY,
    Name VARCHAR(100),
    Course VARCHAR(50),
    Marks INT
);

INSERT INTO Student (StudentID, Name, Course, Marks) VALUES
(101, 'Rahul', 'Python', 80),
(102, 'Priya', 'Java', 75),
(103, 'Aman', 'Python', 90),
(104, 'Neha', 'SQL', 70);
SELECT * FROM Student;


SELECT Name, Marks FROM Student;

SELECT Course FROM Student;
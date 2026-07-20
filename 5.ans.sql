CREATE TABLE Employee (
    EmployeeID INT PRIMARY KEY,
    Name VARCHAR(100),
    DepartmentID INT
);

CREATE TABLE Department (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(100)
);

INSERT INTO Employee VALUES
(1, 'Rahul', 101),
(2, 'Priya', 102),
(3, 'Aman', 101);

INSERT INTO Department VALUES
(101, 'IT'),
(102, 'HR');

SELECT
    Employee.Name,
    Department.DepartmentName
FROM Employee
INNER JOIN Department
ON Employee.DepartmentID = Department.DepartmentID;
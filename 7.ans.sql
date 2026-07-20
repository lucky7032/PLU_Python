CREATE TABLE Employee (
    EmployeeID INT PRIMARY KEY,
    Name VARCHAR(100),
    Department VARCHAR(50),
    Salary INT
);

INSERT INTO Employee VALUES
(1, 'Rahul', 'IT', 65000),
(2, 'Priya', 'HR', 45000),
(3, 'Aman', 'IT', 70000);

CREATE VIEW HighSalaryEmployees AS
SELECT *
FROM Employee
WHERE Salary > 60000;

SELECT * FROM HighSalaryEmployees;
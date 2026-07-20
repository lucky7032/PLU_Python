CREATE TABLE Product (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100),
    Category VARCHAR(50),
    Price INT
);

INSERT INTO Product VALUES
(1,'Mouse','Electronics',800),
(2,'Laptop','Electronics',65000),
(3,'Chair','Furniture',4500),
(4,'Keyboard','Electronics',1200);

SELECT *
FROM Product
WHERE Price > 1000;

SELECT *
FROM Product
WHERE Category='Electronics';

SELECT *
FROM Product
WHERE ProductName='Laptop';
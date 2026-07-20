CREATE TABLE Orders (
    OrderID INT,
    CustomerName VARCHAR(100),
    OrderDate DATE,
    Amount INT
);

CREATE INDEX idx_OrderID
ON Orders(OrderID);

Benefit of Creating an Index:
An Index is used to improve the speed of data retrieval.
One benefit:
It makes SELECT queries faster by allowing the database to find rows quickly without scanning the entire table.
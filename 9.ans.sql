CREATE TABLE Book (
    BookID INT PRIMARY KEY,
    BookName VARCHAR(100),
    Author VARCHAR(100),
    Price INT
);

INSERT INTO Book VALUES
(1, 'Python Basics', 'John', 500),
(2, 'Learning SQL', 'David', 700);

DELIMITER $$

CREATE PROCEDURE GetBooks()
BEGIN
    SELECT * FROM Book;
END $$

DELIMITER ;

CALL GetBooks();

CREATE PROCEDURE GetBooks
AS
BEGIN
    SELECT * FROM Book;
END;

EXEC GetBooks;
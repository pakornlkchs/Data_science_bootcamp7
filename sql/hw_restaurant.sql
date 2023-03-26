.open restaurant.db

-- clear existing data in restaurant database
DROP TABLE customers;
DROP TABLE menus;
DROP TABLE branch;
DROP TABLE member;
DROP TABLE orders;

-- create customers table (1)
CREATE TABLE customers (
  customer_id INT UNIQUE,
  firstname TEXT,
  lastname TEXT,
  member_id INT
);

INSERT INTO customers VALUES
  (1, "John", "Lennon", 4),
  (2, "Sam", "Smith", 3),
  (3, "Tony", "Stark", 2),
  (4, "Peter", "Parker", 5),
  (5, "Captain", "America", 6);


-- create menus table (2)
CREATE TABLE menus (
  food_id INT,
  food_name TEXT,
  price REAL
);

INSERT INTO menus VALUES
  (1, "Pizza", 4.99),
  (2, "Donut", 0.99),
  (3, "Sausage", 2.99),
  (4, "Bread", 1.99),
  (5, "Icecream", 0.99),
  (6, "Coke", 0.99),
  (7, "Mineral water", 1.99);

-- create orders table (3)
CREATE TABLE orders (
  order_item INT,
  order_date TEXT,
  food_id INT,
  customer_id INT,
  branch_id INT,
  payment TEXT  
);

INSERT INTO orders VALUES
  (1, '2023-01-01', 3, 1, 1, "Cash"),
  (2, '2023-01-01', 5, 1, 1, "Cash"),
  (3, '2023-01-01', 1, 4, 2, "Transfer"),
  (4, '2023-01-02', 3, 5, 3, "Transfer"),
  (5, '2023-01-02', 7, 5, 3, "Transfer"),
  (6, '2023-01-02', 2, 2, 4, "Credit"),
  (7, '2023-01-02', 5, 2, 3, "Credit"),
  (8, '2023-01-02', 4, 3, 4, "Transfer"),
  (9, '2023-01-03', 1, 5, 1, "Credit"),
  (10, '2023-01-03', 6, 2, 3, "Cash"),
  (11, '2023-01-01', 3, 3, 5, "Credit")
  ;


-- create branch table(4)
CREATE TABLE branch (
  branch_id INT UNIQUE,
  city TEXT,
  country TEXT,
  continent TEXT,
  foundation TEXT
);

INSERT INTO branch VALUES
  (1, "Bangkok", "Thailand", "Asia", "1990"),
  (2, "Paris", "France", "Europe", "1995"),
  (3, "New york", "USA", "US", "1996"),
  (4, "Tokyo", "Japan", "Asia", "2000"),
  (5, "London", "England", "Europe", "2010");

-- create member table (5)
CREATE TABLE member (
  member_id INT UNIQUE,
  rank INT,
  discount REAL
);

INSERT INTO member VALUES
  (1, "None", 0),
  (2, "Silver", 0.05),
  (3, "Gold", 0.10),
  (4, "Platinum", 0.15),
  (5, "Diamond", 0.30),
  (6, "CEO", 1);

-- change display
.mode column
.header on

-- Who paid by credit card?
SELECT 
  DISTINCT c.firstname || " " || c.lastname AS fullname,
  orders.payment AS payment   
FROM orders
JOIN customers AS c
  ON orders.customer_id = c.customer_id
WHERE payment = 'Credit';

-- Who spend the most?
SELECT 
  customers.firstname || " " || customers.lastname AS fullname,
  SUM(menus.price) AS total_spend  
FROM orders
JOIN menus
  ON orders.food_id = menus.food_id
JOIN customers
  ON orders.customer_id = customers.customer_id
GROUP BY fullname
ORDER BY total_spend DESC;

-- Who spend the most when adding membership discount?
SELECT 
  discount_c.firstname || " " || discount_c.lastname AS fullname,
  SUM(menus.price) AS total_spend,
  discount_c.rank AS member,
  SUM(menus.price * (1 - discount_c.discount)) AS after_discount  
FROM orders
JOIN menus
  ON orders.food_id = menus.food_id
JOIN 
  (SELECT * 
   FROM customers
   JOIN member
    ON customers.member_id = member.member_id
  ) AS discount_c
  ON orders.customer_id = discount_c.customer_id
GROUP BY fullname
ORDER BY after_discount DESC;

-- Which country has total income lower than 3$ ?
SELECT 
  branch.country AS country,
  SUM(menus.price) AS total
FROM orders
JOIN branch
  ON orders.branch_id = branch.branch_id
JOIN menus
  ON orders.food_id = menus.food_id
GROUP BY country
HAVING total < 3
ORDER BY total;

-- Which food generate most income in each day?
WITH merge AS (
  SELECT *
  FROM orders
  JOIN menus
    ON orders.food_id = menus.food_id
)
  
SELECT 
  m.order_date AS date,
  m.food_name AS food,
  SUM(m.price) AS total
FROM merge AS m
GROUP BY date, food
ORDER BY date ASC, total DESC

-- Create a fresh database
DROP SCHEMA IF EXISTS sales_db;

CREATE SCHEMA sales_db;

USE sales_db;

-- 1. Create the customers table
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100)
);

-- 2. Create the products table
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    price DECIMAL(10, 2)
);

-- 3. Create the central orders table with foreign keys
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Insert data
INSERT INTO
    customers
VALUES
    (1, 'Alice'),
    (2, 'Bob');

INSERT INTO
    products
VALUES
    (101, 'Laptop', 1200.00),
    (102, 'Mouse', 25.00);

INSERT INTO
    orders
VALUES
    (1, 1, 101, 1),
    (2, 1, 102, 2),
    (3, 2, 101, 1);

SELECT
    c.customer_name,
    p.product_name,
    o.quantity
FROM
    customers c
    INNER JOIN orders o ON c.customer_id = o.customer_id -- Bridge 1: customers -> orders
    INNER JOIN products p ON o.product_id = p.product_id;
-- Bridge 2: orders -> products
drop schema if exists practice;

-- delete the practice schema if it exists
create schema practice;

use practice;

create table customers (
    id int primary key,
    name varchar(50),
    city varchar(50)
);

create table orders (
    o_id int primary key,
    c_id int,
    product varchar(50)
);

insert into
    customers (id, name, city)
values
    (1, 'Alice', 'New York'),
    (2, 'Bob', 'Los Angeles'),
    (3, 'Charlie', 'Chicago');

insert into
    orders (o_id, c_id, product)
values
    (101, 1, 'Laptop'),
    (102, 2, 'Smartphone'),
    (103, 3, 'Tablet');

SELECT
    customers.id AS cid,
    customers.city AS city,
    orders.o_id AS orid
FROM
    customers
INNER JOIN orders ON customers.id = orders.c_id;

-- on is the bridge that connects the two tables
-- this is an inner join, it will only show the records that have matching ids in both tables. here, customers.id is matching with the orders.c_id(which is the customer id stored in orders table)

-- insert into orders (o_id, c_id, product) values (104, 5, 'Monitor');
insert into customers (id, name, city) values (4, 'Daisy', 'Miami');

select
    c.id,
    c.name,
    o.o_id,
    o.product
from
    customers c  -- This is the LEFT table, so no matter what it will show every row from this table.
left join
    orders o
on c.id = o.c_id;
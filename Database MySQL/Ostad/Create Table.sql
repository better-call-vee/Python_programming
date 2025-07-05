DROP SCHEMA IF EXISTS test;
create schema Sunny_db;
use Sunny_db;

-- Table for grandfather and his siblings
CREATE TABLE grandfather (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);


INSERT INTO grandfather VALUES
(2, 'Abdul Rahim'),
(3, 'Abdul Kibria'),
(4, 'Abdul Kashem'),
(5, 'Abdul Kashem');


select * from grandfather;


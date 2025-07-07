drop database if exists company_db;

create database if not exists company_db;

use company_db;

CREATE TABLE google_salaries (
    id INT NOT NULL,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    department VARCHAR(255),
    education VARCHAR(255),
    salary INT,
    PRIMARY KEY (id)
);

set
    global local_infile = true;

LOAD DATA LOCAL INFILE 'D:/Python_programming/Database MySQL/google_salaries-sum-groupby/google_salaries.csv' INTO TABLE google_salaries FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS;

-- This will load the data from the CSV file into the google_salaries table.
select
    *
from
    google_salaries
where
    salary > 50000;

select
    first_name,
    department,
    education
from
    google_salaries
where
    first_name LIKE 'Ma%';

-- whose name start with Ma...
SELECT
    DISTINCT -- selecting unique entries
    department
FROM
    google_salaries;

select
    education,
    SUM(salary) as total_salary
from
    google_salaries
group by
    education -- same way AVG(), MIN(), MAX() can be used
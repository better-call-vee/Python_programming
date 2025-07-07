-- This creates a fresh, empty database to work in
drop schema if exists family_db;

create schema family_db;

use family_db;

-- Table for the main grandfather
create table grandfather (
    id int primary key,
    name varchar(100)
);

-- Table for all of his siblings
create table grandfather_siblings (
    id int primary key,
    grandparent_id int,
    -- This is the Foreign Key linking to grandfather.id
    name varchar(100),
    gender enum('Male', 'Female') -- enumeration. like MCQ.  telling the database that any value inserted into the gender column must be either 'Male' or 'Female'.
);

-- Insert the grandfather
insert into
    grandfather
values
    (1, 'Abdul Karim');

-- Insert all of his siblings, linking them back to the grandfather with id = 1
insert into
    grandfather_siblings
values
    (101, 1, 'Habibur Rahman', 'Male'),
    (102, 1, 'Jabed Ali', 'Male'),
    (103, 1, 'Nazma Khatun', 'Female'),
    (104, 1, 'Farida Begum', 'Female'),
    (105, 1, 'Sultan Mahmud', 'Male'),
    (106, 1, 'Anisur Rahman', 'Male'),
    (107, 1, 'Shamsun Nahar', 'Female'),
    (108, 1, 'Tariqul Islam', 'Male'),
    (109, 1, 'Rezaul Karim', 'Male'),
    (110, 1, 'Hasina Akter', 'Female');

-- here, if we want to see the siblings of grandfather, we can use a join. but there is a calma with the on. 
select
    ak.name,
    count(gs.id) as number_of_siblings
from
    grandfather ak
    left join grandfather_siblings gs on ak.id = gs.grandparent_id -- we have to match the id of the grandfather table with the grandparent_id of the siblings table
group by
    ak.id,
    ak.name;

-- It's best practice to group by all non-summarized columns to avoid ambiguity
having
    count(gs.id) > 5;

-- Filter the final groups. who have more than 5 siblings using 'having'
select
    ak.name,
    gs.gender,
    count(gs.id) as number_of_male_siblings
from
    grandfather ak
    left join grandfather_siblings gs on ak.id = gs.grandparent_id
where
    gs.gender == "Male" -- where always goes after from and join
group by
    ak.id,
    ak.name;

having
    count(gs.id) > 3;
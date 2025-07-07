drop schema if exists vee1;

create schema vee1;

USE vee1;

/*
 int is the data type here.
 
 primary key is the most important thing.
 - must be unique, id is good for it
 - can't be empty
 
 varchar is a data type for text. 100 = maximum length for the text (VARiable CHARacter)
 */
CREATE TABLE granny (id int primary key, name VARCHAR(100));

insert into
    granny
values
    (2, 'iyakub sardar'),
    (3, 'alimul jahiba'),
    (4, 'abdul azim'),
    (21, 'alimul jahiba');

-- this will cause an error. primary key will be unique. we can't insert further
-- insert into granny values (2, 'ALLAH nobijir naam');
-- showing the data in table and filtering them
select
    *
from
    granny;

select
    *
from
    granny
where
    id = 3;

select
    *
from
    granny
where
    name = "abdul azim";

select
    *
from
    granny
order by
    name;

-- alphabetical sorting
select
    *
from
    granny
order by
    id desc;

-- sorting order modification, we can also use asc
SELECT
    *
FROM
    granny
WHERE
    name = 'alimul jahiba'
ORDER BY
    id DESC;

/*
 1NF rule.
 Using only one single data for a column.
 1 - Vee - 'Music, Coding'    == this is not 1NF(First Normal Form), data will be hard to 
 manage and organize
 id  name   hobby1    hobby2
 but 1 - Vee - 'Music' - 'Coding'
 1NF. perfect
 */
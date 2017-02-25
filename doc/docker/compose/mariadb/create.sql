CREATE TABLE people (
 id int auto_increment primary key,
 name varchar(50),
 salary real,
 born date
);

INSERT INTO people (name, salary, born) VALUES
 ('Ala',  20800, '1990-09-20'),
 ('Alan', 21600, '1989-10-20'),
 ('Anna', 22500, '1988-11-15'),
 ('Lala', 23500, '1987-12-01'),
 ('Leo',  22100, '1986-05-13');

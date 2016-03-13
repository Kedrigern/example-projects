# SQL

Je univerzální dotazovací jazyk pro databáze. Naneštěstí každá DB používá mírně jiný dialekt.


## Základní

```
CREATE DATABASE dbname;
```

```
CREATE TABLE table_name
(
column_name1 data_type(size),
column_name2 data_type(size),
column_name3 data_type(size),
....
);
```

```
INSERT INTO table_name
VALUES (value1,value2,value3,...);
```

```
INSERT INTO table_name (column1,column2,column3,...)
VALUES (value1,value2,value3,...);
```

```
SELECT * FROM `table` ORDER BY `col` desc
```

## Where

```
SELECT * FROM `table` WHERE `colname` LIKE '%,0%'
```

## Tipy

Nahrazení v celém sloupci:
```
UPDATE `table` SET `col_name` = REPLACE(`col_name`, ' ', '')
```


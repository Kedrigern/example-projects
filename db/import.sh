#!/usr/bin/env bash

file="data.csv"
user=""
db=""
table=""
host="localhost"

mysql -u $user -p -h $host $db << EOF
DROP TABLE IF EXISTS $table;

CREATE TABLE $table (
  cislo int NOT NULL,
  castka decimal(12,2) NOT NULL,
  textik varchar(120) NOT NULL,
  datum1 date NOT NULL,
  datum2 varchar(20) NOT NULL
);

LOAD DATA LOCAL INFILE '$file' INTO TABLE $table COLUMNS TERMINATED BY ';' ENCLOSED BY '"' IGNORE 1 LINES 
(cislo, castka, textik, datum1, @var_datum2)
set datum2 = STR_TO_DATE(@var_datum2, '%d.%m.%y');
EOF

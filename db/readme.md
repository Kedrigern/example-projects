# Databáze

- SQL
  - [PostgreSQL](postgres.md)
  - [MySQL](mysql.md)
  - [SQLite](sqlite.md)
- [ldap](ldap/readme.md)
- [neo4j](neo4j/readme.md)

# SQL

Je univerzální dotazovací jazyk pro relační databáze. Naneštěstí každá DB používá mírně jiný dialekt.

## Basic interact

<table>
  <thead>
    <tr>
      <th rowspan=2>What</th>
      <th colspan=3>Command</th>
      <th rowspan=2>Note</th>
    </tr>
    <tr>
      <th>psql</th>
      <th>mysql</th>
      <th>SQLite</th>
    </tr>
  </thead>
  <tbody>
  <tr>
    <td>Port</td>
    <td>5432</td>
    <td>3306</td>
    <td />
    <td />
  </tr>
    <tr>
      <td>Connect server</td>
      <td>psql</td>
      <td>mysql -u &lt;user&gt; -p</td>
      <td>sqlite3 mydb.db</td>
      <td />
    </tr>
    <tr>
      <td>Shell</td>
      <td>\! &lt;cmd&gt;</td>
      <td>\! &lt;cmd&gt;</td>
      <td />
      <td />
    </tr>
    <tr>
      <td>Load file</td>
      <td>\i &lt;filename&gt;.sql</td>
      <td>\\. &lt;filename&gt;.sql</td>
      <td>.read &lt;filename&gt;.sql</td>
      <td />
    </tr>
    <tr>
      <td>List DB</td>
      <td>\l</td>
      <td>show databases;</td>
      <td />
      <td />
    </tr>
    <tr>
      <td>Connect DB</td>
      <td>\c &lt;db&gt;</td>
      <td>use &lt;db&gt;;</td>
      <td />
      <td>\c = connect</td>
    </tr>
    <tr>
      <td>Help</td>
      <td>\h</td>
      <td>help</td>
      <td>.help</td>
      <td></td>
    </tr>
    <tr>
      <td>List table</td>
      <td>\dt</td>
      <td>show tables;</td>
      <td>.tables</td>
      <td/>
    </tr>
    <tr>
      <td>Describe table</td>
      <td>\d &lt;table&gt;</td>
      <td>DESCRIBE &lt;table&gt;;</td>
      <td>.schema &lt;table&gt;</td>
      <td/>
    </tr>
    <tr>
      <td>Describe index</td>
      <td>\di</td>
      <td>SHOW INDEX FROM &lt;table&gt;;</td>
      <td/>
      <td/>
    </tr>
  </tbody>
</table>

## SQL

Budeme pracovat s ukázkovou tabulkou:

|id | name | salary | born       |
|---|------|--------|------------|
| 1 | Ala  | 20 800 | 1990-09-20 |
| 2 | Alan | 21 600 | 1989-10-20 |
| 3 | Anna | 22 500 | 1988-11-15 |
| 4 | Lala | 23 500 | 1987-12-01 |
| 5 | Leo  | 22 100 | 1986-05-13 |

### Create DB and insert

```sql
CREATE TABLE people (
 id serial primary key,
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
```

U MySQL je třeba nahradit typ `serial` za `int` (autoincrement je doplněn automaticky).

### Import a Export csv

<table>
  <thead>
    <tr>
      <th>cmd</th><th>psql</th><th>mysql</th><th>sqlite</th>
    </tr>
  </thead>
  <tr>
    <td>import</td>
    <td><code>\COPY people FROM 'data.csv' WITH CSV HEADER;</code></td>
    <td><code>
    LOAD DATA INFILE "data.csv" INTO TABLE people IGNORE 1 LINES;</code></td>
    <td><code>.separator ","
    .import data.csv people</code></td>
  </tr>
  <tr>
    <td>export</td>
    <td><code>\COPY people TO 'data2.csv' WITH CSV HEADER;</code></td>
    <td><code>mysql -e 'select * from people' -B > data2.tsv</code></td>
    <td><code>.mode csv
    .output data2.csv</code></td>
  </tr>
  <tr>
    <td>note</td>
    <td>
    <code>COPY</code> je interní, běží na DB stroji, zatímco <code>\COPY</code> běží pod userem s kterého jsme připojeni (který zadal <code>psql</code>).
    </td>
    <td>
    U MySQL je třeba nastavit příslušná práva uživateli: <code>grant file on *.* to keddie identified by 'keddie';</code>
    </td>
    <td/>
  </tr>
</table>

### Select

```sql
SELECT * FROM people ORDER BY salary DESC;

SELECT * FROM people WHERE name LIKE 'Ala%';
SELECT * FROM people WHERE name LIKE 'Ala_';
SELECT * FROM people WHERE name LIKE '%la%';

SELECT * FROM people WHERE born < '1987-01-01';
SELECT * FROM people WHERE born BETWEEN '1987-01-01' AND '1989-01-01';
```

### Update

```sql
UPDATE people SET salary = 22900 WHERE id = 5;
UPDATE people SET id = id + 100;
```

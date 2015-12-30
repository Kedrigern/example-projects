
SQLite
======

Je DB, která je uchována v jednom souboru (`*.db`).

Příkazy
-------

Ovládá se pomocí SQL. Příkazy mimo DB začínají . na začátku.

```
.separator ","
.import <file>.csv <table>
```

```
.mode csv
.output <file>.csv
```

```
.help
.quit
```

Příklad
-------

Integrace Python
----------------

```python
import sqlite3

conn = sqlite3.connect('<file>.db')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
```

```python
# Never do this -- insecure!
symbol = 'RHAT'
c.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)

# Do this instead
t = ('RHAT',)
c.execute('SELECT * FROM stocks WHERE symbol=?', t)
```

Integrace PHP
-------------

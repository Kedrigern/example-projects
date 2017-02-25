#PostgREST

PostgREST je velmi mocný nástroj, který automaticky tvoří k Postgre DB JSON api.

Konfig:
```
# postgrest.conf

# The standard connection URI format, documented at
# https://www.postgresql.org/docs/current/static/libpq-connect.html#AEN45347
db-uri       = "postgres://user:pass@host:5432/dbname"

# The name of which database schema to expose to REST clients
db-schema    = "api"

# The database role to use when no client authentication is provided.
# Can (and probably should) differ from user in db-uri
db-anon-role = "anon"

server-port = 3001
```

Spustíme:
`./postgrest postgrest.conf`

A následně přistpoumí třeba z webového prohlížeče: `http://localhost:3001/people?select=id,%20name,salary&order=salary` nebo z pythonu:

```python
import requests
url = 'http://localhost:3001/people'
response = requests.get(url)
response = requests.get(url, params={'select': 'id,salary', 'order': 'salary'})
```

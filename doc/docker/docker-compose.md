# Docker compose

```bash
sudo docker-compose -f definition.yaml up -d
```

## docker-compose.yaml

Je soubor, kterým se konfiguruje celá struktura containerů:

```yaml
version: '2'

services:
  db:
    image: mariadb:10.1
    restart: always
    environment:
      MYSQL_DATABASE: redmine
      MYSQL_USER: redmine
      MYSQL_PASSWORD: redmine
      MYSQL_ROOT_PASSWORD: redmine
  redmine:
    depends_on:
      - db
    image: sameersbn/redmine:3.3.0-4
    restart: always
    ports:
      - 3300:80
    environment:
      REDMINE_PORT: 80
      REDMINE_HTTPS: 0
      DB_TYPE: mysql
      DB_ADAPTER: mysql2
      DB_HOST: db
      DB_NAME: redmine
      DB_USER: redmine
      DB_PASS: redmine
```

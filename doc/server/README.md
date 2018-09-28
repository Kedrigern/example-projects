Nastavení základní VPS.

# 1\. Prerekvizity

1. Pořídíme VPS, např. od [VPS free](https://vpsfree.cz/). Zde si můžeme v rámci playground zřídit i dočasný server nad rámec plánu.
2. Jako OS jsem zvolil Ubuntu 18.04 LTS
3. Máme domenu. Já mám např. [profant.eu](https://www.profant.eu). A některé subdomeny směřuji na daný server. Na cloudflare to vypadá takto:
  
  | Type | Name | Value | TTL |
  |------|------|-------|-----|
  | A    | test | points to `ip` | Automatic |

# 2\. Prepare OS

```bash
apt update
apt install ufw apache2 ffmpeg zip postgresql php libapache2-mod-php php-mysql php-pgsql \
php-fpm php-gd php-json php-curl php-mbstring php-intl php-imagick php-xml php-zip php-log php-bz2 php-gmp php-memcached php-redis
```

- php-**mcrypt** je obsolete
- stává se mi, že instalace postgresql zamrzne okolo 96%, ale v reálu se vše v pořádku nainstaluje
- [Ubuntu 18 package web browser](https://packages.ubuntu.com/)

# 3. Apache: basic

Vše by mělo ihned v pořádku běžet. Pokud zadáme IP adresu serveru do browseru, tak uvidíme default welcome page.

# 4\. Source code

Vytvoříme `/var/www/test/index.php`:

```html
<!doctype html>
<html>
        <head>
                <meta charset="utf-8">
                <title>DB a virtualhost test</title>
        </head>
        <body>
        <h1>DB and virtualhost test</h1>
<?php
echo("<p>php!</p>\n");

$host        = "host = 127.0.0.1";
$port        = "port = 5432";
$dbname      = "dbname = ptest
$credentials = "user = ptest password=ptest";

$db = pg_connect( "$host $port $dbname $credentials"  );
if(!$db) {
      echo("Error : Unable to open database\n");
} else {
      echo("<p>Opened database successfully</p>\n");
}
?>
</body>
</html>
```

# 5\. Apache: virtualhost and php

1. **Zkopírujeme** soubor `000-default.conf`: 
    ```cp /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-available/010-test.conf```
2. **Přepíšeme** `010-test.conf`: 
  ```
  ServerName test.profant.eu
  DocumentRoot /var/www/test
  ```
3. **Aktivujeme** pomocí symlinku:
    ```ln -s /etc/apache2/sites-available/010-test.conf /etc/apache2/sites-enabled/010-test.conf```
4. **Vyzkoušíme** v prohlížeči, např. `test.profant.eu`, zatím se nepůjde připojit k DB.

# 6\. Postgresql

Otestujeme, že se umíme lokálně připojit k postgre:

```
sudo -u postgres psql
\q
```

Obecně operace s DB provádíme pod tímto uživatelem. Vytvoříme usera a k němu příslušnou DB:

```
createuser
createdb <username>
```

Následně potřebujeme ještě stejně pojmenovaného usera v systému:

```
sudo adduser <username>
```

https://github.com/Kedrigern/example-projects/tree/master/db



# 7\. SSL

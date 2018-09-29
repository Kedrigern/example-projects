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
apt upgrade
apt install ufw apache2 ffmpeg zip postgresql php libapache2-mod-php php-mysql php-pgsql \
php-fpm php-gd php-json php-curl php-mbstring php-intl php-imagick php-xml php-zip php-log php-bz2 php-gmp php-memcached php-redis
```
- zamrzá mi post install script u postgres
- php-**mcrypt** je obsolete
- [Ubuntu 18 package web browser](https://packages.ubuntu.com/)

# 3. Apache: basic

Vše by mělo ihned v pořádku běžet. Pokud zadáme IP adresu serveru do browseru, tak uvidíme default welcome page.

Aktivujeme modyly:

```
a2enmod rewrite
a2enmod headers
systemctl restart apache2
```

# 4\. Source code

```
mkdir /var/www/test
chown -R  www-data:www-data test/
touch /var/www/test/index.php
```

Soubor `index.php` má následující obsah:

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
echo("<p>PHP jede!</p>\n");

$host        = "host = 127.0.0.1";
$port        = "port = 5432";
$dbname      = "dbname = ptest";
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

# 5\. Apache: virtualhost, php, httaccess

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

TODO: httaccess

# 6\. Postgresql

Otestujeme, že se umíme lokálně připojit k postgre:

```
sudo -u postgres psql
\q
```

Obecně operace s DB provádíme pod tímto uživatelem. 

Vytvoříme usera a k němu příslušnou DB:

```
createuser ptest
createdb ptest
```

Následně potřebujeme ještě stejně pojmenovaného usera v systému:

```
sudo adduser <username>
```

A nastavíme heslo:
```
su ptest
psql
\password
```

https://github.com/Kedrigern/example-projects/tree/master/db



# 7\. SSL

Pro využití let's encrypt potřebujeme cerbota:

```
apt-get install software-properties-common
add-apt-repository ppa:certbot/certbot
apt update 
apt install python-certbot-apache
certbot --apache # nás provede instalací (sám rozpozná virtualhost apod)
```

Ještě je dobré vyzkoušet: `certbot renew --dry-run` aby nám správně chodilo automatické přegenerování certifikátu.


# Odkazy

Digital ocean:
- [LAMP](https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-ubuntu-18-04)
- [UFW](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-18-04)
- [Postgres](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04)
- [Lets Encrypt](https://www.digitalocean.com/community/tutorials/how-to-secure-apache-with-let-s-encrypt-on-ubuntu-18-04)

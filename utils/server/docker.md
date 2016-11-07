
Docker
======

Je jedním z nejrozšířenějších containerovacích systémů (popř. též os level virtualization). Využívá k tomu základní nástroje obsažené přímo v kernelu Linuxu (namespace, cgroups, ...). V praxi je důležité, že každý container využivá kernel hosta, popř. dokonce i základní knihovny.

Kontejner si nese knihovny a samotnou aplikaci (vlastně se chová jako složitější binárka). Tím pádem nám odpadají různá dependecy hell. Např. kompilování nativ modulů v Pythonu a instalace věcí z pipu.

Kontejnery mají vlastní síť a Docker nám dovoluje jí docela lehce ovládat. Dovolí nám snadno vystrčit porty na hosta (čili webová aplikace v kontejneru vám chodí na localhostu), dovolí nám umístit některé kontejnery do stejné sítě.

Pozor na rozdíl mezi obraz (image) a container. Container je instancí obrazu.
Obdobný vztah jako soubor (binárka) vs proces.

Docker image má vrstvy. Ty jsou read-only. Díky tomu stahuje vrsty právě jednou. Např. když stáhnete dva kontejnery založené na fedoře, tak základní kontejner Fedory (resp. i jeho vrstvy) se stáhne jen jednou.

Běžící kontejner má volumes. To jsou speciální složky v questu u kterých se počítá, že se do nich zapisuje a že je budeme chtít mít persistentní.

**Persistentní uložiště** (volume): namountované složky, které jsou persistentní mezi běhy. Mohou být:
 * nepojmenované: vytvoří se složka ve `/var/lib/docker/volumes/`, ale bude pojmenavaná hashem
 * pojmenovaný: vytvoří se pojmenovaná složka ve `/var/lib/docker/volumes/`
 * mountovaný: využije se konkrétně zadaná složka v hostovi


Ovládání
--------

Jedná se o běžného démona: `service docker start`


| Cmd         | Parametry           | Popis                        |
|-------------|---------------------|------------------------------|
| **cp**      | container:path path | zkopíruje soubor z hosta     |
| **images**  |                     | nainstalované obrazy         |
| **inspect** | `<container_id>`    | podrobnosti o kontejneru     |
| **logs**    |                     | std. výstup kontjneru        |
| **network** | create, rm, ls, ... | ovládá síťování              |
| **ps**      | `-a` vypnuté, `-l`  | výpis běžících kontjnerů     |
| **pull**    | `<image>:<version>` | stáhne obraz                 |
| **rename**  | `<old> <new>`       | přejmenuje                   |
| **restart** | `<container_id>`    | restaruje                    |
| **rm**      | `<container_id>`    | smaže kontejner              |
| **rmi**     | `<image_id>`        | smaže obraz                  |
| **run**     | `<image_id>`        | zapne image, viz dále        |
| **search**  | `<string>`          | vyhledává na `hub.docker.io` |
| **start**   | `<container_id>`    | nastartuje kontejner         |
| **stats**   |                     |                              |
| **stop**    | `<container_id>`    | zastaví kontejner            |
| **volume**  |                     | zobrazí volumes              |


### Run

`docker run <image> <command>`, kde command je např. `/bin/echo "Hello world"`.

`docker run -ti <image> /bin/bash` spustí interaktivní shell.

`-d` zapne container jako démona a vrátí nám container ID.

`-p` namapuje porty, mapuje na rozsah 49153-65535. 
Můžeme předat jako argument `-p <vnější>:<vnitřní>` (typicky třeba `-p 8182:80`).
Zjistit namapování lze například pomocí `docker ps -l` nebo `docker port <image>`

`-v <host/path>:<container/path>` připojí nějaký svazek (třeba data DB, log). 
Tím pádem na původním systému máme data a logy a v dockeru běží jen aplikace.

`--restart [always|no|on-failure[:max-retries] ]` na testování se tedy hodi `no`,
zatímco na produkci `always`.

Jednoduchý příklad:

```
sudo docker run --rm -p 8181:80 nginx:stable-alpine
```

A následně v prohlížeči zadáme `localhost:8181`

## Networking

### Přímé linkování

Kontejnery lze přímo linkovat. To už je silně nedoporučená metoda.

### Net

Lze vytvářet přímo sítě v kterých je několik docker kontejnerů:

```
docker network create my-net
docker run --net my-net --net-alias mysql -e MYSQL_ROOT_PASSWORD=pw mariadb:10.1
docker run --net my net --net-alias wp -p 8080:80 -e WORDPRESS_DB_PASSWORD=pw  wordpress:4.6
```

### Tipy

#### Záloha DB


```bash
# Spustíme mysql container:
docker run --name mysql -d sameersbn/mysql:latest

# Práce s mysql containerem (linkování s dalšími containery etc.)
# ...
# Záloha:
docker run -it --rm --volumes-from=mysql sameersbn/mysql:latest mysqldump <db> <table> > dump.sql
# Při použití parametru -rm se dumpovací container ihned po použití smaže
# dump.sql bude uložen na hostu
```

Popřípadě přístup k konzoli DB:

```
docker run -it --rm --volumes-from=mysql sameersbn/mysql:latest mysql -uroot
```

Spuštění mysql skriptu:
```
touch example.sql
docker run -it --rm --volumes-from=mysql -v $PWD:/host sameersbn/mysql:latest mysql -uroot --default-character-set=utf8 -e "source /host/example.sql"
```


Obrazy
------

V centrálním repozitáři obrazů (hubu) je předpřipraveno mnoho obrazů. Velmi příjemné jsou různé linuxové distribuce. Nicméně máme zde samozřejmě i DB ([MySQL][mysql], [PostgreSQL][postgre]). A hotové aplikace ([Redmine][redmine], [ODOO][odoo], Helios). Výhodou je, že můžeme transparentně používat uložiště mimo docker image a vývojáři se starají opravdu jen o sladění komponent. Zatímco admin se stará o zálohu dat, místo na disku, porty etc.


Údržba
------

Pokud s dockerem více experimentujete, tak se vám začnou hromadit obrazy i containery.

```bash
> docker ps -a
CONTAINER ID   IMAGE         COMMAND      CREATED             STATUS                         PORTS                    NAMES
9f7e465dd3be   neo4j/neo4j   "/neo4j.sh"  About an hour ago   Restarting (0) 1 seconds ago   0.0.0.0:8475->7473/tcp   neo4j
> docker rm -f 9f7e465dd3be
> # nebo 
> docker rm neo4j 
> docker images
REPOSITORY              TAG      IMAGE ID         CREATED           VIRTUAL SIZE
docker.io/neo4j/neo4j   latest   5aff38694e3d     8 weeks ago       880.8 MB
> docker rmi 5aff38694e3d
```

Instalace
---------

Verze z repozitářů:

| Disribuce       | Verze  |
|-----------------|-------:|
| Fedora 24       | 1.10.3 |
| Debian 8 Jessie |  1.3.2 |
| CoreOS          |  1.6.2 |
| Ubuntu 14.10 UU |  1.2.0 |


Příklady a tipy
---------------

### Lokální přístup

Container můžeme používat i na běžném localhostu.

Pokud použijeme:

```
docker run -d --name mysql -p 127.0.0.1:3306:3306 sameersbn/mysql:latest
```

namísto:

```
docker run -d --name mysql -p 3306:3306 sameersbn/mysql:latest
```

tak se k DB můžeme připojit na klasickém portu. Čili např. přes MySQL Workbench. Což nám jistě usnadní vývoj. A zároveň můžeme DB stále držet izolované. [Zdroj][s1].


Další
-----

* docker řízený skrz `systemd`: [doc][systemd]
* [linkování kontejnerů][link]
* [příklad s OwnCloud][exOwnCloud]
* [CoreOS][] - distribuce přímo navržená pro provoz Dockeru (včetně decentralizace etc).



[redmine]: https://registry.hub.docker.com/u/sameersbn/redmine/
[mysql]: https://github.com/sameersbn/docker-mysql
[postgre]: https://github.com/sameersbn/docker-postgresql
[mysql]: https://github.com/sameersbn/docker-mysql
[odoo]: https://registry.hub.docker.com/u/xcgd/odoo/
[systemd]: https://docs.docker.com/articles/systemd/
[link]: https://docs.docker.com/articles/ambassador_pattern_linking/
[exOwnCloud]: http://dischord.org/blog/2013/07/10/docker-and-owncloud/  
[s1]: http://serverfault.com/questions/565294/why-does-a-docker-container-running-a-server-expose-port-to-the-outside-world-ev
[coreos]: https://coreos.com

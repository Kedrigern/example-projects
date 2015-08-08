Docker
======

Je systém pro izolaci aplikací pomocí lehkých vláken, cgroups etc. v Linuxu. Všichni používají kernel hosta, ale zbytek (plus zdroje - porty, file descriptory) je již izolován. To se velmi hodí pro různorodé webové aplikace, které potřebují různé verze Rails, Pythonů, DB, PHP etc. Výhodou je, že každý programátor si může integrovat na OS, které má rád a pak se udělá jednoduchý deployment. 

2 části:

 * daemon: stará se o běh klientů
 * client

Pozor na rozdíl mezi obraz (image) a container.
Container je instancí obrazu.

Ovládání
--------

Jedná se o běžného démona: `service docker start`

Vyhledání obrazu: `docker search <string>`

Stažení obrazu: `docker pull learn/tutorial`

Nainstalované obrazy: `docker images`

Běžící containery: `docker ps` s `-a` i vypnuté.


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


### Další příkazy

`ps` procesy / seznam běžících container, má běžné přepínače jako `-l`, `-a` (i neběžící obrazy).

`logs` stdout containeru

`stop` zastaví container



### Tipy


#### Zkopírování souborů

Zkopírování souborů z containaru do hostu (např. získání konfiguráku):

```
{host} docker run -v /path/to/hostdir:/mnt --name my_container my_image
{host} docker exec -it my_container bash
{container} cp /mnt/sourcefile /path/to/destfile
```


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

| Disribuce       | Verze |
|-----------------|-------|
| Fedora 22	  | 1.7.1 |
| Fedora 21       | 1.4.0 |
| Debian 8 Jessie | 1.3.2 |
| CoreOS          | 1.6.2 |
| Ubuntu 14.10 UU | 1.2.0 |


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

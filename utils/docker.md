Docker
======

Je systém pro izolaci aplikací pomocí lehkých vláken, cgroups etc. v Linuxu. Všichni používají kernel hosta, ale zbytek (plus zdroje - porty, file descriptory) je již izolován. To se velmi hodí pro různorodé webové aplikace, které potřebují různé verze Rails, Pythonů, DB, PHP etc. Výhodou je, že každý programátor si může integrovat na OS, které má rád a pak se udělá jednoduchý deployment. 

2 části:

 * daemon: stará se o běh klientů
 * client

## Ovládání

Vyhledání obrazu:
```docker search <string>```

Stažení obrazu: 
```docker pull learn/tutorial```

Nainstalované obrazy:
```docker images```


### Run

`docker run <image> <command>`, kde command je např. `/bin/echo "Hello world"`.

`docker run -ti <image> /bin/bash` spustí interaktivní shell.

`-d` zapne container jako démona a vrátí nám container ID.

`-p` namapuje porty, mapuje na rozsah 49153-65535. Můžeme předat jako argument `-p <containerPort>:<hostPort>`. Zjistit namapování lze například pomocí `docker ps -l` nebo `docker port <image>`

`-v <host/path>:<container/path>` připojí nějaký svazek (třeba data DB, log). 
Tím pádem na původním systému máme data a logy a v dockeru běží jen aplikace.

### Další příkazy
`ps` procesy / seznam běžících container, má běžné přepínače jako `-l`, `-a` (i neběžící obrazy).

`logs` stdout containeru

`stop` zastaví container

## Obrazy

V centrálním repozitáři obrazů (hubu) je předpřipraveno mnoho obrazů. Velmi příjemné jsou různé linuxové distribuce. Nicméně máme zde samozřejmě i DB ([MySQL][mysql], [PostgreSQL][posgre]). A hotové aplikace ([Redmine][redmine], [ODOO][odoo], Helios). Výhodou je, že můžeme transparentně používat uložiště mimo docker image a vývojáři se starají opravdu jen o sladění komponent. Zatímco admin se stará o zálohu dat, místo na disku, porty etc.

## Instalace

Verze z repozitářů:

| Disribuce       | Verze |
|-----------------|-------|
| Fedora 21       | 1.4.0 |
| Debian 8 Jessie | 1.3.2 |
| CoreOS          | 1.3.3 |
| Ubuntu 14.10 UU | 1.2.0 |


[redmine]: https://registry.hub.docker.com/u/sameersbn/redmine/
[mysql]: https://github.com/sameersbn/docker-mysql
[postgre]: https://github.com/sameersbn/docker-postgresql
[odoo]: https://registry.hub.docker.com/u/xcgd/odoo/

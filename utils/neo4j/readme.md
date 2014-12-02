#Neo4j

[Neo4j](http://neo4j.com) je grafová databáze s velmi příjemným uživatelským rozhraním.

Pokud ji máme nainstalovanou, tak naslouchá na portu `7474`, popřípadě má velmi hezké webové rozhraní: `http://localhost:7474/browser/`, resp `/webadmin/`


## Grafové databáze

### Ontologie

Je schéma dle kterého je graf sestavován. V `neo4j` je struktura volná.

## Instalace a spuštění

Instalace (Fedora):

```dnf install neo4j```

Obsluhuje se jako jakýkoliv jiný démon:

```service neo4j start```

popřípadě subpříkazy `stop` a `restart`.

## Příkazy

Základní klíčová slova jsou: `MATCH`, `WHERE`, `RETURN`, `CREATE`, `MERGE`, `DELETE`, `SET`, `FOREACH`, `WITH`, `LOAD CSV`, `UNWIND`, `START`, `CREATE UNIQUE`.
Použití vypadá např. takto: ```MATCH <pattern> WHERE <conditions> RETURN <expressions>```


V interaktivní příkazovém řádku můžeme zadat: `:help COMMAND` a dostaneme nápovědu.

Smazání uzlů i vztahů:
```MATCH (n) OPTIONAL MATCH (n)-[r]-() DELETE n,r```

## Links

* [neo4j.cz](neo4j.cz)
* [seriál Zdroják](http://www.zdrojak.cz/clanky/grafova-terminologie-a-dostupne-technologie/)
* [dokumentace](http://docs.spring.io/spring-data/neo4j/docs/current/reference/html/)
* [dokumentace rozcestník](http://neo4j.com/docs/milestone/)
* [blog](http://jexp.de/blog/2013/04/cool-first-neo4j-2-0-milestone-now-with-labels-and-real-indexes/)

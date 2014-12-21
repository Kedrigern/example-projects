Spring rts
==========

Je velmi výkoný engine pro běh her podobných legendární Total Annihilation.

Instalace
---------

Nejjednoduším způsobem jak používat aktuální verzi enginu na Linuxu je stáhnout si [statickou binárku](http://springrts.com/wiki/Download),
kterou umístíme do složky `/opt`.
Následně máme aktuální verzi, neřešíme konflikty a vše funguje. A snadno se aktualizuje.

Pro nainstalování módů je přiložena utilitka `pr-downloader`, která nám pomůže postahovat módy, mapy a AI.

```
./pr-downloader --download-game "Balanced Annihilation v8.06"
```

Nebo lze použít předefinované [tagy](http://springrts.com/wiki/Rapid_Tags):

```
./pr-downloader zk:stable
./pr-downloader ba:stable
```

Popřípadě samozřejmě lze stáhnout mapy:

```
./pr-downloader --download-map "tropical"
```

Další mapy vyhledávejte na sprinfiles, např. MoonQ10x, Spartan_Isle_v02, Vittra_v1, desert_plateaus

Odkazy
------

* [springrts.com](http://springrts.com)

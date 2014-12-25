Spring rts
==========

[Spring rts][homepage] je velmi výkoný engine pro běh her podobných legendární Total Annihilation. Mód, který je nejvěrnější této legendě se jmenuje [Balanced annihilation][ba.org]

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

Soubory jsou ze serveru springfiles.com. Parametr je filename.

Další mapy vyhledávejte na [sprinfiles][files], např. MoonQ10x, Spartan_Isle_v02, Vittra_v1, desert_plateaus


[homepage]: http://springrts.com
[files]: http://springfiles.com
[ba.org]: http://balancedannihilation.org

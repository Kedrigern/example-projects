
Portable
--------



Linux
-----

Steamovská verze Age of Empires II HD a jejich DLC (Forgotten empires, African Kingdorms) chodí docela dobře na Linuxu.

Postup:

1. Nainstalujeme PlayOnLinux
2. Začneme instalovat AoE II HD
3. V rámci toho se nám nainstaluje windows verze Steamu (i když máte verzi linuxovou) a přes ten stáhnete samostnou hru.
4. PlayOnLinux hry jsou využívají wineprefix, čili z terminálu Win Steam spustíme:
  ```
  WINEPREFIX=/home/keddie/.PlayOnLinux/wineprefix/AOE2HD/ wine .PlayOnLinux/wineprefix/AOE2HD/drive_c/Program\ Files/Steam/Steam.exe
  ```
5. Zde hru normálně zapneme.

Problémy:

- úvodní obrazovka trochu zlobí
- multiplayer se déle načítá

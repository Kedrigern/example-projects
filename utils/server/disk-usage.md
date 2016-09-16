# Diskový prostor

Disk usage / využití disku.

Odshora dolu:

## OS

```
df -h
```

-h lidsky čitelné
-l pouze lokální

## Adresářový strom

```
du [file]
```

Vypíše velikost adresářů. Užitečné argumenty:

|    |             |                        |qq
|----|-------------|------------------------|
| -a | --all       | vypisuje i soubory     |
| -c | --total     |                        |
| -s | --summarize | celkem pro každý vstup |
| -d | --max-depth | maximální hloubka, `0` to samé co `--summarize` |
| -h | --human-readable | lidsky čitelné    |
| -t | --threshold | vyjme menší než velikost pokud, pro větší zadej negativní hodnotu               |
|    | --time      | čas poslední modifikace |

## Složka

```
ls -hS
```

Nezapomínat na alias `ll` (`ls -l`).

-l vypiš tabulku s atributy (nejen prostý seznam jmen)
-a vše, včetně skrytých
-h lidsky čitelné
-S seřaď dle velikosti




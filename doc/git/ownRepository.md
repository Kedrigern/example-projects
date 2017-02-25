
Vlastní repozitář
=================

Pokud umíte základy gitu (např. z readme.md), tak pocítíte potřebu tvořit více vlastních repozitářů např. i na vlastním serveru.

Centrální repozitář
-------------------

Následující text popisuje vytvoření 3 repozitářů na 1 počítači. Dva jsou uživatelské (dva vývojáři) a jeden je centrální (server). Jelikož je git flexibilní, tak úplně stejně si to můžete vyrobit na svém serveru (gitu je jedno zda mu zadáte `/src/myProject` či `ssh://user@server.com`.

Budeme mít tedy dva vývojáře Alice a Bob. A jeden server. V našem podání budou jen v rozdílných složkách. Z počátku máme strukturu:

```
|-- alice
|---- projectA
|-- bob
|-- server
```



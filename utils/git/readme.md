Inicializace nového repositáře
==============================

`user@pc:/new_repo $ git init` vytvoří nový repositář ze složky
    `new_repo`.

`git clone <zdroj>`
:   naklonuje existující repositář ze zdroje. Zdroj může být libovolný:
    relativní cesta, absolutní cesta, ftp, ssh, …

Práce s commitem
================

Commit je úprava repositáře. Mělo by se jednat o konkrétní úpravu - např
přidání funkce, opravení chyby. Soubory dělíme na: nesledované a
sledované. Nesledované jsou ignorovány, sledované můžeme automaticky
zařadit do commitu.

`git add`
: přidá soubor do commitu (je třeba provést s každým novým souborem).
Často se používá `git add .`, který přidá vše ve stromě.

`git rm`: odmaže soubor, je dobré takto mazat soubory z projektu. Má klasické parametry `-rf` jako unixový `rm`.

`--cached <file>` s tímto přepínačem odstraníme soubory z gitu, ale nikoliv z disku. Pokud si omylem přidáte soubor skrz `git add`, tak toto je správné řešení, jak ho smazat.

`-q` potlačí výstup (normálně vypíše řádku za každý smazaný soubor).

`git mv`: přesun souboru, je dobré takto přesouvat soubory v projektu.

`commit`: vytvoří commit. Parametry:

`-a`: vloží do commitu vše změněné (čili není potřeba přidávat soubory skrz `git add`).

`-p`: vloží do commitu zadanou cestu.

`-m <zpráva>`: zpráva připojená ke commitu.

Každý commit je jednoznačně určen 40 místným řetězcem, lze z něj
používat jen jednoznačný prefix (typicky prvních _n_ znaků).

GUI
---

Provádět commity v terminálu není vždy pohodlné. Např. když je mnoho
změněných souborů a chcete je rozdělit do několika commitu. Zde není od
věci využít grafickou nádstavbu, např. `git-cola` (v Linuxu) nebo zcela univerzální `git gui` (součást instalace).

Oprava
------

`git reset --hard HEAD`: vrátí vše do stavu posledního commitu.

`git commit --amend`: připojí commit k poslednímu (např. když jsme něco zapomněli). S dodáním parametrů `-C HEAD` nás nebude otravovat editor a použije se message minulého commitu.

Pokud se chceme zbavit netrackovaných souborů (např. tmp), tak v kořeni repozitáře zadáme:
`git clean -f -n` pro seznam a následně odebereme `-n` pro smazání.

Push
====

Push pošle commity do jiné větve. Nejčastější užití je pokud máme
klonovaný repositář, tak uděláme úpravy, připravíme commit a zadáme:
`git push origin master` (origin je větev z které jsme klonovali, master
je naše lokální primární větev). Při správném nastavení stačí
`git push`.

Řešení konfliktů
----------------
Občas se stane, že při PUSH/PULL dojde ke kolizi. Git nás na to upozorní a čeká, co uděláme. Nejjednoduší forma nápavy je příkaz:

`git mergetool -y --tool=meld`

Který konflikt otevře v editoru `meld` a dovolí nám graficky vyřešit konflikt (vzít jednu změnu z jednoho souboru, druhou z druhého etc.).

Porovnání větví
---------------
`git difftool -y --dir-diff <branch>...`


Historie
========
`git log` nám ukaže historii commitů s parametrem `-p` nám zobrazí i rozdíly. Číselný parametr omezí hloubku.

`git show <commit>` ukáže konkrétní commit.

`git branch --contains <commit>` pokud chceme najít z které větve je daný commit.

`git blame <file>` zobrazuje historii konkrétního souboru.

Modifikace
----------
`git rebase --interactive HEAD~2` spojení 2 (obecně *n*) commitů dohromady a podobné věci.


Tagy
====

Tagy jsou víceméně lidsky pojmenované commity, např. alpha, beta,
v1.2.3. Rozlišujeme dva druhy tagů - jednoduchý a úplný (komentovaný).

`tag <name> <commit>`: označí daný commit daným jménem.

`tag -a <name> -m <message>`: vytvoří tag s komentářem, čili třeba tag beta, popis: stále ještě je
    nefunkční síť.

Pro nahrání tagů na server je třeba použít příkaz `git push --tags` (defaultně se tagy nepřenášejí).

Gitignore
=========

Soubor umístěný v kořenu repozitáře, kterým definujeme, které soubory se
mají ignorovat. Typicky binární soubory, dočasné a tak.

Pro definici se používají wildcardy jako `*.o` a také máme přítomen operátor negace `!important.o`.

Odložení rozdělané práce
========================

Pokud implementujeme složitou funkci a najdeme drobnou chybu, tak chceme
nepřijít o rozdělanou práci, ale zároveň vytvořit nový commit, který jen
opraví drobnou chybu.

`git stash save <message>`: uloží rozdělanou práci (naše super nové funkce).

`git stash pop`: vrátí rozdělanou práci (po té, co jsme si v klidu udělali opravný commit, který s tím vůbec nesouvisel).

Logicky se jedná o zásobník, čili tento postup můžeme opakovat.

Větve
=====

`git branch`: výpis větví (existuje i stav, kdy nejsme přítomni v žádné větvi)

`git branch --contains <commit>`: zjištění do které větve commit patří.

`git checkout <branch> <path>`: skočí na větev, smaže necommitované změny. S parametrem `-b` bude při neexistenci nová větev vytvořena. Pokud je specifikována cesta, tak se změny projeví jen na daném souboru (cherry-pick).

`git fetch <origin repo> <origin branch>:<local branch>` z repozitáře origin vytáhne větev origin a u nás vytvoří novou větev.

Smazaní posledního commitu (lokálně, nastavení větve na předposlední commit): `git reset --hard HEAD^`

Spojování větví
---------------
`git merge <branch>` spojí aktuální větev s větví v parametru. Pokud nastane konflikt dostaneme se do speciální "větvě", kde jsou v konfliktních souborech úpravy z obou verzí. Tyto konflikty můžeme vyřešit v normálním textovém editoru či specializovaném (např. meld). Poté změny (náš merge) commitneme.

Při složitějším slučování je důležitý parametr `--no-commit`, který nesloučí "nekonfliktní" soubory automaticky.

Přidání větve do vzdáleného repositáře
--------------------------------------
Začali jsme pracovat na úpravách projektu ve vlastní větvi - my_work_branch, teď jí chceme poslat na server.
`git push -u origin my_work_branch`

Smazání větve ve vzdáleném rpeositáři
-------------------------------------

```
git push origin :<branch_to_del>
```

Rebase
------

Se také používá k spojení větví, ale nespojuje je jako aktuální větvě (jejich HEAD commit), ale spojuje je chronologicky po commitech. Což může být v mnoha případech přehlednější (vidíme jak se věci měnily). Proces vypadá takto:
 1. `git rebase <branch_to_rebas>` zahájíme rebase
 2. Opravíme konflikty (jsou normálně v diff formátu)
 3. Konfliktní soubory přidáme do stage (`git add <file>`)
 4. `git rebase --continue` pokračujeme k dalšímu konfliktu.
 5. Nakonec máme v aktuální větvi několik nových commitů

Cherry pick
-----------

```
git cherry-pick <commit>
```

Pokud je commit HEAD nějaké větve, tak lze použít název větve.

Ukázka
------
 1. Mějme repozitář a v něm jednu větev `master`.
 2. Vytvoříme si pracovní větev: `git checkout -b dev`.
 3. Provádíme běžné změny, commitujeme, tagujeme etc.
 4. Nyní se vrátíme do původní větve `git checkout master`.
 5. Spojíme větve `git merge dev`, pokud jsme v master neprovedli změny, tak vše proběhne ok.


Submoduly
=========

```
git submodule add <git_repo_url> <path/in/repo>
```

Git repo url může být url či lokální cesta.

Path in repo je vlastně cesta a jméno jak bude submodule zobrazen.

Github
======

Github je jedna z nejlepších služeb poskytujících `git`. Jsou zde
veřejné i soukromé repozitáře, systém issues (track, úkoly), wiki pro
projekt, webové stránky projektu a vše je navíc řešeno přes git (stránky
jsou jen další větev).

Deploy
------
Tradičním problém je, že máte zdrojáky na Githubu a lokálně a chcete je deployovat. Tento problém řeším následujícím jednoduchým způsobem.

 1. Vytvořím větev `production` (to je dobré tak jako tak): ```git checkout -b production```, tu přidám na Github: ```git push -u origin production```
 2. V production tedy udržuji kód pro produkci. Kritické je mít dobře nastavené `.gitignore`, aby nemohlo dojít ke smazání konkrétních neverzovaných dat - např. obrázků, specifických modifikací kódu apod.
 3. Na hostingu naklonuji větev `production` přímo z Githubu: ```git clone -b production --single-branch https://github.com/<user>/<repo>.git```
 4. Nyní normálně vyvíjím na localhostu, kód posílám na Github a pokud chci deployovat, tak se jen přihlásím na server a zadám: ```git pull```

Pokročilé
=========
* [Velká sada tipů](https://ochronus.com/git-tips-from-the-trenches), která navíc provede mnoha složitějšími funkcionalitami gitu.

Odkazy
======
* [Pět důvodů proč zvolit git](http://www.zdrojak.cz/serialy/pet-duvodu-proc-zvolit-git)
* [Homepage](http://git-scm.com) s rozsahlou dokumentací
* [Deploy](http://markdotto.com/2011/11/02/how-to-deploy-sites-via-github)
* [Interaktivní návod](http://www.ndpsoftware.com/git-cheatsheet.html)

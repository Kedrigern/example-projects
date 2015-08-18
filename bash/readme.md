
Bash scripts
============

* [md2pdf](md2pdf.sh): Convertor for nautilus scripts
* [adoc2md](adoc2md.sh):
* [findPdf](findPdf.sh):  Search pattern in all pdf files in actual directory. Use pdftotext for convert - it`s main limit of this script. 
* [html2epub](html2epub.sh): html2epub via pandoc with GUI (Zenity). Some mechanism for cleaning html code.


Základní tipy jak psát v bashy
------------------------------

Na začátku skriptu píšeme: `#!/usr/bin/env bash`, což označuje interpret.
Bash nevoláme přímo, protože se v různých distribucích nachází na různých místech
(např. v Ubuntu nesprávně v: `/bin/bash`, zatímco ve Fedoře: `/usr/bin/bash`).

Dále je dobré uvést základní dokumentační komentáře:

```
Author: Joe Doe, mail@example.org
Licence: GPL
Dependency: gcc
Description: Short description
Todo: All funcionality
```

### Funkce

I v bashy existují funkce. Jsou velmi omezené, dokonce ani neumějí vrátit hodnotu.
Nicméně samozřejmě pomohou:

- logickému dělení delšího kódu
- dokumentaci
- testování

Syntaxe:

```bash
function putTextIntoFiles() {
	text="$1"
	shift 1;
	for f in $@; do
		echo "$text" >> f
	done;
}
```

Funkce má proměnné `$1, ...`, což jsou její argumenty. A samozřejmě též může přistupovat ke globálním proměnným.

### Pajpy

Pipe je propojení výstupu jednoho programu se vstupem dalšího, např:
`echo "Lorem ipsum" | grep "Lorem" | wc -c`

Pokud bychom chtěli návratové hodnoty jednotlivých programů, tak je k tomu určena proměnná `PIPESTATUS`.
Pipes však vyvolávají subshelly, čili je dostupná pouze přímo v subshellu, kde jsou pipes:

`echo "Lorem ipsum" | grep "Lorem" | wc -c; echo ${PIPESTATUS[2]}`

Jedná se o bash array.

### Vstupy a výstupy

Bash má standardní vstup (`stdin`), standardní výstup (`stdout`) a standardní chybový výstup (`stderr`).
Výstupy a vstupy jsou operace nad soubory (jako vše v unixu). Proto můžeme vstupy jednoduše přesměrovávat:

```bash
echo "Normal info"			# vypíše na stdin - obvykle na příslušný terminál
echo "Normal info" > text.txt		# vypíše na stdin, což je soubor text.txt
echo "Normal info" >> text.txt		# vypíše na stdin, což je soubor text.txt, text připojí - nepřepíše
echo "Normal info" >> text.txt 2>&1	# vypíše na stdin, což je soubor text.txt, text připojí - nepřepíše, připojili jsme i chybový výstu
>&2 echo "error"			# echo píše na stderr
grep lorem < file.txt 2> /dev/null	# grep má stdin file.txt a chyby vypisuje do /dev/null
grep lorem < file.txt &> both.txt	# oba 2 výstupy do jednoho souboru
```

Ještě se hodí umět zapsat víceřádkový vstup:

```bash
cat > file.txt << EOF
Více řádkový soubor.
Přehledně zapsaný ve skriptu.
EOF
```








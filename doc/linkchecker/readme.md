#Linkchecker

[Link checker](http://wummel.github.io/linkchecker/) je program, kterému zadáte adresu 
a on zkontroluje platnost odkazů. 
Ve skutečnosti toho umí mnohem více - od kontrolování syntaxe po hledání virů v odkazech.

*Upozornění:* kontrola vzdálených odkazů je samozřejmě poněkud obtížnější, 
čili doba kontroly může být relativně dlouhá.

##Testovací stránka
Připravil jsem drobnou html5 stránku na které si lze vše jednoduše vyzkoušet.
Obsahuje 7 linků, 1 rozbitý (`seznam.cy`) a na podstránce `local 3` rozbitou syntax html.

##Use cases
### Výpis do csv
`linkchecker -o csv index.html | sed '/^#/d' > out.csv && libreoffice out.csv`

Rozbor:

`-o csv` výstup v csv

`|` pipe spojuje dva procesy v shellu

`sed '/^#/d'` odfiltrování řádků začínajícím hashem

`> <filename>` výstup do `<filename>`

`&&` po úspěšném skončení spusť další příkaz

`libreoffice out.csv` otevře výstup v libreoffice

##Parametrs
(Víceméně překlad výtahu z manuálu, pro více podrobností samozřejmě `man linkchecker`)

`linkchecker [options] [file-or-url]...`

Adresa může být ve tvaru:
 * http://www.example.net/
 * mysite.example.org
 * ../bla.html
 * c:\temp\test.html
 * www.example.com

`--stdin` čte url ze stadartního vstupu. Url se oddělují mezerou.

`--check-css` zkontroluje syntax css, potřebuje program: `cssutils`

`--check-html` zkontroluje syntax html, potřebuje program: `tidy`

`--scan-virus` skrz `ClamAV` zkusí najít viry

`-o` specifikuj výstupní formát, možnosti:
 * text (default), barevný textový výstup
 * html stránka (i s vloženým css)
 * sql skript pro přímé vložení do DB 
 * csv po řadcích v csv
 * gml GML sitemap graph
 * dot DOT sitemap graph
 * xml strojově čitelné XML
 * gxml GraphXML
 * sitemap XML sitemap, [protocol](http://www.sitemaps.org/protocol.html)

`-a` testuje i linky uvnitř stránky (`<a href="#tips">tips>` to `<a id="tips>tips</a>`), lze otestovat na testovací stránce.

`--ignore-url=REGEX` URL vyhovující REGEX budou ignorovány, tento parametr lze zadat vícekrát.

`--no-follow-url=REGEX` vyzkouší, ale nezanořuje se.

`-u` / `-p` username / password pro HTTP nebo FTP autentizaci.

`--timeout=NUMBER` timeout pro spojení ve vteřinách, default je 60.

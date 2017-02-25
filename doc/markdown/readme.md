# Markdown

Markdown je způsob jak prostým textem zapsat html. Díky tomu, že se jedná o prostý text vám postačí libovolný textový editor. Stejně tak výsledné soubory lze snadno zpracovávat, jelikož se jedná o téměř čistý text. Hlavní pravidla jsou:

```markdown
# Nadpis

Prvni odstavec textu.

Druhý odstavec textu.

Seznam ovoce:

- jablko
- pomeranč
- banán
```

Tento text byl napsán v markdownu. Kromě `#` před nadpisem je to vlastně úplně běžný text. Nicméně konvertory ho dokáží převést do kvalitního html.

Primárně se markdown využivá na internetu, kde je nejjednoduším způsobem (pro uživatele, programátory i adminy) jak ukládat příspěvky. Ty se pak lehko konvertují do kvalitního a bezpečného html. 

Nicméně možnosti využití jsou mnohem širší. Např. dnes je již nepsaným standardem psát readme soubory v markdownu. Ale nejedná se o nástroj jen pro programátory. Např. internetové vydavatelství [leanpub][] nechává autory psát knihy v markdownu a následně je snadno konvertuje.

## Dialekty

Původní markdown od [Johna Grubera][md] dnes není jediný. 
Naštěstí všechny další dialekty jsou spíš jen rozšířením původního, 
čili si uživatel ani nevšimne, že je používá. Nejzajímavější jsou:

* multimarkdown: Rozšiřuje původní markdown o mnoho funcionalit. Jako poznámky pod čarou, citace, tabulky etc. Jeho syntax je základem i pro většinu dalších. Pro podrobné seznámení se syntaxí doporučují rozsáhlou [uživatelskou příručku][mmdPdf] (pdf).
* github markdown: Markdown použivaný na [Github][]u. Krom funcionalit z mmd jde především o odkazování na commity a různé další vychytávky hodící se programátorům.
* pandoc markdown: [Pandoc][] je univerzální konvertor pracující s mnoha formáty. Interně používá markdown jako jazyk mezi všemi převody. Pro tyto účely potřeboval o něco obsáhlejší.

## Syntax

Všechny důležité prvky syntaxe jsou v [MultiMarkdown Guide][mdref].

## Konvertory

### Pandoc

Velmi univerzální konvertor opravdu mnoha různých formátů. 
Pro většinu formátů poskytuje šablony, které lze lehko [modifikovat][pandocTemplate].
Což umožňuje pracovat s textem opravdu dle vlastních představ.

Napsán je v Haskellu, instalovat aktuální verzi lze přes cabal.

```bash
yum install haskell-platform
cabal update
cabal install pandoc
```

### MultiMarkdown

Instalace:

```bash
git clone git@github.com:fletcher/MultiMarkdown-4.git
cd MultiMarkdown-4
git submodule init
git submodule update
make
sudo make install
```

#### Citace

Citace zdrojů se dělají obdobně jako poznámka pod čarou. Namísto `^` se však použije `#` a předpokládá se opakované užití.

```markdown
Lorem[str. 12][#Doe:2006] ipsum dolor sit amet[str. 15][#Doe:2007], consectetur adipiscing elit[].

[#Doe:2006]: John Doe. *Some Big Fancy Book*.  Vanity Press, 2006.
[#Doe:2007]: John Doe. *Some Big Fancy Book 2*.  Vanity Press, 2007.
```

[md]: http://daringfireball.net/projects/markdown
[mmd]: http://fletcherpenney.net/multimarkdown
[mmdPdf]: http://fletcher.github.io/MultiMarkdown-4/MMD_Users_Guide.pdf
[mdref]: https://rawgit.com/fletcher/human-markdown-reference/master/index.html
[github]: https://www.github.com
[pandoc]: http://johnmacfarlane.net/pandoc
[pandocTemplate]: http://los-pajaros-de-hogano.blogspot.cz/2015/01/pandoc-customized-latex-templates-for.html
[leanpub]: https://leanpub.com/

OCR
===

## Převod pdf na obrázky


### PDFcairo

```
pdftocairo [-png|-jpeg|-svg] ing.pdf out
```

Vygeneruje obrázky v příslušném formátu.

### ImageMagick

Pro cmd utility je dobré nejdříve převést pdf na jednotlivé obrázky:

```
convert -density 288 in.pdf -background white -flatten +matte -depth 8 out.tiff
```

popř. lze samozřejmě i `out.jpg`.
  
Problém je s pdfky s alfa kanálem.



## Tesseract

```
tesseract imagename [output] [-l lang] [-psm N]
```

`l` má hodnoty: `ces`, `eng`, `deu`
  
| psm | zpracování sazby                 |
|-----|----------------------------------|
| 1   | auto s OSD                       |
| 3   | plně automatické bez OSD         | 
| 4   | jeden sloupec                    |
| 5   | blok textu zarovnaný vertikálně  |
| 6   | blok textu                       |
| 7   | jednořádkový tex                 |
| 8   | jedno slovo                      |
| 9   | jedno slovo v kruhu              |
| 10  | jedno písmeno                    |

 
Vícerosouborů:
```
for i in *.tif ; do tesseract $i outtext; done;
```

gui: `gImageReader`


## Cuneiform

gui: YAGF


## Automatizace

```bash
#!/bin/bash
# Author: Ondřej Profant
# OCR PDF

if [ $# -ne 1 ]; then
  echo "Usage:";
  echo -e "\t$0 input.pdf"
  exit 1;
fi;

input="$1";
pid=$$;
basename="out-$pid";
output="${input%%.*}.txt"

pdftocairo -jpeg "$1" basename
for i in basename*.jpg ; do
  tesseract $i tmp-outtext;
  cat tmp-outtext* >> "$output";
  rm "$i" "tmp-outtext"*;
done;
```

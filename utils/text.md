
Text proccesing
===============

Pdf
---

Visual diff between 2 pdf files:
```
diffpdf file1.pdf file2.pdf
```

Merge:
```
pdftk soubor1.pdf soubor2.pdf cat output vystup.pdf
```

Split:
```
pdftk soubor.pdf cat 1-9 26-end output vystup.pdf
```

Split to the pages:
```
pdftk soubor.pdf burst
```

### Check 
List of images:
```
pdfimages -list file.pdf
```
For information about one image use `identify` and see [stackoverflow](http://stackoverflow.com/questions/12661093/preflight-program-for-pdfs-using-podofo-or-anything-else-open-source)
List of fonts:
```
pdffonts vamp.pdf
```

### Convert to color space
To cmyk:
```
gs -dSAFER -dBATCH -dNOPAUSE -dNOCACHE -sDEVICE=pdfwrite \
-sColorConversionStrategy=CMYK -dProcessColorModel=/DeviceCMYK \
-sOutputFile=output.pdf input.pdf
```

To grayscale:
```
gs \
 -sOutputFile=output.pdf \
 -sDEVICE=pdfwrite \
 -sColorConversionStrategy=Gray \
 -dProcessColorModel=/DeviceGray \
 -dCompatibilityLevel=1.4 \
 -dNOPAUSE \
 -dBATCH \
 input.pdf
```

LibreOffice
-----------
XML representation of odf:
```
odt2txt --raw example.odt | xmllint --format -
```
Convert odf to markdown:
```
unoconv -f mediawiki --stdout example.odt | pandoc -f mediawiki -t markdown --smart --normalize --preserve-tabs 
```

### git diff for odt
Global config `~/.gitconfig`:
```
[diff "odf"]
	textconv=odt2txt
```
Repository config via [gitatributes](http://git-scm.com/docs/gitattributes) (`.gitattributes`)
```
*.ods diff=odf
*.odt diff=odf
*.odp diff=odf
```

[Source](http://www-verimag.imag.fr/~moy/opendocument/)

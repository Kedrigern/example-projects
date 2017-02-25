
all: toTex

toTex: template/head1.tex template/head2.tex template/foot.tex
	multimarkdown -t latex *.md > book.tex
	vlna book.tex 

toEpub:
	:

clean:
	rm -rf *.aux *.log *.idx *.out *.tex *.pdf
	rm -rf book.te~


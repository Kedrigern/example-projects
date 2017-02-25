all: toTex

toTex: template/head1.tex template/head2.tex template/foot.tex
	multimarkdown \
		-t latex -o letter.tex \
		--smart \
		--full \
		letter.md
	xelatex letter.tex

toEpub:
	:

clean:
	rm -rf *.aux *.log *.idx *.out *.tex *.pdf;


                                                      

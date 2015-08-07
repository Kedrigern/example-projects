#!/usr/bin/bash
## Author: Ondřej Profant
## Licence: GPL
## Dependencies: pandoc, zenity, vlna
## Install into:
## - ~/.local/share/nautilus/scripts/ (Fedora, Ubuntu)


bin=pandoc
filefull=${NAUTILUS_SCRIPT_SELECTED_FILE_PATHS[0]}
file=$(basename "$filefull")
output="${file%.*}.pdf";

#file=readme.md
#output=readme.pdf

function convert() {
	if $bin -v > /dev/null; then
	
		errorFile=errors.txt
		
		$bin -f markdown --smart --normalize -s -t latex --latex-engine=xelatex -o - "$1" 2> "$errorFile" | vlna -f -v KkSsVvZzOoUuAaI 2>> "$errorFile" | xelatex -output-directory="/tmp" 2>> "$errorFile"; rets=(${PIPESTATUS[*]})

		if [ ${rets[0]} -ne 0 ]; then
			zenity --text "Pandoc vrátil kód ${rets[0]} pro $file ($output), podrobnosti v $errorFile" --error;
			exit 1		
		fi;
		if [ ${rets[1]} -ne 0 ]; then
			zenity --text "vlna vrátil kód ${rets[1]} pro $file ($output), podrobnosti v $errorFile" --error;
			exit 1
		fi;
		if [ ${rets[2]} -ne 0 ]; then
			zenity --text "xelatex vrátil kód ${rets[2]} pro $file ($output), podrobnosti v $errorFile" --error;
			exit 1
		fi;
		
		rm "$errorFile"
		mv "/tmp/texput.pdf" "./$2"
	
	else
		zenity --text "Pandoc nenalezen" --error;
		exit 1
	fi;
}

convert "$file" "$output"

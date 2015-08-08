#!/usr/bin/bash
## Author: Ondřej Profant
## Licence: GPL
## Dependencies: pandoc, zenity, vlna
## Install into:
## - ~/.local/share/nautilus/scripts/ (Fedora, Ubuntu)

# Global vars
bin=pandoc
output=""
tmpdir="textmpdir"

function input() {
	if [ -z "$NAUTILUS_SCRIPT_SELECTED_FILE_PATHS" ]; then
		echo "Nautilus doesn't not pass any data, use readme instead"
		NAUTILUS_SCRIPT_SELECTED_FILE_PATHS=("readme.md" "readme2.md" "readme3.md")
		cp "readme.md" "readme2.md"
		cp "readme.md" "readme3.md"
	fi;
	file1=${NAUTILUS_SCRIPT_SELECTED_FILE_PATHS[0]}
	file=$(basename "$file1")
	output="${file%.*}.pdf"
}

function convert() {

	if $bin -v > /dev/null; then
		mkdir -p "$tmpdir"	
		errorFile=errors.txt
		
		$bin -f markdown -t latex --latex-engine=xelatex \
			--smart --normalize -s \
			-o - ${NAUTILUS_SCRIPT_SELECTED_FILE_PATHS[@]} \
			2> "$errorFile" | \
		vlna -f -v KkSsVvZzOoUuAaI 2>> "$errorFile" | \
		xelatex -output-directory="$tmpdir" >> "$errorFile" 2>&1; \
		rets=(${PIPESTATUS[*]})

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
		
		mv "$tmpdir/texput.pdf" "$output"
		rm "$errorFile"
		rm -rf "$tmpdir"
	
	else
		zenity --text "Pandoc nenalezen" --error;
		exit 1
	fi;
}

input
convert


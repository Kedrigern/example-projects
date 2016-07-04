#!/usr/bin/env python3
"""
Fix epubs generate by Google docs.
In this epubs are inline styles.
This script removes this inline styles.
"""

__version__ = "v0.1.1"
__author__ = "Ondřej Profant"

import os
import re
import zipfile
import argparse
import tkinter as tk
from tkinter import filedialog, messagebox

def copyNameWith(name):
	return re.sub(r'([\w-]*).epub', r'\1-clean.epub', name)

def preview(zf):
	""" Preview of epub printed into terminal """
	texts = [f for f in zf.namelist() if f.startswith('OEBPS/Text/') and f.endswith('.xhtml')]
	styles = [f for f in zf.namelist() if f.startswith('OEBPS/Styles/') and f.endswith('.css')]
	print('Texts files in epub:', texts)
	print('Styles files in epub:', styles)
	with zf.open(texts[0], 'r') as fo:
		chars = 5000
		print('First %d chars:' % chars, fo.read(chars).decode('UTF-8'))

def copyZipExcept(zin, zout, exceptList):
	""" Copy zipfile into another zipfile """
	zout.comment = zin.comment # preserve the comment
	for item in zin.infolist():
		if not item.filename in exceptList:
			zout.writestr(item, zin.read(item.filename))

def fix(zin, newname):
	""" Substitute inline style """
	remove1 = r'( class="[a-zA-Z0-9 ]*"| style="[a-zA-Z0-9:; -]*")'
	remove2 = r'(<span>|</span>)'
	texts = [f for f in zin.namelist() if f.startswith('OEBPS/Text/') and f.endswith('.xhtml')]
	# copy archive without text files
	with zipfile.ZipFile(newname, 'w') as zout:
		copyZipExcept(zin, zout, texts)
		# modify text files
		for f in texts:
			with zin.open(f, 'r') as fo:
				t1 = fo.read().decode('UTF-8')
				t2 = re.sub(remove1, r'', t1)
				t3 = re.sub(remove2, r'', t2)
				zout.writestr(f, t3)

def main():
	parser = argparse.ArgumentParser(description=__doc__, epilog='Author: ' + __author__ + ', version: ' + __version__)
	sub = parser.add_subparsers(dest='subparser_name')
	parser_g = sub.add_parser('gui', help='Run with simple GUI.')
	parser_g.add_argument('-o', '--out', default=None, help='Filename of fixed file.')
	parser_v = sub.add_parser('view', help='Only preview of epub for quick visual analytics.')
	parser_v.add_argument('infile', help='Input file (epub with inline styles)')
	parser_f = sub.add_parser('fix', help='Replace in-line styles.')
	parser_f.add_argument('-o', '--out', help='Filename of fixed file.')
	parser_f.add_argument('infile', help='Input file (epub with inline styles)')
	args = parser.parse_args()

	if args.subparser_name == 'gui':
		root = tk.Tk()
		root.withdraw()
		infile = filedialog.askopenfilename(
				filetypes=[('Epub', "*.epub")],
				initialdir=os.path.expanduser('~') )
	else:
		infile = args.infile

	if not zipfile.is_zipfile(infile):
		print('Error: %s is not a zip / epub')
		if args.subparser_name == 'gui':
			messagebox.showwarning('Chyba', 'Soubor nemá správný formát: %s ' % infile)
		return

	with zipfile.ZipFile(infile) as zin:
		if args.subparser_name == 'view':
			preview(zin)
		elif args.subparser_name in ['fix', 'gui']:
			if not args.out:
				outfile = copyNameWith(infile)
			fix(zin, outfile)

if __name__ == '__main__':
	main()

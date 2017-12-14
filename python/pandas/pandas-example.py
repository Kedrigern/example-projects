#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Jednoduchá ukázka práce s knihovnou Pandas.
Ta slouží k úpravám tabulkových dat.
"""

import pandas as pd

datafile1 = "datafile.csv"
use_cols = ['a', 'b', 'c']  # use only these 3 cols, col d will be removed
to_del = ['d']              # remove column d

def load_csv():
    # Use only some cols
    t1 = pd.read_csv(datafile1, sep=',', usecols=use_cols)

    # Drop some cols
    t2 = pd.read_csv(datafile1, sep=",")
    t2.drop(to_del, axis=1, inplace=True)

    print("1. Můžeme načíst csv a rovnou v něm profiltrovat řádky či sloupce.")
    print(t1.head(1))
    print(t2.head(1))

def view():
    t1 = pd.read_csv(datafile1)

    print("2. Můžeme snadno vyfiltrovat řádky:")

    print('t1[t1.index != 2]')
    print( t1[t1.index != 2] )
    
    print('t1.drop(t1.index[[2,3]])')
    print( t1.drop(t1.index[[2,3]]) )

def main():

    print(__doc__)

    load_csv()
    view()

if __name__ == '__main__':
    main()

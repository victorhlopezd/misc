#! /usr/bin/env python

import sys

#Counting DNA Nucleotides

#Given: A DNA string s of length at most 1000 nt. 
#Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

s = sys.argv[1]

a = s.count('A')
c = s.count('C')
g = s.count('G')
t = s.count('T')

print(f'{a} {c} {g} {t}')

#! /usr/bin/env python

import sys

#Transcribing DNA into RNA

#Given: A DNA string t having length at most 1000 nt. 
#Return: The transcribed RNA string of t.

t = sys.argv[1]

rna = t.replace('T', 'U')

print(rna)	

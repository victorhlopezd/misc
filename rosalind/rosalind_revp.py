#! /usr/bin/env python

import sys

#Locating Restriction Sites

#Given: A DNA string of length at most 1 kbp in FASTA format.
#Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.

file = sys.argv[1]

seq = ''

with open(file, 'r') as file:
	for line in file:
		line = line.rstrip()
		if not line.startswith('>'):
			seq += line

comp_dict = {'A' : 'T', 'T' : 'A', 'C' : 'G', 'G' : 'C'}


pal_pos = []
pal_len = []

pos = 0

for nuc in seq:
	pal_range = [x for x in range(4,13)]
	
	for c in pal_range:
		endpos = pos + c
	
		if endpos <= len(seq) and c <= 12:
			subseq = seq[pos:endpos]
			rev_subseq = subseq[::-1]
			rev_comp = ''
		
			for nucleotide in rev_subseq:
				nucleotide = comp_dict[nucleotide]
				rev_comp += nucleotide
		
			if subseq == rev_comp:
				pal_pos.append(pos + 1)
				pal_len.append(len(rev_comp))
	
	pos += 1	

for a,b in zip(pal_pos, pal_len):
	print(str(a) + ' ' + str(b))

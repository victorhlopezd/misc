#! /usr/bin/env python

import sys

#Finding a Most Likely Common Ancestor

#Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format. 
#Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

file = sys.argv[1]

seq_list = []
seq = ''

c = 0

with open(file, 'r') as file:

	for line in file:
		line = line.rstrip()
		
		if line.startswith('>'):
			c += 1
			
			if c > 1:
				seq_list.append(seq)
			
			seq = ''
		
		else: 
			seq += line
	
	seq_list.append(seq)


for seq in seq_list:
	n = len(seq)
	

profile_matrix = {'A': [0]*n, 'C': [0]*n, 'G': [0]*n, 'T': [0]*n}


for seq in seq_list:
	for pos, nuc in enumerate(seq):
		profile_matrix[nuc][pos] += 1

maxes = []

for pos in range(n):
	max_c = 0
	max_nuc = None
	
	for nuc in ['A', 'C', 'G', 'T']:
		c = profile_matrix[nuc][pos]
		
		if c > max_c:
			max_c = c
			max_nuc = nuc
		
	maxes.append(max_nuc)
				
cons_seq = ''.join(maxes)

print(cons_seq)


for nuc, occur in profile_matrix.items():
	occur = [str(x) for x in occur]
	occur = " ".join(occur)
	print(nuc + ": " + occur)

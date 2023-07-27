#! /usr/bin/env python

import sys

#Computing GC content

#Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each). 
#Return: The ID of the string having the highest GC-content, followed by the GC-content of that string.

infile = sys.argv[1]

id_list = []
seq_list = []
seq = ''

c = 0

with open(infile, 'r') as infile:

	for line in infile:
		line = line.rstrip()
		
		if line.startswith('>'):
			line = line.replace('>','')
			id_list.append(line)
			
			c += 1
			
			if c > 1:
				seq_list.append(seq)
			
			seq = ''
		
		else: 
			seq += line


gc_content = []

for seq in seq_list:
	gc = (seq.count('C') + seq.count('G'))/len(seq)*100
	gc_content.append(gc)
	
	
output_dict = dict(zip(id_list, gc_content))

highest_gc = max(gc_content)

for seqid, seq in output_dict.items():
	if seq == highest_gc:
		print(seqid + '\n' + f'{seq}')

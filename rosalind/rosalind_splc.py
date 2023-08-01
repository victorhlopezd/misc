#! /usr/bin/env python

import sys

#RNA Splicing

#Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format. 
#Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)

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


exons = seq_list[0]

introns = seq_list[1:]

for intron in introns:
	exons = exons.replace(intron, '')


codons_exons = [exons[i:i+3] for i in range(0, len(exons), 3)]
	
codon_dict = {'S': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'], 'L': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'], 'C': ['TGT', 'TGC'], 'W': ['TGG'], 'E': ['GAA', 'GAG'], 'D': ['GAT', 'GAC'], 'P': ['CCT', 'CCC', 'CCA', 'CCG'], 'V': ['GTT', 'GTC', 'GTA', 'GTG'], 'N': ['AAT', 'AAC'], 'M': ['ATG'], 'K': ['AAA', 'AAG'], 'Y': ['TAT', 'TAC'], 'I': ['ATT', 'ATC', 'ATA'], 'Q': ['CAA', 'CAG'], 'F': ['TTT', 'TTC'], 'R': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'], 'T': ['ACT', 'ACC', 'ACA', 'ACG'], '': ['TAA', 'TAG', 'TGA'], 'A': ['GCT', 'GCC', 'GCA', 'GCG'], 'G': ['GGT', 'GGC', 'GGA', 'GGG'], 'H': ['CAT', 'CAC']}

amino_list = []

for codon in codons_exons:
	for amino, codon_list in codon_dict.items():
		if codon in codon_list:
			amino_list.append(amino)

protein = ''.join(amino_list)

print(protein)

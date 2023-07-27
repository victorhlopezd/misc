#! /usr/bin/env python

import sys

#Translating RNA into Protein

#Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp). 
#Return: The protein string encoded by s.


codon_dict = {'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'], 'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'], 'C': ['UGU', 'UGC'], 'W': ['UGG'], 'E': ['GAA', 'GAG'], 'D': ['GAU', 'GAC'], 'P': ['CCU', 'CCC', 'CCA', 'CCG'], 'V': ['GUU', 'GUC', 'GUA', 'GUG'], 'N': ['AAU', 'AAC'], 'M': ['AUG'], 'K': ['AAA', 'AAG'], 'Y': ['UAU', 'UAC'], 'I': ['AUU', 'AUC', 'AUA'], 'Q': ['CAA', 'CAG'], 'F': ['UUU', 'UUC'], 'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'], 'T': ['ACU', 'ACC', 'ACA', 'ACG'], '': ['UAA', 'UAG', 'UGA'], 'A': ['GCU', 'GCC', 'GCA', 'GCG'], 'G': ['GGU', 'GGC', 'GGA', 'GGG'], 'H': ['CAU', 'CAC']}

file = sys.argv[1]

s = ''

with open(file, 'r') as file:
	for line in file:
		line = line.rstrip()
		s += line
		
codons_rna = [s[i:i+3] for i in range(0, len(s), 3)]

amino_list = []

for codon in codons_rna:
	for amino, codon_list in codon_dict.items():
		if codon in codon_list:
			amino_list.append(amino)
			
protein = ''.join(amino_list)

print(protein)

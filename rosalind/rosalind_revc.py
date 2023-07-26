#! /usr/bin/env python

import sys

#Complementing a Strand of DNA

#Given: A DNA string s of length at most 1000 bp. 
#Return: The reverse complement sc of s.

s = sys.argv[1]

complementary_nucleotides = {"A" : "T", "C" : "G", "T" : "A", "G" : "C"}

reverse_dna = s[::-1]


reverse_complementary = ""

for nucleotide in reverse_dna:
	nucleotide = complementary_nucleotides[nucleotide]
	reverse_complementary += nucleotide
			

print(reverse_complementary)

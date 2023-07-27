#! /usr/bin/env python

import sys

#Counting Point Mutations

#Given: Two DNA strings s and t of equal length (not exceeding 1 kbp). 
#Return: The Hamming distance dH(s,t).

infile = sys.argv[1]

with open(infile, 'r') as infile:
	
	c = 0
	
	for line in infile:
		c += 1
		if c > 1:
			t = line
		else:
			s = line

hamming_distance = 0

for nuc1, nuc2 in zip(s,t):
	if nuc1 != nuc2:
		hamming_distance += 1

print(hamming_distance)

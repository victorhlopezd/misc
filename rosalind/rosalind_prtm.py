#! /usr/bin/env python

import sys

#Chaining the Amino Acids

#Given: A protein string P of length at most 1000 aa.
#Return: The total weight of P. Consult the monoisotropic mass table.

file = sys.argv[1]


amino_mass_dict = {'A' : 71.03711, 'C' : 103.00919, 'D' : 115.02694, 'E' : 129.04259, 'F' : 147.06841, 'G' : 57.02146, 'H' : 137.05891, 'I' : 113.08406, 'K' : 128.09496, 'L' : 113.08406, 'M' : 131.04049, 'N' : 114.04293, 'P' : 97.05276, 'Q' : 128.05858, 'R' : 156.10111, 'S' : 87.03203, 'T' : 101.04768, 'V' : 99.06841, 'W' : 186.07931, 'Y' : 163.06333}


prot = ''

with open(file, 'r') as file:
	for line in file:
		line = line.rstrip()
		prot += line


amino_list = list(prot)

amino_mass_list = []

for amino in amino_list:
	amino = amino_mass_dict[amino]
	amino_mass_list.append(amino)
	
total_mass = round(sum(amino_mass_list), 3)

print(total_mass)

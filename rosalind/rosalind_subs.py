#! /usr/bin/env python

import sys 

#Finding a Motif in DNA

#Given: Two DNA strings s and t (each of length at most 1 kbp). 
#Return: All locations of t as a substring of s.

file = sys.argv[1]

with open(file, 'r') as file:
	c = 0
	for line in file:
		c += 1
		if c > 1:
			t = line
		else:
			s = line
			
s = s.rstrip()
t = t.rstrip()

location_list = []

for i in range(len(s)):
	if s[i] == t[0]:
		if s[i:i+len(t)] == t:
			location_list.append(i+1)
			
			
locations = ' '.join(str(loc) for loc in location_list)

print(locations)

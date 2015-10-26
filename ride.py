#! /usr/bin/python

import sys

with open(sys.argv[1]) as f_in:
	out = open(sys.argv[2],'w')
	i = 0	
	for line in f_in:
		for word in line.split():
			if i ==3:
				out.write(word+' ')
			if i!=2:	
				out.write(word+' ')
			i+=1		
		i = 0
		out.write('\n')

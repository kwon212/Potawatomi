#! /usr/bin/python

# make a carmel file that creates a list of all characters of train and dev files
# and creates a fsa with paths to and from all characters
# anc creates a fst that removes accents 
#./make_fsm.py <train file> <dev file> <fsa file> <fst file>

import string
import sys
import unicodedata

file_list=[]
file_list.append("_")

# function that creates list
def create_list(filename):
	with open(filename) as f_input:
		for l1 in f_input:
			l1=l1.rstrip('\n') 
			l1=unicode(l1,"utf-8")
 			for c1 in l1:
				if not c1 in file_list and c1 != '"':
					file_list.append(c1)
	
create_list(sys.argv[1])
create_list(sys.argv[2])

# make fsa 	
with open(sys.argv[3],'w') as file_output:
	
	file_output.write(str(len(file_list))+'\n')  # final state
	for i in range(0,len(file_list)):		
		for j in range(0,len(file_list)+1):
			if j == len(file_list):
				line ='('+str(i)+' ('+str(j)+' '+ ' *e* *e* ))\n'

			else:
				letter = file_list[j]	
				line ='('+str(i)+' ('+str(j)+' '+ ' *e* "' + letter +'" ))\n' 
			line=line.encode('utf-8')
			file_output.write(line)
			
		
# make fst	
with open(sys.argv[4],'w') as file_output:

        file_output.write('0\n')  # final state

        for i in range(0,len(file_list)):
                input = file_list[i]
		input = input.encode("utf-8")
		input = unicode(input, "utf-8")
		out = unicodedata.normalize("NFKD", input)      #decompose
                out = u"".join([c for c in out if not unicodedata.combining(c)])
                out=out.encode("utf-8")
                input = input.encode("utf-8")
                line ='(0 (0 "'+str(input)+'" "'+str(out)+'" 1))\n'
                file_output.write(line)


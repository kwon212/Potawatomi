#! /usr/bin/python

# modify original data so that it outputs two new files
# 1. a file with "" around each char and whitespace as _ on each line
# 2. a file with modified line on each even line; each odd line is blank (*e*)
# ./modify_data.py <input file> <output file w blank lines> <output file w.o blank lines>

import unicodedata
import sys


with open(sys.argv[1]) as file_input:
	with open(sys.argv[2],'w') as file_output:
		with open(sys.argv[3],'w') as file_output_1:
			for line in file_input:
				line = line.rstrip()
				if line != '':
					file_output.write('*e*'+'\n')
					line = line.rstrip()
					line = line.rstrip('\n')
					line = unicode(line, "utf-8")	
					for i in line:	
						i = i.strip() #strips front and end chars
						if i != '\"':
							if i == "":
								i = '_'			
							line = '"'+i+'"'+" "
							line = line.encode("utf-8")
							file_output.write(line)
							file_output_1.write(line)
					file_output.write('\n')
					file_output_1.write('\n')

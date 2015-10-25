#! /usr/bin/python

# Split a file into train/dev/test (80/10/10) with and without accents 

import math
import os
import unicodedata


def remove_accents(line):              
	line = unicode(line,"utf-8")     #convert to unicode
        line = unicodedata.normalize("NFKD", line)	#decompose 
	line = u"".join([c for c in line if not unicodedata.combining(c)])    
	line = line.lower()     #make lowercase
        line = line.encode("utf-8")
	return line

def split_file(file_name):
	
        base , ext = os.path.splitext(file_name)        #split filename

	f_out = open(base+'_train'+ext,'w')		#open train files
	f_out_rm = open(base+'_train_rm'+ext,'w')

	i = 0

	while ( i < lnum ):
		if i == int(math.ceil(lnum*0.8)):       
			# when 80 percent of file is reached, 
			# close train files and write to dev files
                        f_out.close()
                        f_out_rm.close()
                        f_out = open(base+'_dev'+ext,'w')
                        f_out_rm = open(base+'_dev_rm'+ext,'w')
                        print "writing training files\n"

		if i == int(math.ceil(lnum*0.9)):       
			# when 90 percent of file is reached,
			# close deve files and write to test files
                        f_out.close()
                        f_out_rm.close()
                        f_out = open(base+'_text'+ext,'w')
                        f_out_rm = open(base+'_test_rm'+ext,'w')
                        print "writing dev files\n"

                f_out.write(lines[i])
                f_out_rm.write(lines_rm[i])
                i += 1

	print "writing test files\n"
        f_out.close()
        f_out_rm.close()

try:
	lines = []	# list of sentences with accents
	lines_rm = []	# without accents

	with open('french.txt') as file_input:
		for line in file_input:
			lines.append(line) 	
			lines_rm.append(remove_accents(line))	

	lnum = len(lines)	# total number of lines 

	split_file('french.txt')	#split file

except IOError as e:
	print 'Could not open file for reading!' % e



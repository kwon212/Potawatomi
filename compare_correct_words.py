#! /usr/bin/python

# compare differences in list of correct words

import sys

with open(sys.argv[1]) as f1:
	with open(sys.argv[2]) as f2:
		list1 = []
		list2 = []
		correct = []
		for l1 in f1:
			ll1 = []
			ll1=l1.split()
			list1.append(ll1[3])
		for l2 in f2:
			ll2 = []
			ll2=l2.split()
			list2.append(ll2[3])
		for i in list1:
			for j in list2:
				if i == j: # same word exists
					if not i in correct:
						correct.append(i)
					#list1.remove(i)
					#list2.remove(i)	
		#list1 = list(set(correct)^set(list1))
		#list2 = list(set(correct)^set(list2))
	f_out = open(sys.argv[3],'w')
	
	#f_out.write("Words unique to %s\n\n"%sys.argv[1])
	#for l1 in list1:
#		f_out.write(l1)
#	f_out.write("\n\n\nWords unique to %s\n\n" % sys.argv[2])
#	for l2 in list2:
#		f_out.write(l2)
#	f_out.write("\n\nList of same words between two files:\n\n")
        i=0
	for l in correct:
		
                f_out.write("(ZERO ("+str(i)+" "+l+" "+l+" 1))"+'\n')
		i+=1

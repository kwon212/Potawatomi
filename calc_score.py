#! /usr/bin/python
# -*- coding: utf-8 -*-

# calculate score (correct # of vowels/total # of vowels)
#./calc_score.py <original file> <new file>

import unicodedata
import sys

with open(sys.argv[1]) as file1:	#original final before training w/ double quotations
	with open(sys.argv[2]) as file2:	#updated file after wfsa training w/ double quotations
		accent =dict({3:u'ù',4:u'û',5:u'ü',7:u'à',8:u'â',9:u'é',10:u'è',11:u'ê',12:u'ë',13:u'ï',14:u'î',15:u'ô',16:u'a',17:u'e',18:u'i',19:u'o',20:u'u'})
		f_out=open('score_correctwords.txt','w')
		f_out1=open('score_wrongwords.txt','w')
		f_out2=open(sys.argv[3],'w')
		correct = 0
		wrong = 0
		accent_total = 0
		count = 0
		count_cor = 0
		accent_count = 0
		f_out.write("correct  wrong"+'\n')
		for l1, l2 in zip(file1,file2):
			l1=unicode(l1,"utf-8")
                        l2=unicode(l2,"utf-8")
			l2=l2.replace('\"'," ")
                        l1=l1.replace('\"'," ")
			l2=l2.replace(" ","")
                        l1=l1.replace(" ","")
			l2=l2.replace("_"," ")
			l1=l1.replace("_"," ")
			for ch1 in l1:
				for key in accent:
					if ch1 == accent[key]:
						accent_total+=1
			for w1,w2 in zip(l1.split(),l2.split()):
				for c1,c2 in zip(w1,w2):
					for key in accent:
						if accent[key] == c1:
							count +=1
							if c1 == c2:
								if key < 16:
									accent_count = 1
								correct+=1
								count_cor += 1
				if count_cor < count  and count>0: 
					f_out1.write(w1.encode('utf-8')+' '+w2.encode('utf-8')+'\n')
				if count_cor > 0 and count == count_cor and accent_count == 1:
					f_out.write(w1.encode('utf-8')+' '+w2.encode('utf-8')+'\n')
					f_out2.write(w1.encode('utf-8')+'\n')
				count = 0
				accent_count = 0
				count_cor = 0
		print "number of correct vowels:"  + str(correct)	
		print "total number of vowels:" + str(accent_total)		
		score = correct/ float(accent_total)
		print "score:" + str(score)

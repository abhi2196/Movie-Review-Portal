#!/usr/bin/python
import sys
 
current_word = None
current_title = None
current_rating = None
current_count = 1
word=None
 
for line in sys.stdin:
    word=line.split(',')
    word[2]=str(word[2]).replace("\n","")
    if(word[0]==current_word):
    	current_count+=1
	sys.stdout.write("%s#%s$" % (word[1],word[2]))
	sys.stdout.flush()	
    else:
	if current_word: 
                sys.stdout.write("%s#%s" % (word[1],word[2]))
        	print "\n%s,%d" % (current_word,current_count)
		current_count=1
	current_word = word[0]

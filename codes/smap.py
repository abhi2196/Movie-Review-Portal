#!/usr/bin/python
 
import sys
for line in sys.stdin:
    line=line.strip()
    words=line.split('\t')
    title=words[0]
    try:
	    release_date=words[2]
    except IndexError:
	    release_date='null'
    try:
    	    rating=words[3]
    except IndexError:
	    rating=0.0
    print "%s,%s,%s" % (release_date,title,rating)

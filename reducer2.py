#!/usr/bin/env python

import sys, ast
from operator import itemgetter
from collections import Counter


c_w = None
map_c = {}
word = None

for line in sys.stdin:
    line = line.strip()
    
    #print line.split('\t')
    # parse the mapper input
    word, dicto = line.split('\t')
    dicto = ast.literal_eval(dicto)
     # convert count (currently a string) to int
    
    if c_w == word:
        A = Counter(dicto)
	B = Counter(map_c)
	map_c = dict(A+B)
    else:
        if c_w:
	    # write result to STDOUT
	    print '%s\t%s' % (c_w, map_c)
	map_c = dicto
	c_w = word

if c_w == word:
    print '%s\t%s' % (c_w, map_c)


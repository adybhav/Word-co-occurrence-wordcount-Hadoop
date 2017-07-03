#!/usr/bin/env python

import sys, re

window = 2

for line in sys.stdin:
    line = line.strip()
    twits = line.split()
    i = 0
    while i <len(twits):
        j = 0
        while j <len(twits):
            if i!= j:
                print("%s%s\t%d" % (twits[i]+' ', twits[j], 1))
            j+=1
        i+=1
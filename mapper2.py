#!/usr/bin/env python

import sys, re

# size of the context window
window = 2

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove non alpha-numeric
    line = re.sub("[^a-zA-Z-0-9]", " ", line)

    # remove leading and trailing whitespace
    line = line.strip()

    # split the line into keys
    keys = line.split()
    i=0
    j=0
    cp=0
    while i< len(keys)-1:
        keys_p = {}
        while j< len(keys)-1:
            if i==j:
                cp+=1
            else:
                if keys[j] not in keys_p:
                    keys_p[keys[j]] = 1
                else:
                    keys_p[keys[j]] += 1
            j+=1
        i+=1
        print('%s\t%s' % (keys[i], keys_p))

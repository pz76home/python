#!/usr/bin/python

import sys

f = open('/directory/file')
# If you need to use stdin instead
#f = sys.stdin
for line in f:
    fields = line.strip().split()
    # Array indices start at 0 unlike AWK
    print(fields[4])

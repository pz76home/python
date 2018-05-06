#!/usr/bin/python

import sys
sum = 0

f = open('/admin/scripts/test/list.report')
# If you need to use stdin instead
#f = sys.stdin
for line in f:
    fields = line.strip().split()
    # Convert field into an integer and add the total of the 4th field
    sum += int(fields[4])
#To print the total value, first convert to an integer value and have "print" outside of the for loop.  
print sum

#!/usr/bin/python

import sys
from decimal import Decimal
size = 0

#f = open('/admin/scripts/test/list.report')
# If you need to use stdin instead
f = sys.stdin
for line in f:
    # change field separator to ":"
    fields = line.strip().split(':')
    # Convert field 10 to decimal value for maths operation
    output = Decimal(fields[10])
    # Maths operation
    output1 =(output/1024/1024)
    # Round the calculated value into 2 decimal places
    output2 = round(output1,2)
    # Convert rounded decimal value in a string to allow concatenation
    size = str(output2)
    # Use the "+" sign for concantenation and create a csv output
    print  fields[6]+","+fields[7]+","+fields[9]+","+size

#Sample data

#mmrepquota::0:1:::nas:GRP:12046:12046:0:0:0:0:none:5:0:0:0:none:i:on:off:::
#mmrepquota::0:1:::nas:GRP:1000014:1000014:32:0:0:0:none:3:0:0:0:none:i:on:off:::
#mmrepquota::0:1:::nas:GRP:1007:1007:0:0:0:0:none:1:0:0:0:none:i:on:off:::
#mmrepquota::0:1:::nas:GRP:10031:10031:15345344:0:0:0:none:26597:0:0:0:none:i:on:off:::
#mmrepquota::0:1:::nas:GRP:12047:12047:795392:0:0:0:none:62:0:0:0:none:i:on:off:::

#!/usr/bin/python

import sys
from decimal import Decimal
size = 0

#f = open('/admin/scripts/test/list.report')
# If you need to use stdin instead
f = sys.stdin
for line in f:
    fields = line.strip().split(':')
    # Array indices start at 0 unlike AWK
    output = Decimal(fields[10])
    output1 =(output/1024/1024)
    output2 = round(output1,2)
    size = str(output2)
    print  fields[6]+","+fields[7]+","+fields[9]+","+size

#Sample data

#mmrepquota::0:1:::nas:GRP:12046:12046:0:0:0:0:none:5:0:0:0:none:i:on:off:::
#mmrepquota::0:1:::nas:GRP:1000014:1000014:32:0:0:0:none:3:0:0:0:none:i:on:off:::
#mmrepquota::0:1:::nas:GRP:1007:1007:0:0:0:0:none:1:0:0:0:none:i:on:off:::
#mmrepquota::0:1:::nas:GRP:10031:10031:15345344:0:0:0:none:26597:0:0:0:none:i:on:off:::
#mmrepquota::0:1:::nas:GRP:12047:12047:795392:0:0:0:none:62:0:0:0:none:i:on:off:::

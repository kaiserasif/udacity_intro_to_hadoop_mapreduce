#!/usr/bin/python

# just a counter

import sys

oldkey = None
count = 0

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        # something went wrong, skip
        continue

    key, value = data
    if oldkey and oldkey != key:
        print "{0}\t{1}".format(oldkey, count)
        count = 0

    oldkey = key
    count += 1

# last entry
if oldkey:
    print "{0}\t{1}".format(oldkey, count)

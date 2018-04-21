#!/usr/bin/python

# print key, value separated by tabs
# for project 2, ip and address/request description 

import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        ipaddr, identity, user, time, tz, method, page, http_version, status, size = data
        print "{0}\t{1}".format(ipaddr, 1)


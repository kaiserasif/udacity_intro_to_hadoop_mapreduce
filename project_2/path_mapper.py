#!/usr/bin/python

# print key, value separated by tabs
# for project 2, count most requested paths

import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        ipaddr, identity, user, time, tz, method, page, http_version, status, size = data
        # path after removing http://www.the-associates.co.uk
        prefix = "http://www.the-associates.co.uk"
        if page.startswith(prefix):
            page = page[len(prefix):]
        print "{0}\t{1}".format(page, 1)


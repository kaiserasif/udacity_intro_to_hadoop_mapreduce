#!/usr/bin/python

# key, value = tag, 1
# for Final Project
# Problem: Find Top 10 Tags, sorted by count
# Assumption: 1 reducer

import sys
import csv
import heapq


def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t')

    TopN = 10
    heap = []
    old_tag, count = None, 0
    for data in reader:
        if len(data) != 2: # something wrong
	    continue

	tag, i = data
	if old_tag and tag != old_tag: # process previous one
	    insert_record(heap, TopN, old_tag, count)
	    count = 0
	
	count += 1	
	old_tag = tag

    if old_tag: # process last student
	insert_record(heap, TopN, old_tag, count)

    # print results
    for item in heapq.nlargest(TopN, heap):
	writer.writerow(item)
	
def insert_record(heap, max_size, tag, count):
    heapq.heappush(heap, (count, tag))
    if len(heap) > max_size:
	heapq.heappop(heap)

def main():
    reducer()

if __name__ == "__main__":
    main()

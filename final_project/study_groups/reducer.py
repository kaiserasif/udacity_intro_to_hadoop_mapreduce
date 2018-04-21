#!/usr/bin/python

# key, value = original_question, student_id
# for Final Project
# Problem: Find Study Groups

import sys
import csv
import heapq


def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t')

    old_q, std_list = None, {}
    for data in reader:
        if len(data) != 2: # something wrong
	    continue

	q, std = data

	if old_q and q != old_q: # process previous one
	    writer.writerow([q, std_list.keys()])
	    std_list = {}
	
	std_list[std] = 1	
	old_q = q

    if old_q: # process last student
	writer.writerow([q, std_list.keys()])

def main():
    reducer()

if __name__ == "__main__":
    main()

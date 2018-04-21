#!/usr/bin/python

# key, value1, value2 = abs_parent_id, node_type (question, answer, comment), len(body)

import sys
import csv


def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t')

    old_parent, total, count = None, 0.0, 0
    for data in reader:
        if len(data) != 3: # something wrong
	    continue

	abs_parent, node_type, length = data
	if old_parent and abs_parent != old_parent: # process previous one
	    writer.writerow([old_parent, total / max(1, count)])
	    total, count = 0.0, 0
	if node_type == 'answer':
	    total += float(length)
	    count += 1	
	old_parent = abs_parent

    if old_parent: # process last student
	writer.writerow([old_parent, total / max(1, count)])
	

def main():
    reducer()

if __name__ == "__main__":
    main()

#!/usr/bin/python
# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

import sys
import csv

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    A, B = None, None

    for line in reader:
	if line[1] == "A": A = line
	else: B = line
	if A and B : # when both segments are received, sorted by key, so they will be grouped together
	    writer.writerow(B[2:] + A[2:])
	    A, B = None, None
        
        
        

if __name__ == "__main__":
    reducer()

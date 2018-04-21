#!/usr/bin/python

# print student_id, hour separated by tabs
# for Final Project
# Problem: Find most active hours per student


import sys
import re
import csv

def isInteger(text):
    try:
         int(text)
         return True
    except ValueError:
	 return False

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t', quoting=csv.QUOTE_ALL, quotechar='"')
    writer = csv.writer(sys.stdout, delimiter='\t')
	
    for line in reader:
        if len(line) > 9 and isInteger(line[0]):
	    (id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at,
	        score, state_string, last_edited_id, last_activity_by_id, last_activity_at,
   	        activity_revision_id, extra, extra_ref_id, extra_count, marked) = line
	    hour = added_at[added_at.index(' ')+1:added_at.index(':')]
	    writer.writerow([author_id, hour])

def main():
    mapper()

if __name__ == "__main__":
    main()

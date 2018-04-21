#!/usr/bin/python

# print tag, 1 separated by tabs
# for Final Project
# Problem: Find Top Ten Tags, sorted by count
# only question tags, skipping answers and comments
# Assumption: 1 reducer


import sys
import csv

def isInteger(text): # skip header by checking int('id')
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
	    
	    if node_type == 'question':
		tags = tagnames.split()
		for tag in tags:
		    writer.writerow([tag, 1])

def main():
    mapper()

if __name__ == "__main__":
    main()

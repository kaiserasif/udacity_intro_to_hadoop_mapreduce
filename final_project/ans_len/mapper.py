#!/usr/bin/python

# print root_post_id, post_type, post_length separated by tabs
# for Final Project
# Problem: Find average post length of answers per question
# question id needed, for len=0 posts
# node_type needed to separate 'answer' from 'question' and 'comment'


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
	    if abs_parent_id == '\N':
		abs_parent_id = id # root questions don't have parents
	    writer.writerow([abs_parent_id, node_type, len(body)])

def main():
    mapper()

if __name__ == "__main__":
    main()

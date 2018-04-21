#!/usr/bin/python

# key, value = student_id, hour
# print multiple tops
# for Final Project
# Problem: Find most active hours per student

import sys
import csv


def print_top_hours(student_id, hour_list, writer):
    hour_list = sorted(hour_list.iteritems(), key = lambda x : -x[1])
    top = hour_list[0][1]
    for (k, v) in hour_list:	
	if top != v: break # not equal to top occurences
	writer.writerow([student_id, int(k)]) #, v])
    

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t')

    old_student, hour_list = None, {}
    for data in reader:
        if len(data) != 2: # something wrong
	    continue
	student, hour = data
	if old_student and student != old_student: # process previous one
	    print_top_hours(old_student, hour_list, writer)
	    hour_list = {}
	hour_list[hour] = 1 if hour not in hour_list else hour_list[hour] + 1
	old_student = student

    if old_student: # process last student
	print_top_hours(old_student, hour_list, writer)
	

def main():
    reducer()

if __name__ == "__main__":
    main()

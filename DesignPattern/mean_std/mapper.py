#!/usr/bin/python

# print key, value separated by tabs
# for Design Pattern - Summerization Pattern
# Problem: Find Inverted index of forum posts


import sys
import csv
from datetime import datetime

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t')
	
    for data in reader:
        if len(data) == 6:
            date, time, store, item, cost, payment = data
	    weekday = datetime.strptime(date, '%Y-%m-%d').strftime("%A")
            writer.writerow([weekday, cost, 1])

def main():
    mapper()

if __name__ == "__main__":
    main()

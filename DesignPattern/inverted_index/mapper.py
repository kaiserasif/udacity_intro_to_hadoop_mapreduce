#!/usr/bin/python

# print key, value separated by tabs
# for Design Pattern - Summerization Pattern
# Problem: Find Inverted index of forum posts


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
        if len(line) > 4 and isInteger(line[0]):
	    line[4] = line[4].replace("\n", " ").replace("\r", " ").lower()
            words = re.split('\W+', line[4])
            for word in words:
                 if len(word) > 0:
	              writer.writerow([word, line[0]])

def main():
    mapper()

if __name__ == "__main__":
    main()

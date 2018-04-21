#!/usr/bin/python

# using purchase.txt
# key, value = weekday, cost

import sys
import csv

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t')

    oldday, total_cost, counts = None, 0, 0
    for data in reader:
         if len(data) != 3: # something wrong
             continue
         weekday, cost, count = data[0], float(data[1]), int(data[2])
         if oldday and oldday != weekday:
             writer.writerow([oldday, total_cost/counts, counts])
	     total_cost, counts = 0, 0

         oldday = weekday
         total_cost += cost * count
	 counts += count

    # last entry
    if oldday:
        writer.writerow([oldday, total_cost/counts, counts])

def main():
    reducer()

if __name__ == "__main__":
    main()

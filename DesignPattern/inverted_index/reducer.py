#!/usr/bin/python

# key, value = word, node_id

import sys
import csv

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t')

    oldword, node_list = None, []
    for data in reader:
         if len(data) != 2: # something wrong
             continue
         word, node_id = data[0], int(data[1])
         if oldword and oldword != word:
             # writer.writerow([oldword, ", ".join([str(i) for i in sorted(set(node_list))])])
	     print "{0}({2})\t{1}".format(oldword, " ,".join([str(i) for i in sorted(node_list)]), len(node_list))
	     node_list = []

         oldword = word
         node_list.append(node_id)

    # last entry
    if oldword:
        # writer.writerow([oldword, " ,".join([str(i) for i in sorted(set(node_list))])])
        print "{0}({2})\t{1}".format(oldword, " ,".join([str(i) for i in sorted(node_list)]), len(node_list))

def main():
    reducer()

if __name__ == "__main__":
    main()

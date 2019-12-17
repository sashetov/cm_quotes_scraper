#!/usr/bin/env python3
import csv
import sys
from tabulate import tabulate
def get_table(table_files):
    table = []
    for filename in table_files:
        with open(filename) as handle:
            csvreader = csv.reader(handle, delimiter=',', quotechar='"')
            for row in csvreader:
                table.append(row[0:2])
    return table
def pretty_print_table(table,headers):
    print(tabulate(table,headers))
def main():
    progname = sys.argv[0]
    table_files = sys.argv[1:]
    argc = len(table_files)
    if argc < 1:
        print(f"Usage:\n{progname} table_file1 table_file2 ...\n")
        exit(1)
    headers = ["Quote","Author"]
    table = get_table(table_files)
    pretty_print_table(table, headers)
if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import csv
import sys
from urllib.request import urlopen
from bs4 import BeautifulSoup
from tabulate import tabulate
def get_cm_quotes():
    table = []
    url_pref="http://www.criminalmindsfanwiki.com/page/Season+"
    url_post="+Quotes"
    seasons=14
    i = 1
    while i < seasons + 1:
        url = f"{url_pref}{i}{url_post}"
        soup = BeautifulSoup(urlopen(url).read(), features="html.parser")
        for row in soup.findAll('table')[0].tbody.findAll('tr'):
            quote = row.findAll('td')[1].find(text=True)
            author = row.findAll('td')[2].find(text=True)
            if quote and author and not quote == " " and not author == " ":
                row = [quote,author]
                table.append(row)
        i=i+1
    return table
def pretty_print_table(table,headers):
    print(tabulate(table,headers))
def main():
    headers = ["Quote","Author"]
    table = get_cm_quotes()
    pretty_print_table(table, headers)
if __name__ == "__main__":
    main()

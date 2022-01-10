#!/usr/bin/python3
"""search for a particular string in a webpage
   import beautiful soup to scrape the webpage
   import requests to get request the url
   and sys to get user input"""
import re
from bs4 import BeautifulSoup
import requests
import sys


if __name__ == "__main__":
    """use"""
    if len(sys.argv) < 2:
        print("Usage: ./webscrapper <url> <searched_string>")
        sys.exit(1)
    url = sys.argv[1]
    string_searched = sys.argv[2]
    r = requests.get(url).text
    soup = BeautifulSoup(r, features='lxml')
    power = soup.find(string=re.compile(f'{string_searched}'), recursive=True)
    print(power)
    print(len(power))



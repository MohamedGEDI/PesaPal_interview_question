|Name|Email|
|----|-----|
|Mohamed Gedi| gedimohammed@gmail.com|


#Introduction

Question 4 of the PesaPal application



#Problem
Write an application which, when given a web page will download the text on it and output a sorted list of the unique words on the page, with counts of the occurrences.


##Requirements
###imports
1. requests
2. sys
3. beautifulsoup4
4. re


##Usage
Usage: ./webscrapper url string


##Solution
Get request the given url and parse the response from bytes to text.
Use Beautifulsoup4 to parse the text to easy to read html version.
Search through the html parsed text using regex for the inputted string



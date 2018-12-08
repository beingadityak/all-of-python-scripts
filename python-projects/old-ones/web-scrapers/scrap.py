# a silly web scraper for scraping
# list of data structures topics from GeeksForGeeks

import requests
from bs4 import BeautifulSoup

URL = "http://www.geeksforgeeks.org/data-structures/"

r = requests.get(URL)
soup = BeautifulSoup(r.content,'html5lib')

algos = []

table = soup.find('ol')

for row in table.findAll('li'):
    algo = {}
    algo['url'] = row.a['href']
    algos.append(algo)

print(algos)
#Python program to scrape website 
#and save quotes from website
import requests
from bs4 import BeautifulSoup
import json
 
URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL)

fo = open("inspire_quotes.json","a+");
fo.write("\n\n");

soup = BeautifulSoup(r.content, 'html5lib')
 
quotes=[]  # a list to store quotes
 
table = soup.find('div', attrs = {'id':'container'})
 
for row in table.findAll('div', attrs = {'class':'quote'}):
    quote = {}
    quote['theme'] = row.h5.text
    quote['img'] = row.img['src']
    quote['lines'] = row.h6.text
    quote['author'] = row.p.text
    quotes.append(quote)
 
# print(quotes)

json.dump(quotes,fo)
fo.close()

print('The JSON is generated ! Enjoy !!')
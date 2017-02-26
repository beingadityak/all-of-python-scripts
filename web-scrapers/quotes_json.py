#Python program to scrape website 
#and save quotes from website
import requests
from bs4 import BeautifulSoup
import json
 
fo = open("inspire_quotes.json","a+");

urlList = ["http://www.values.com/inspirational-quotes","http://www.values.com/inspirational-quotes?page=2","http://www.values.com/inspirational-quotes?page=3","http://www.values.com/inspirational-quotes?page=4","http://www.values.com/inspirational-quotes?page=5","http://www.values.com/inspirational-quotes?page=6","http://www.values.com/inspirational-quotes?page=7","http://www.values.com/inspirational-quotes?page=8","http://www.values.com/inspirational-quotes?page=9","http://www.values.com/inspirational-quotes?page=10","http://www.values.com/inspirational-quotes?page=11","http://www.values.com/inspirational-quotes?page=12","http://www.values.com/inspirational-quotes?page=13","http://www.values.com/inspirational-quotes?page=14","http://www.values.com/inspirational-quotes?page=15","http://www.values.com/inspirational-quotes?page=16","http://www.values.com/inspirational-quotes?page=17","http://www.values.com/inspirational-quotes?page=18","http://www.values.com/inspirational-quotes?page=19","http://www.values.com/inspirational-quotes?page=20"]

for URL in urlList:
    r = requests.get(URL)
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
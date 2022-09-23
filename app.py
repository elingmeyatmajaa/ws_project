import csv
import requests
from bs4 import BeautifulSoup

# URL = "https://id.77577.live/id/post/index"
URL ='http://www.values.com/inspirational-quotes'
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}

r = requests.get(url=URL, headers=headers)

soup = BeautifulSoup(r.content, 'html5lib')

quotes=[] # alist to store quotes

table = soup.find('div', attrs={'id':'all_quotes'})

# print(table.prettify)
for row in table.findAll('div', attrs={'class':'col-6 col-lg-4 text-center margin-30px-bottom sm-margin-30px-top'}):
    quote = {}
    quote['theme'] = row.h5.text
    quote['url'] = row.a['href']
    quote['img'] = row.img['src']
    quote['lines'] = row.img['alt'].split(" #")[0]
    quote['author'] = row.img['alt'].split(" #")[1]
    quotes.append(quote)

filename = 'inspirational_quotes.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f, ['theme', 'url', 'img', 'lines', 'author'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)

# 
# 
# # print(soup.prettify())

# for page in range(1,10):

# page = requests.get(URL)

# print(page.text)
# soup = BeautifulSoup(page.content, "html.parser")
# results = soup.find(id="ResultsContainer")

# results = soup.find(id="ResultsContainer")
# print(results.prettify())
import csv
import requests
from bs4 import BeautifulSoup

URL = "https://en.77577.live/en/post/index"
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}

r = requests.get(url=URL, headers=headers)

soup = BeautifulSoup(r.content, 'html5lib')
# print(soup)

quotes=[] # alist to store quotes
# count = 1
table = soup.find('div', attrs={'class':'row p-0 m-0 mb-3'})

# print(table.prettify)
for row in table.findAll('div', attrs={'class':'col-md-6 p-1'}):
    quote = {}
    quote['title'] = row.p.text
    # quote['url'] = row.a['href']
    quote['img'] = row.img['src']
    quote['date'] = row.small.text
    # count += 1
    # quote['lines'] = row.img['alt'].split(" #")[0]
#     quote['author'] = row.img['alt'].split(" #")[1]
    quotes.append(quote)

filename = 'article_news.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f, ['title', 'img', 'date'])
    w.writeheader()

    # w.writerow(quote)
    for quote in quotes:
        w.writerow(quote)
print('success webscrepping. file in \WEBSCRAPPING')


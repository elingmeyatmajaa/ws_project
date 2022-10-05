import csv
import requests
from bs4 import BeautifulSoup
from pprint import pprint


URL = "https://republika.co.id/kanal/sepakbola"
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}

r = requests.get(url=URL, headers=headers)
# print(r)

soup = BeautifulSoup(r.content, 'html5lib')
# print(soup)

articles=[] 
table = soup.find('div', attrs={'class':'conten_kanal'})
# print(table)

# URL = link.contents[0].find_all('a')[0] 
# for link in soup.find_all('a', attrs={'class':'content1'}):
#     print(link.get('href'))

# for row in table.findAll('a', href=True):
#     print(row['href'])

for row in table.findAll('div', attrs={'class':'teaser_conten1_center'}):
    # print(row)
    article = {}
    article['category'] = row.p.text
    article['title'] = row.h2.text
    article['content'] = row.p.text
  
    # article['href'] = row.a['href']
    # article['img'] = row.img['data-original']
    # article['date'] = row.p.text
   
    articles.append(article)
    pprint(article)

# filename = 'article.csv'
# with open(filename, 'w', newline='') as f:
#     w = csv.DictWriter(f, ['category', 'title','href', 'img'])
#     w.writeheader()
#     for article in articles:
#         w.writerow(article)
# print('success webscrepping. file in \WEBSCRAPPING')


import csv
from attr import attrs
import requests
from bs4 import BeautifulSoup
from pprint import pprint


# from selenium import  webdriver
# driver= webdriver.Firefox()


URL = "https://www.sportingnews.com/us/soccer/news"
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}

r = requests.get(url=URL, headers=headers)

# eleml = drive.find_element_by_link_text("Load More")
# eleml.click()

soup = BeautifulSoup(r.content, 'html.parser', multi_valued_attributes=None)

articles=[] 
table = soup.find('div', attrs={'class':'view-content'})


for row in table.findAll('div', attrs={'role':'article'}):
    article = {}
    list =  row.div.text
    article['title'] =  list.strip()
    article['img'] = row.source['srcset']
    article['href'] = "https://www.sportingnews.com" + row.a['href']
    articles.append(article)
    pprint(article)

# filename = 'article_sportingnews.csv'
# with open(filename, 'w', newline='') as f:
#     w = csv.DictWriter(f, ['title','img', 'href'])
#     w.writeheader()
#     for article in articles:
#         w.writerow(article)
# print('success webscrepping. file in \WEBSCRAPPING')


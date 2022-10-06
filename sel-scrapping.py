import time
from numpy import tile
import requests
from bs4 import BeautifulSoup
import json
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pprint import pprint

base = "https://www.sportingnews.com"
browser = webdriver.Chrome('D:/REPOSITORY/python_project/chromedriver.exe')
wait = WebDriverWait(browser, 10)
browser.get('https://www.sportingnews.com/us/soccer/news')
while True:
    try:
        time.sleep(1)
        show_more = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@class="button"][contains(.,"Load more")]')))  
        show_more.click()
    except Exception as e:
            print(e)
            break    

soup = BeautifulSoup(browser.page_source,'lxml')
search_results = soup.find('div', {'class':'trending-news__list'})

links = search_results.find_all('a')
for link in links:
    link_url = link['href']

    title = link.find_next('a').text
    print(title + '\n' + link_url + '\n')

    response = requests.get(base + link_url)

    soup_link = BeautifulSoup(response.content, 'html.parser',  multi_valued_attributes=None)
    articles=[]

    table = soup_link.find('div', attrs={'class':'article-page'})
    
    article ={}

    article['title'] = table.h1.text
    article['img'] = table.img['src']
    article['content'] = table.find_all('p')
    articles.append(article)
    pprint(article)
    # print(soup_link)

    # scripts = soup_link.find_all('script')
    # for script in scripts:
    #     if 'window.__preloadedData = ' in script.text:
    #         jsonStr = script.text
    #         jsonStr = jsonStr.split('window.__preloadedData = ')[-1]
    #         jsonStr = jsonStr.rsplit(';',1)[0]

    #         jsonData = json.loads(jsonStr)
    #         print(jsonData)

    #         article = []
    #         for k, v in jsonData['initialState'].items():
    #             w=1
    #             try:
    #                 if v['__typename'] == 'TextInline':
    #                     article.append(v['text'])

    #             except:
    #                 continue
    #         article = [ each.strip() for each in article ]
    #         article = ''.join([('' if c in string.punctuation else ' ')+c for c in article]).strip()
    # print (article + '\n')

print("Complete")

browser.quit()
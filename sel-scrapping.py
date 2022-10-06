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

    response = requests.get(base + link_url)

    soup_link = BeautifulSoup(response.content, 'html.parser',  multi_valued_attributes=None)
    articles=[]

    table = soup_link.find('div', attrs={'class':'article-page'})
    
    article ={}

    article['title'] = table.h1.text
    article['img'] = table.source['srcset']
    a = table.find_all('p')
    article['content'] = str(a).replace('[','').replace(']','')

    articles.append(article)
    pprint(article)
print("Complete")

browser.quit()
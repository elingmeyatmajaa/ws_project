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
import csv
from datetime import datetime
import re
from slugify import slugify



from selenium.webdriver.chrome.options import Options
from selenium import webdriver

options = Options()
options.add_argument('--no-sandbox')
options.add_argument("--headless")
options.add_argument('--disable-dev-shm-usage')

# import mysql.connector
import mysql.connector as mysql

import html


# driver = webdriver.Chrome('./chromedriver', options = options)

base = "https://www.livescore.com/"
browser = webdriver.Chrome('D:/REPOSITORY/python_project/driver/chromedriver.exe')
# browser = webdriver.Chrome('/home/eling/chromedriver', options = options)
wait = WebDriverWait(browser, 10)
browser.get('https://www.livescore.com/en/news/world-cup-2022-qatar/')
# while True:
#     try:
#         time.sleep(1)
#         show_more = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@class="button"][contains(.,"Load more")]')))  
#         show_more.click()
#     except Exception as e:
#             print(e)
#             break    

soup = BeautifulSoup(browser.page_source,'lxml')
# print(soup.prettify())
search_results = soup.find('div', {'class':'jj'})
# print(search_results)

# article ={}
mydb = mysql.connect(
        host="localhost",
        user="root",
        password="strong_password1234",
        database="db_test_allfootball"
)

links = search_results.find_all('div',attrs={'class':'lj'} )
# print(links)

for link in links:
    
    link_url = link.a['href']
    

    response = requests.get("https://www.livescore.com" + link_url)

    soup_link = BeautifulSoup(response.text, 'html5lib')

    table = soup_link.find('div', attrs={'data-testid':'article-content_wrapper'})
    # print(table)
   
    # a = '1'
    a = '21'
    cc = table.figure.img['src']
    b = cc.partition("?")[0].strip()
    c = table.h1.text
    d = ' '
    e = ' '
    f = ' '
    aa = table.find_all('p')
    # html_pattern = "<(?:\"[^\"]*\"['\"]*|'[^']*'['\"]*|[^'\">])+>"
    g = str(aa).replace('[','').replace(']','')
    h = ' '
    i = ' '
    j = ' '
    k = slugify(c)
    l = '7'
    m = datetime.now()

    # print(a,b,c,d,e,f,g,h,i,j,k,l,m)

    mycursor = mydb.cursor()

    query = "INSERT INTO artikel_posts(id_kategori,sampul, judul,judulVi, judulCn, judulId, konten,kontenVi,kontenCn,kontenId,slug, user_id, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    values = (a,b,c,d,e,f,g,h,i,j,k,l,m)

    mycursor.execute(query, values)

mydb.commit()
print(mycursor.rowcount, "was inserted.")

  
print("Complete")

browser.quit()
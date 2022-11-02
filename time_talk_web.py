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

base = "https://www.teamtalk.com"
browser = webdriver.Chrome('D:/REPOSITORY/python_project/driver/chromedriver.exe')
# browser = webdriver.Chrome('/home/eling/chromedriver', options = options)
wait = WebDriverWait(browser, 10)
browser.get('https://www.teamtalk.com/english-premiership')
# while True:
#     try:
#         time.sleep(1)
#         show_more = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@class="button"][contains(.,"Load more")]')))  
#         show_more.click()
#     except Exception as e:
#             print(e)
#             break    

soup = BeautifulSoup(browser.page_source,'lxml')
# print(soup)
# print(soup.prettify())
search_results = soup.find('div', {'class':'mt-5 space-y-3'})
# print(search_results)

# article ={}
mydb = mysql.connect(
        host="localhost",
        user="root",
        password="strong_password1234",
        database="db_starting_sport_dev"
)

links = search_results.find_all('div',attrs={'class':'flex-1 flex flex-col xs:flex-row items-stretch'} )
# print(links)

for link in links:
    
    link_url = link.a['href']
    # print(link_url)
    

    response = requests.get(link_url)

    soup_link = BeautifulSoup(response.text, 'html5lib')

    table = soup_link.find('article', attrs={'class':'lg:mt-5 lg:mb-10 rounded-lg lg:shadow-primary ps-article-content'})
    # print(table.h1.text)
    # print(table.img['src'])
    
    
    # print(h)

   
    a = '1'
    b = '1'
    c = table.img['src']
    d = table.h1.text
    e = ' '
    f = ' '
    g = ' '
    aa = table.find_all('p')
    html_pattern = "<(?:\"[^\"]*\"['\"]*|'[^']*'['\"]*|[^'\">])+>"
    h = re.sub(html_pattern, '', str(aa).replace('[','').replace(']',''))
    i = ' '
    j = ' '
    k = ' '
    l = ' '
    m = '1'
    n = datetime.now()

    # print(a,b,c,d,e,f,g,h,i,j,k,l,m,n)

    mycursor = mydb.cursor()

    query = "INSERT INTO artikel_posts(id_main_kategori,id_kategori,sampul, judul,judulVi, judulCn, judulId, konten,kontenVi,kontenCn,kontenId,slug, user_id, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    values = (a,b,c,d,e,f,g,h,i,j,k,l,m,n)

    mycursor.execute(query, values)

mydb.commit()
print(mycursor.rowcount, "was inserted.")

  
print("Complete")

browser.quit()
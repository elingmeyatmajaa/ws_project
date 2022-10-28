from ast import If
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


from selenium.webdriver.chrome.options import Options
from selenium import webdriver

options = Options()
options.add_argument('--no-sandbox')
options.add_argument("--headless")
options.add_argument('--disable-dev-shm-usage')

import mysql.connector
import mysql.connector as mysql

import html

mydb = mysql.connect(
        host="localhost",
        user="root",
        password="strong_password1234",
        database="db_starting_sport_dev"
)

# driver = webdriver.Chrome('./chromedriver', options = options)

base = "https://www.fotmob.com"
browser = webdriver.Chrome('D:/REPOSITORY/python_project/chromedriver.exe')
# browser = webdriver.Chrome('/home/eling/chromedriver', options = options)
wait = WebDriverWait(browser, 10)
browser.get('https://www.fotmob.com/world?page=3')
 

soup = BeautifulSoup(browser.page_source,'lxml')
# print(soup)
search_results = soup.find('section', {'class':'css-76ndue-WorldNewsCSS e1p0v7yy3'})

# article ={}


links = search_results.find_all('a')
# print(links)
# print(search_results)
for link in links:
    
    link_url = link['href']
    
    

    response = requests.get(base + link_url)
   
    
    soup_link = BeautifulSoup(response.text, 'lxml')
    c = soup_link.find("meta", property="og:image")
    hh = soup_link.find('div', {'class': 'css-1qy2ihy-iaContentBodyCSS'})

    h = str(hh).replace('<div class="css-1qy2ihy-iaContentBodyCSS">','').replace('</div>', '')
    
    a = '1'
    b = '1'
    cc = soup_link.find("meta", property="og:image")
    c = cc['content']
    d = link.h3.text
    e = ' '
    f = ' '
    g = ' '
    h = str(hh).replace('<div class="css-1qy2ihy-iaContentBodyCSS">','').replace('</div>', '')
    i = ' '
    j = ' '
    k = ' '
    l = ' '
    m = '1'
    n = datetime.now()


    mycursor = mydb.cursor()

    query = "INSERT INTO artikel_posts(id_main_kategori,id_kategori,sampul, judul,judulVi, judulCn, judulId, konten,kontenVi,kontenCn,kontenId,slug, user_id, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    values = (a,b,c,d,e,f,g,h,i,j,k,l,m,n)

    mycursor.execute(query, values)

mydb.commit()
print(mycursor.rowcount, "was inserted.")

  
print("Complete")

browser.quit()
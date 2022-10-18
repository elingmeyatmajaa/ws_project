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

# import mysql.connector
import mysql.connector as mysql

import html


# driver = webdriver.Chrome('./chromedriver', options = options)

base = "https://www.cbssports.com/"
browser = webdriver.Chrome('D:/REPOSITORY/python_project/chromedriver.exe')
# browser = webdriver.Chrome('/home/eling/chromedriver', options = options)
wait = WebDriverWait(browser, 10)
browser.get('https://www.cbssports.com/nba')
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
search_results = soup.find('div', {'class':'row'})
# print(search_results)

# article ={}
# mydb = mysql.connect(
#         host="localhost",
#         user="root",
#         password="strong_password1234",
#         database="db_starting_sport_dev"
# )

links = search_results.find_all('li',attrs={'class':'col-4 article-list-pack-item'} )

for link in links:
   
    
    link_url = link.a['href']
    # print(link_url)
    

    response = requests.get(base + link_url)
    print(response)

    # soup_link = BeautifulSoup(response.text, 'html5lib')
#     articles=[]

    # table = soup_link.find('div', attrs={'data-testid':'article-content_wrapper'})
    # print(table.h1.text)

    # a = table.h1.text
    # cc = table.figure.img['src']
    # b = cc.partition("?")[0].strip()
    # aa = table.find_all('p')
    # c = str(aa).replace('[','').replace('<p>','').replace('</p>','').replace('<a>','').replace('</a>','').replace('<strong>','').replace('</strong>','').replace(']','')

    # print(b)

    # print(c)
    # a = '1'
    # b = '1'
    # cc = table.figure.img['src']
    # c = cc.partition("?")[0].strip()
    # d = table.h1.text
    # e = ' '
    # f = ' '
    # g = ' '
    # aa = table.find_all('p')
    # h = str(aa).replace('[','').replace('<p>','').replace('</p>','').replace('<a>','').replace('</a>','').replace('<strong>','').replace('</strong>','').replace(']','')
    # i = ' '
    # j = ' '
    # k = ' '
    # l = ' '
    # m = '1'
    # n = datetime.now()

    # print(a,b,c)

#     mycursor = mydb.cursor()

#     query = "INSERT INTO artikel_posts(id_main_kategori,id_kategori,sampul, judul,judulVi, judulCn, judulId, konten,kontenVi,kontenCn,kontenId,slug, user_id, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

#     values = (a,b,c,d,e,f,g,h,i,j,k,l,m,n)

#     mycursor.execute(query, values)

# mydb.commit()
# print(mycursor.rowcount, "was inserted.")

  
print("Complete")

browser.quit()
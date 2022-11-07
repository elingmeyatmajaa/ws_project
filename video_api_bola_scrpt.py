import time
from jmespath import search
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

mydb = mysql.connect(
        host="localhost",
        user="root",
        password="strong_password1234",
        database="db_test_allfootball"
)

# driver = webdriver.Chrome('./chromedriver', options = options)

base = "https://www.bola.com/"
# browser = webdriver.Chrome('/home/eling/chromedriver', options = options)
browser = webdriver.Chrome('D:/REPOSITORY/python_project/driver/chromedriver.exe')
wait = WebDriverWait(browser, 10)
browser.get('https://www.bola.com/video/indeks')


soup = BeautifulSoup(browser.page_source,'lxml')
search_results = soup.find('div', {'class':'articles--list articles--list_rows'})


links = search_results.find_all('figure',attrs={'class':'articles--rows--item__figure-thumbnail'} )

# print(links)

for link in links:
    # print(link)
    
    link_url = link.a['href']
    # print(link_url)

    response = requests.get(link_url)
    # print(response)

    soup_link = BeautifulSoup(response.text, 'html5lib')
  
    table = soup_link.find('div', {'class':'read-page-upper'})

    a = '1'
    b = link.img['src']
    c = table.iframe['src']
    d = ' '
    e = table.h1.text
    f = ' '
    g = ' '
    h = '1'
    i = datetime.now()


    # print(a,b,c,d,e,f,g,h,i)

    mycursor = mydb.cursor()

    query = "INSERT INTO videos(id_kategori_video,covers, file, description, descriptionId, descriptionVi, descriptionCn,user_id, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

    values = (a,b,c,d,e,f,g,h,i)

    mycursor.execute(query, values)

mydb.commit()
mydb.close()
print(mycursor.rowcount, "was inserted.")


print("Complete")

browser.quit()
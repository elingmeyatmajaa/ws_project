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

mydb = mysql.connect(
        host="localhost",
        user="root",
        password="strong_password1234",
        database="db_starting_sport_dev"
)

# driver = webdriver.Chrome('./chromedriver', options = options)

base = "https://www.bola.com/"
browser = webdriver.Chrome('/home/eling/chromedriver', options = options)
# browser = webdriver.Chrome('D:/REPOSITORY/python_project/chromedriver.exe')
wait = WebDriverWait(browser, 10)
browser.get('https://www.bola.com/video')


soup = BeautifulSoup(browser.page_source,'lxml')
# print(soup.prettify())
links = soup.find_all('article', {'class':'gallery--grid--video'})
# print(search_results)


for link in links:
    
    link_url = link.a['href']
    # b = link.a.text
   
   

    response = requests.get(link_url)
    # print(response)

    soup_link = BeautifulSoup(response.text, 'html5lib')
    # print(soup_link)
    # articles=[]

    table = soup_link.find('div', {'class':'container-article'})
    # table = soup_link.find('article', {'class':'article'})

    # a = table['src']
    # b = table.h1.text
    # print(a)
 
# returns current date and time

    a = '1'
    b = '1'
    c = table.iframe['src']
    d = link.img['src']
    e = table.h1.text
    f = ' '
    g = ' '
    h = ' '
    i = '1'
    j = datetime.now()

    # print(f)

    # print(a,b,c,d,e,f,g,h,i)

    mycursor = mydb.cursor()

    query = "INSERT INTO video_posts(id_kategori_video,id_main_kategori_video, file,cover, description, descriptionId, descriptionVi, descriptionCn,user_id, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    values = (a,b,c,d,e,f,g,h,i,j)

    mycursor.execute(query, values)

mydb.commit()
print(mycursor.rowcount, "was inserted.")


print("Complete")

browser.quit()
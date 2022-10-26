from lib2to3.pgen2 import driver
import time
from urllib import response
import bs4
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

base = "https://www.wdbj7.com"
# browser = webdriver.Chrome('/home/eling/chromedriver', options = options)
browser = webdriver.Chrome('D:/REPOSITORY/python_project/chromedriver.exe')
wait = WebDriverWait(browser, 10)
browser.get('https://www.wdbj7.com/2022/10/25/liberty-basketball-prepares-season-opener/')


soup = BeautifulSoup(browser.page_source,'lxml')


search_results = soup.find('div', {'class':'article-header article row mb-3'})


image = json.loads(search_results.find("script").text)



a = '1'
b = '1'
c = image['contentUrl']
d = image['thumbnailUrl']
e = image['description']
f = ' '
g = ' '
h = ' '
i = '1'
j = datetime.now()

# print(a,b,c,d,e)

mycursor = mydb.cursor()

query = "INSERT INTO video_posts(id_kategori_video,id_main_kategori_video, file,cover, description, descriptionId, descriptionVi, descriptionCn,user_id, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

values = (a,b,c,d,e,f,g,h,i,j)

mycursor.execute(query, values)

mydb.commit()
print(mycursor.rowcount, "was inserted.")




print("Complete")

browser.quit()
import time
from urllib import response
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
# import mysql.connector as mysql

# import html

# mydb = mysql.connect(
#         host="localhost",
#         user="root",
#         password="xxx",
#         database="xxx"
# )

# driver = webdriver.Chrome('./chromedriver', options = options)

base = "https://www.sport.es/"
# browser = webdriver.Chrome('/home/eling/chromedriver', options = options)
browser = webdriver.Chrome('D:/REPOSITORY/python_project/chromedriver.exe')
wait = WebDriverWait(browser, 10)
browser.get('https://www.sport.es/en')


soup = BeautifulSoup(browser.page_source,'lxml')

links = soup.find('h2', {'class':'title'})
link_url = links.a['href']

response = requests.get(link_url)


soup_link = BeautifulSoup(response.content, 'html5lib')

table = soup_link.find('article', {'class':'newdetail'})

tables_1 = soup_link.find('div', {'class':'col-xs-12 col-sm-12 col-md-8 col-lg-8 col'})

a = table.h1.text
b = table.img['src']

c = tables_1.figure.div['data-video-file']


print(a,b,c)

print("Complete")

browser.quit()
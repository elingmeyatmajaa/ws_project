from lib2to3.pgen2 import driver
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

base = "https://www.foxsports.com.au/"
# browser = webdriver.Chrome('/home/eling/chromedriver', options = options)
browser = webdriver.Chrome('D:/REPOSITORY/python_project/chromedriver.exe')
wait = WebDriverWait(browser, 10)
browser.get('https://www.foxsports.com.au/video/basketball/wnbl/flames-star-ready-to-fire-in-wnbl!836407')


soup = BeautifulSoup(browser.page_source,'lxml')
# print(soup)

# search_results1 = soup.find('img', itemprop="thumbnailUrl")

search_results = soup.find('div', {'class':'styles__VideoPlayerWrapper-sc-l83x2x-3 gQuvyE'})
search_results1 = soup.find('img', itemprop="thumbnailUrl")

search_result_title = soup.find('span', {'class':'styles__VideoTitle-sc-l83x2x-10 gmJKwN'})

url = search_results.find("meta", itemprop="contentURL")
# print(search_results1['src'])


a = '1'
b = '1'
c = url["content"]
d = search_results1['src']
e = str(search_result_title).replace('<span class="styles__VideoTitle-sc-l83x2x-10 gmJKwN">','').replace('</span>','')
f = ' '
g = ' '
h = ' '
i = '1'
j = datetime.now()

mycursor = mydb.cursor()

query = "INSERT INTO video_posts(id_kategori_video,id_main_kategori_video, file,cover, description, descriptionId, descriptionVi, descriptionCn,user_id, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

values = (a,b,c,d,e,f,g,h,i,j)

mycursor.execute(query, values)

mydb.commit()
print(mycursor.rowcount, "was inserted.")
# print(a,b,c,d,e,f,g,h,i,j)

# print(url['content'])
# links = search_results.find_all('div', attrs={'class':'styles__ThumbnailWrapper-sc-1d7lsd2-6 dKPzei'})

# for link in links:

# 	link_url = link.a['href']

# 	browser.get("https://www.foxsports.com.au/" + link_url)

# 	soup_link = BeautifulSoup(browser.page_source,'lxml')
# 	print(link)

	# search_results1 = soup_link.find('img', itemprop="thumbnailUrl")
	# search_result_title = soup_link.find('span', {'class':'styles__VideoTitle-sc-l83x2x-10 gmJKwN'})

	# search_results = soup_link.find('div', {'class':'styles__VideoPlayerWrapper-sc-l83x2x-3 gQuvyE'})
	# url = search_results.find("meta", itemprop="contentURL")
	
	

	# a = '1'
	# b = '1'
	# c = url["content"]
	# d = search_results1['src']
	# e = str(search_result_title).replace('<span class="styles__VideoTitle-sc-l83x2x-10 gmJKwN">','').replace('</span>','')
	# f = ' '
	# g = ' '
	# h = ' '
	# i = '1'
	# j = datetime.now()
	


	# mycursor = mydb.cursor()

	# query = "INSERT INTO video_posts(id_kategori_video,id_main_kategori_video, file,cover, description, descriptionId, descriptionVi, descriptionCn,user_id, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

	# values = (a,b,c,d,e,f,g,h,i,j)

	# mycursor.execute(query, values)

	# mydb.commit()
	# print(mycursor.rowcount, "was inserted.")

# print("Complete")

# browser.quit()
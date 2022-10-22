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
browser.get('https://www.foxsports.com.au/video/basketball/nbl/sixers-cook-the-kings-in-sydney!836571')


soup = BeautifulSoup(browser.page_source,'lxml')
# print(soup)
# print(soup)
search_results1 = soup.find('img', itemprop="thumbnailUrl")
# image = (search_results1['src'])

# search_results2 = soup.find('div', {'class':'styles__VideoTitleWrapper-sc-l83x2x-9 fiYrIt'})
# print(search_results2.span.text)


search_results = soup.find('div', {'class':'styles__VideoPlayerWrapper-sc-l83x2x-3 gQuvyE'})
url = search_results.find("meta", itemprop="contentURL")

# link_url = links.a['href']
# print(links)
# print(search_results.meta.meta['content'])


# response = requests.get(link_url)
# links = search_results.find_all('li',attrs={'class':'ArticleGrid_articleGridColumnQuarter__WhOHk'} )

# for link in links:
	# print(link)
	# link_url = link.a['href']
	# print(link_url)
	# browser.get("https://www.nba.com/" + link_url)

	# soup_link =  BeautifulSoup(browser.page_source,'lxml')
	# print(soup_link)

	

	# response = requests.get("https://www.nba.com/" + link_url)
	# print(response)
	
	# soup_link = BeautifulSoup(driver.page_source)

	# table = soup_link.find('div', attrs={'class':'brand-font VideoPlayer_videoPlayer__eVA7E'})
	
	# a = table.h2.text
	# b = table.video.text	
	# print(soup_link.video.text)
	# a = (table.h1.text)
	# b = (table.)
	# print(a)
	
	# print(table.h1.text)
# soup_link = BeautifulSoup(response.content, 'html5lib')

# table = soup_link.find('article', {'class':'newdetail'})

# tables_1 = soup_link.find('div', {'class':'col-xs-12 col-sm-12 col-md-8 col-lg-8 col'})

a = '1'
b = '1'
c = url["content"]
d = (search_results1['src'])
e = 'Sixers cook the Kings in Sydney'
f = ' '
g = ' '
h = ' '
i = '1'
j = datetime.now()

# print(a,b,c,d,e,f,g,h,i,j)


mycursor = mydb.cursor()

query = "INSERT INTO video_posts(id_kategori_video,id_main_kategori_video, file,cover, description, descriptionId, descriptionVi, descriptionCn,user_id, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

values = (a,b,c,d,e,f,g,h,i,j)

mycursor.execute(query, values)

mydb.commit()
print(mycursor.rowcount, "was inserted.")

print("Complete")

browser.quit()
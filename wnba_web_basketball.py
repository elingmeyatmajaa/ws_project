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

base = "https://www.wnba.com"
# browser = webdriver.Chrome('/home/eling/chromedriver', options = options) 
browser = webdriver.Chrome('D:/REPOSITORY/python_project/driver/chromedriver.exe')
wait = WebDriverWait(browser, 10)
browser.get('https://www.wnba.com/video/?channel=playbyplay')


soup = BeautifulSoup(browser.page_source,'lxml')
# print(soup)


search_results = soup.find('section', {'class':'row video-archive__content'})

links = search_results.find_all('a')

for link in links:
        # print(link)
        link_url = link['href']
        
        response = requests.get(link_url)

        soup_link = BeautifulSoup(response.text, 'lxml')
        vid = soup_link.find('div',{'class':'video-theatre__stage'})
        # print(c.video['data-video-id-large'])
        # print(c.video['data-video-thumb-medium'])
        # print(c.h1.text)
        text = soup_link.find('header', {'class':'video-theatre__header'})
        # print(d.h1.text)
        
        # print(response)
        # print(link_url)
# image = json.loads(search_results.find("script").text)



        a = '2'
        b = '2'
        c = vid.video['data-video-id-large']
        d = vid.video['data-video-thumb-medium']
        e = text.h1.text
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
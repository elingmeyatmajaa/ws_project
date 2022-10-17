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

base = "https://www.sport.es/"
# browser = webdriver.Chrome('/home/eling/chromedriver', options = options)
browser = webdriver.Chrome('D:/REPOSITORY/python_project/chromedriver.exe')
wait = WebDriverWait(browser, 10)
browser.get('https://www.sport.es/en')
# while True:
#     try:
#         time.sleep(1)
#         show_more = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@class="text"][contains(.,"See More")]')))  
#         show_more.click()
#     except Exception as e:
#             print(e)
#             break    


soup = BeautifulSoup(browser.page_source,'lxml')

search_results = soup.find('div', {'class':'col-xs-12 col-sm-12 col-md-8 col-lg-9 pub-lg-8 col'})
# print(links)


links = search_results.find_all('h2',class_ = 'title')
# print(links)


for link in links:
    # print(link.a['href'])
   
    link_url = link.a['href']


    response = requests.get(link_url)
    # print(response)




    soup_link = BeautifulSoup(response.content, 'html5lib')



    table = soup_link.find('article', {'class':'newdetail'})



    # tables_1 = soup_link.find('div', {'class':'col-xs-12 col-sm-12 col-md-8 col-lg-8 col'})

    # a = table.h1.text
    # b = table.img['src']
    # c = table.figure.div['data-video-file']

    a = '1'
    b = '1'
    c = table.figure.div['data-video-file']
    d = table.img['src']
    e = table.h1.text
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

print("Complete")

browser.quit()
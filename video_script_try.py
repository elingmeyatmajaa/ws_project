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
        password="3c065435b63a57e6",
        database="starting_sport_dev"
)

# driver = webdriver.Chrome('./chromedriver', options = options)

base = "https://www.bola.com/"
browser = webdriver.Chrome('/home/eling/chromedriver', options = options)
# browser = webdriver.Chrome('D:/REPOSITORY/python_project/chromedriver.exe')
wait = WebDriverWait(browser, 10)
browser.get('https://www.bola.com/video')
# while True:
#     try:
#         time.sleep(1)
#         show_more = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="link channel-section-content__load"][contains(.,"Load more channels ")]')))  
#         show_more.click()
#     except Exception as e:
#             print(e)
#             break    

soup = BeautifulSoup(browser.page_source,'lxml')
# print(soup.prettify())
links = soup.find_all('article', {'class':'gallery--grid--video'})
# print(search_results)

# a = search_results['src']
# b = search_results.a.text
# print(a)

# article ={}
# mydb = mysql.connect(
#         host="localhost",
#         user="root",
#         password="3c065435b63a57e6",
#         database="starting_sport_dev"
# )

# links = search_results.find_all('div',attrs={'class':'channel-section-content__item-wrapper'} )
# print(links.a.name)

# link_url = links.find_all('a')
# print(link_url)
for link in links:
    # link.a['href']
    
    link_url = link.a['href']
    # print(link_url)

    # print ("The list is: " + str(link_url)) 

    # remove duplicated from list 
    # result = [] 
    # for i in link_url: 
    #     if i not in result: 
    #         result.append(i) 
    # print ("The list after removing duplicates : " + str(result)) 

    # # a = list(set(link_url))
    # a = list(dict.fromkeys(link_url))
    # print(a)

# title = links.find_nevasdaxt('a').text
# print(title)

    response = requests.get(link_url)
    # print(response)

    soup_link = BeautifulSoup(response.text, 'html5lib')
    # print(soup_link)
    # articles=[]

    table = soup_link.find('iframe', {'class':'vidio-embed read-page--video-gallery--item__vidio-embed'})
    # a = table['src']
    # b = table.h1.text
    # print(a)

    
    a = '1'
    b = '2'
    c = table['src']
    d = ' '
    e = ' '
    f = ' '
    g = ' '
    h = '1'
    # tt = table.h1.text
    # d = str(tt).replace('/n','')
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

    # print(a)

    mycursor = mydb.cursor()

    query = "INSERT INTO videos(id_main_kategori_video, id_kategori_video, file, description, descriptionVi, descriptionCn, descriptionId,user_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

    values = (a,b,c,d,e,f,g,h)

    mycursor.execute(query, values)

mydb.commit()
print(mycursor.rowcount, "was inserted.")

    # print("INSERT INTO article(title,img, content) VALUES (`" + table.h1.text + "`,`" + table.source['srcset'] + "`,`" + table.find_all('p') + "`)") 
    # article = [table.h1.text, table.source['srcset']]
    # print(len(article))
    # article['title'] = table.h1.text
    # article['img'] = table.source['srcset']
    # a = table.find_all('p')
    # article['content'] = str(a).replace('[','').replace(']','')

   
    # d = str(c).replace('[','').replace(']','')
    # article = [a,b,d]
    # pprint({a, b , d})

    # articles.append(article)
    # pprint(article)

   
    # mycursor = mydb.cursor()

# #     # data = [article]
    # stmt = """INSERT INTO article (title, img, content) VALUES  (%s, %s, %s)"""
    # mycursor.executemany(stmt, article)
# for a in article:
    # sql = "INSERT INTO article(title,img) VALUES ('"+ a['title']+"'"+"," +"'"+ a['img']+"')"  
#     val = [article]

    # sql = "INSERT INTO article (title, img) VALUES (%s,%s)"

    # mycursor.execute(sql)

    # mydb.commit()

    # print(mycursor.rowcount, "was inserted.")
    # pprint(article)


# filename = 'selinux-sportingnews.csv'
# with open(filename, 'w', newline='') as f:
#     w = csv.DictWriter(f, ['content','img', 'title'])
#     w.writeheader()
#     for article in articles:
#         w.writerow(article)
# print('success webscrepping. file in \WEBSCRAPPING')


print("Complete")

browser.quit()
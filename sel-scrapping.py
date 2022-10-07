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

# import mysql.connector
import mysql.connector as mysql

import html



base = "https://www.sportingnews.com"
browser = webdriver.Chrome('D:/REPOSITORY/python_project/chromedriver.exe')
wait = WebDriverWait(browser, 10)
browser.get('https://www.sportingnews.com/us/soccer/news')
while True:
    try:
        time.sleep(1)
        show_more = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@class="button"][contains(.,"Load more")]')))  
        show_more.click()
    except Exception as e:
            print(e)
            break    

soup = BeautifulSoup(browser.page_source,'lxml')
search_results = soup.find('div', {'class':'trending-news__list'})

article ={}
mydb = mysql.connect(
        host="localhost",
        user="root",
        password="strong_password1234",
        database="webscrapping"
)

links = search_results.find_all('a')
# print(links)

# link_url = links['href']
# print(link_url)
for link in links:
    link_url = link['href']
    # print(link_url)

    title = link.find_next('a').text

    response = requests.get(base + link_url)

    soup_link = BeautifulSoup(response.text, 'html5lib')
#     articles=[]

    table = soup_link.find('div', attrs={'role':'article'})
    a = table.h1.text
    b = table.source['srcset']
    c = ''
#     print(a)

    mycursor = mydb.cursor()

#     ## defining the Query
    query = "INSERT INTO article (title,img, content) VALUES (%s, %s, %s)"
#     ## storing values in a variable
    # values = ('halo', 'halo1','p')

    values = (a, b,c)

#     ## executing the query with values
    mycursor.execute(query, values)

# ## to make final output we have to run the 'commit()' method of the database object
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
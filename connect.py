import mysql.connector
import requests
from bs4 import BeautifulSoup

import json

mydb = mysql.connector.connect(
    host = "localhost",
    user = 'root',
    password = 'strong_password1234',
    database = "db_webscrapp"
)


mycursor = mydb.cursor()
   

r = requests.get("https://id.77577.live/id/post/index")

soup = BeautifulSoup(r.content, 'html.parser')

images_list = []
images = soup.select("img")

for image in images:
	src = image.get('src')
	images_list.append(src)
	sql = """INSERT INTO article_image (image) VALUES (%s)"""
	mycursor.executemany(sql, (images_list,))
	mydb.commit()
	print(mycursor.rowcount, 'was inserted.')
# print(images_list)

# testjson = json.dumps(images_list)
    
#   itemBank.append((
#         tempRow2['Item_Name'],
#         tempRow1['Item_Price'],
#         tempRow3['Item_In_Stock'],
#         tempRow4['Item_Max'], 
#         getTimeExtra
#         )) #append data

# print(images_list)


#create connection db 

 




# for image in images_list:
# 	print(image)

# sql = "INSERT INTO article_image(src) VALUES(%s)"

# mycursor.executemany(image)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")
   

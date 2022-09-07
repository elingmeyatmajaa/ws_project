import requests
from bs4 import BeautifulSoup as bs
import mysql.connector


mydb = mysql.connector.connect(
    host = "localhost",
    user = 'root',
    password = 'strong_password1234',
    database = "db_webscrapp"
)

mycursor = mydb.cursor()

URL = 'https://id.77577.live/id/post/index'
for page in range(1, 10):


	req = requests.get(URL, params={page:page})
	
	soup = bs(req.content, 'html.parser')

	images_list = []
	images = soup.select("img")

	# print(images)
	for image in images:
		src = image.get('src')
		images_list.append(src)
		sql = """INSERT INTO article_image (image) VALUES (%s)"""
		mycursor.executemany(sql, (images_list,))
		mydb.commit()
		print(mycursor.rowcount, 'was inserted.')
		
	# print(images_list)


	# soup = bs(req.text, 'html.parser')

	# titles = soup.find_all('div', attrs={'class', 'head'})

	# for i in range(4, 19):
	# 	if page > 1:
	# 		print(f"{(i-3)+page*15}" + titles[i].text)
	# 	else:
	# 		print(f"{i-3}" + titles[i].text)

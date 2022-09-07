from urllib import urlopen
from bs4 import BeautifulSoup
import pymysql.cursors

#Webpage conncection
html = urlopen("http://www.officialcharts.com/charts/singles-chart/19800203/7501/")


#Grab title-artis classes
bsObj = BeautifulSoup(html)
recordList = bsObj.find_all("div", {'class': 'title-artist',})

connection = pymysql.connect(host="localhost",
                             user='root',
                             password="strong_password1234",
                             db = "webscrapping", 
                             charset = 'utf8mb4',
                             cursorclas = pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        for record in recordList:
            title = record.find("div", {"class": "title",}).get_text().strip()
            artist = record.find("div", {"class": "artist"}).get_text().strip()
            sql = "INSERT INTO `artist_song` (`artist`, `song`) VALUES (%s, %s)"
            cursor.execute(sql, (artist, title))
    connection.commit()
finally:
    connection.close()
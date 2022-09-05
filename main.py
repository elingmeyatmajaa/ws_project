from ast import If
import requests
from bs4 import BeautifulSoup as bs

from app import URL

URL = "https://id.77577.live/id/post/index"


for page in range(1,10):
    req = requests.get(URL)
    soup = bs(req.text, 'html.parser')
    titles = soup.find_all('div', attrs = {'class', 'row p-0 m-0'})

    for i in range(4, 19):
        if page > 1:
            print(f"{(i-3)+page*15}" + titles[i].text)
        else:
            print(f"{i-3}" + titles[i].text)

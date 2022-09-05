import requests
from bs4 import BeautifulSoup as bs

from app import URL

URL = "https://id.77577.live/id/post/index"

req = requests.get(URL)

soup = bs(req.text, 'html.parser')

titles = soup.find_all('div', attrs= {'class', 'row p-0 m-0'})
print(titles[1].text)
# r =requests.get('https://id.77577.live/id/post/index')


# soup = BeautifulSoup(r.content, 'html.parser')

# for link in soup.find_all('a'):
#     print(link.get('href'))

# s = soup.find("div", class_="row p-0 m-0 mb-3")


# contents = s.find_all( 'p')

# for content in contents:
#     print(content.text)

# print(soup.title)

# print(soup.title.name)

# print(soup.title.parent.name)

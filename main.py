import requests
from bs4 import BeautifulSoup

r =requests.get('https://id.77577.live/id/post/index')


soup = BeautifulSoup(r.content, 'html.parser')

s = soup.find("div", class_="row m-0 p-0 mt-2")


content = s.find_all( 'p')
print(content)

# print(soup.title)

# print(soup.title.name)

# print(soup.title.parent.name)

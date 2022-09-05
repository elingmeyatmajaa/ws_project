import requests
from bs4 import BeautifulSoup

r =requests.get('https://id.77577.live/id/post/index')


soup = BeautifulSoup(r.content, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))

# s = soup.find("div", class_="row p-0 m-0 mb-3")


# contents = s.find_all( 'p')

# for content in contents:
#     print(content.text)

# print(soup.title)

# print(soup.title.name)

# print(soup.title.parent.name)

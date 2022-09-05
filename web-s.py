import requests
from bs4 import BeautifulSoup

r =requests.get('https://www.geeksforgeeks.org/python-programming-language/')

# print(r)

soup = BeautifulSoup(r.content, 'html.parser')

s = soup.find("div", id="main")

leftbar = s.find('ul', class_="leftBarList")



lines = leftbar.find_all('li')
print(lines)

# for line in lines: 
    # print(line.text)
# print(soup.title)

# print(soup.title.name)

# print(soup.title.parent.name)



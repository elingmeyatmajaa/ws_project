import requests
from bs4 import BeautifulSoup as bs


URL = ["https://id.77577.live/id/post/index", "https://id.77577.live/id/post/index?page=10"]


for url in range(0, 2):
    # print(url)
    req = requests.get(URL[url])
    # print(req)
    soup = bs(req.text, 'html.parser')
    # print(soup)

    titles = soup.find_all('div', attrs = {'class', 'row p-0 m-0 mb-3'})
    print(titles)

    # for i in range(4,19):
    #     print(i)
        # if url+1 > 1:
        #     print(i)

    # for i in range(4):
    #   print(i)
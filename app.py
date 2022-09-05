import requests
from bs4 import BeautifulSoup

URL = "https://id.77577.live/id/post/index"
page = requests.get(URL)

print(page.text)
# soup = BeautifulSoup(page.content, "html.parser")
# results = soup.find(id="ResultsContainer")

# results = soup.find(id="ResultsContainer")
# print(results.prettify())
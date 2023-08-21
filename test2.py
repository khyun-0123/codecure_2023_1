import requests
from bs4 import BeautifulSoup

url = "https://www.smu.ac.kr/ko/life/restaurantView4.do"
html = requests.get(url).text
soup = BeautifulSoup(html, "html5lib")
tags = soup.select("#ko > div.board-name-thumb.board-wrap > ul > li:nth-child(1) > dl > dt > a")
for tag in tags:
    print(tag.text)
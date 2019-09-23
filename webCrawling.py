from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

b_url = 'https://www.bikeseoul.com/customer/opinionBoard/opinionBoardList.do?currentPageNo={}'

for n in range(1740):
    url = b_url.format(n + 1)
    webpage = urlopen(url)
    source = BeautifulSoup(webpage, 'html.parser')
    reviews = source.find_all('td', {'class': 'left'})

    for review in reviews:
        print(review.get_text().strip())

review_list = []

for review in reviews:
    review_list.append(review.get_text().strip())

file = open('sharebikeangry2.txt', 'w', encoding='utf-8')

for review in review_list:
    file.write(review + '\n')

file.close()
import requests
from bs4 import BeautifulSoup

url = 'https://ny.eater.com/restaurant-openings'

response = requests.get(url)
# print(response)
soup = BeautifulSoup(response.content, 'html.parser')
# print(soup)
shop_elements = soup.find_all('div', class_='c-entry-box--compact__body')
# print(shop_elements)
for shop in shop_elements:
    # print(shop, '\n')
    shop_head = shop.find('h2', class_='c-entry-box--compact__title')
    if shop_head is None:
        continue
    shop_name = shop_head.find('a').text
    print(shop_name)

    author = shop.find('span', class_='c-byline__author-name')
    author = author.text
    print(f"by {author}")

    time = shop.find('time', class_='c-byline__item')
    time = time.get_text(strip=True)
    print(time)
    print('\n')


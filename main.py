import requests
from bs4 import BeautifulSoup
import json


stores = []

url = 'https://ny.eater.com/restaurant-openings'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
# print(soup)
shop_elements = soup.find_all('div', class_='c-entry-box--compact__body')
# print(shop_elements)
for shop in shop_elements:
    # print(shop, '\n')
    shop_head = shop.find('h2', class_='c-entry-box--compact__title')
    if shop_head is None:
        continue
    # print(shop_head)
    link = shop_head.find('a')['href']
    
    shop_name = shop_head.find('a').text
    

    # print(shop_name)
    # print(shop_url)


    author = shop.find('span', class_='c-byline__author-name')
    author = author.text
    # print(f"by {author}")

    time = shop.find('time', class_='c-byline__item')
    time = time.get_text(strip=True)
    # print(time)

    # print(link)
    print('\n')

    #appending the details to the dict
    stores.append({
        "name": shop_name,
        "author": author,
        "time": time,
        "shop_url": link
    })

for shop in stores:
    print(shop,"\n")

with open('stores.json', 'w') as json_file:
    json.dump(stores, json_file)

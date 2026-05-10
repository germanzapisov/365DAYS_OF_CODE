import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com/'

session = requests.Session()
response = session.get(url)



soup = BeautifulSoup(response.text, 'html.parser')

finder = soup.find_all('article', class_='product_pod')

for i in finder:
    title = i.find('h3').find('a')['title']
    price = i.select_one('.price_color').text
    print(title, price)





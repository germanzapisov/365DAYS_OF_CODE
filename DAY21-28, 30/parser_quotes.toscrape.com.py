import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'

session = requests.Session()

response = session.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
finder = soup.find_all('div', class_='quote')

for i in finder:
    text = i.find('span', class_='text')
    author = i.find('small', class_='author')
    if text and author:
        print(text.get_text())
        print(author.get_text())
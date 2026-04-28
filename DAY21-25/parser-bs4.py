import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows 10 AT win64 x64)',
    'Accept': 'text/html',
    "Accept-Language": "ru-RU,ru;q=0.9"
}

session = requests.Session()
url = ''

response = session.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

print(response.cookies)

for i in soup.find_all('div', class_='podbor__chord'):
    for c in i.children:
        print(c.get_text(strip=True))

params = {
    'q': 'London',
    'appid': 'c313aff6a85060c28ce1ff391e718adc'
}

session = requests.Session()
url = 'https://api.openweathermap.org/data/2.5/weather'
response = session.get(url, params=params, headers=headers)

text = response.json()

weather = text["weather"][0]

print(weather["main"])
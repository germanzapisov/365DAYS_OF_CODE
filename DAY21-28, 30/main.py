import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()

def post(response):
    print(response.text)
    print(response.ok)
    print(response.url)

def get_and_soup(response):
    print(response.status_code)
    text = response.text
    soup = BeautifulSoup(text, "html.parser")
    for s in soup.find_all('strong'):
        text = s.get_text(strip=True)
        if text:
            print(text)



if __name__ == "__main__":

    data = {
        'name': 'german',
        'password': 'G1e9r2dwf'

    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows 10 AT win64 x64)',
        'Accept': 'text/html',
        "Accept-Language": "ru-RU,ru;q=0.9"
    }

    url = os.getenv('URL')
    session = requests.Session()
    response = session.post(url, headers=headers, json=data, timeout=5)
    response.raise_for_status()

    post(response)
    get_and_soup(response)

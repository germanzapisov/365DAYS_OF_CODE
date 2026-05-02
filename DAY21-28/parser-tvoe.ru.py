import requests


url ='https://tvoe.ru/api/product/bonus/'

params = {
    'barcode': '4660303362913'
}
session = requests.Session()

response = session.get(url, params=params)

text = response.json()
print(text)
print('price =',text['items']['4660303362913']['price'])
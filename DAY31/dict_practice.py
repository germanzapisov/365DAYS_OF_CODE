product = {
    'price': 1000,
    'id': 1,
    'name': 'bear'
}

# get — получить значение по ключу
product.get('price')
print(product['price'])
# keys — получить все ключи
product.keys()
# values — получить все значения
product.values()
# items — получить пары ключ/значение
product.items()
# update — обновить словарь
product.update({'price': 7000})
# pop — удалить ключ и вернуть значение
product.pop('id')
# popitem — удалить последнюю пару
product.popitem()
# clear — полностью очистить словарь
# product.clear()
# copy — скопировать словарь
product.copy()
# setdefault — получить значение или создать ключ
product.setdefault('brand', 'Nike')
# fromkeys — создать dict из ключей
dict.fromkeys(['name', 'price'])
# del — удалить ключ
del product['price']
# for — перебор ключей
for key in product:
    print(key)
# values() — перебор значений
for value in product.values():
    print(value)
# items() — перебор ключей и значений
for key, value in product.items():
    print(key, value)
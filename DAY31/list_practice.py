links = ['apple',
         'orange',
         'juice',
         'pineapple',
         'lemon',
         'banana',
         'qiwi',
         'dragonfruit'
         ]

links_array =  [
    [1,2,3],
    [4,5,6],
    [7,8,9]]

print("6: ", links_array[1][2])

# append — добавить элемент в конец
links.append('https://example.com')
# extend — добавить несколько элементов
links.extend(['spider', 'fruit'])
# insert — вставить элемент по индексу
links.insert(0, 'xd')
# remove — удалить элемент по значению
links.remove('lemon')
# pop — удалить элемент по индексу
links.pop()
# clear — полностью очистить список
# links.clear()
# copy — скопировать список
links.copy()
# count — посчитать количество элементов
links.count('apple')
# index — найти индекс элемента
links.index('apple')
# sort — сортировка списка
links.sort()
# sorted() - Создает новый сортированный список
links_three = sorted(links)
# reverse — развернуть список
links.reverse()
# + — объединение списков
# links + links_2



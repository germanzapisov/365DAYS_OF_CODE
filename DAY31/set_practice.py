# #set training
#
# links = set([
#     'https://example13',
#     'https://example353535',
#     'https://example23223',
#     'https://example353',
#     'https://example3533',
#     'https://example4353',
#     'https://example12',
#     'https://example24',
#     'https://example12'
# ])
#
#
# links_2 = set([
#     'https://example1323232',
#     'https://example353535',
#     'https://example23224223',
#     'https://example353',
#     'https://example32424533',
#     'https://example424353',
#     'https://example12',
#     'https://example24',
#     'https://example12'
# ])

# ### Добавить элемент в коллекцию
# links_2.add('https://eaxada')
# ### Удалить элемент (Может выдать ошибку)
# links_2.remove('https://eaxada')
# ### Удалить элемент (Без ошибок)
# links_2.discard('https://eaxada')
# ### Что есть в первом сет, но нет во втором
# new_link = links - links_2
# links.difference(links_2)
# ### Обьединение коллекций
# new_links_un = links.union(links_2)
# new_links = links | links_2
# ### Обьединение коллекций, без создания новой
# links.update(links_2)
# ### Удалить случайный элемент
# links_2.pop()
# ### полностью очистить сет
# links_2.clear()
# ### Скопировать коллекцию
# links_2.copy()


players = set([
           'johny',
           'peter',
           'rihana',
           'andrew',
           'maxim'])

vip_players = set([
            'eagle',
            'freeze_001',
            'viperr',
            'andrew24'])

admins = frozenset([
    'mirgin23',
    'alexxs'
])


def remove_players(vip, basic):
    choice_remove = input("Введите имя игрока для удаления: ")
    vip.remove(choice_remove)
    basic.add(choice_remove)
    return vip_players, players

def add_players(vip, basic):
    choice_add = input("Введите имя игрока для добавления: 1")
    vip_players.add(choice_add)
    players.remove(choice_add)
    return vip, basic


def all_players(vip, basic):
    all_players = vip.union(basic)
    print(all_players)
    return all_players

def return_players(basic):
    print(players)
    return basic

def return_vip_players(vip):
    print(vip)
    return vip

def pop_players(vip, basic):
    lucky_player = basic.pop()
    vip.add(lucky_player)
    return vip_players, players

def clear_players(vip,basic):
    vip_players_new = vip.copy()
    players_new = basic.copy()
    vip_players.clear()
    players.clear()
    return vip_players_new, players_new



def menu():
    while True:
        main_asc = int(input("""Выберите нужное действие:
                             1 - Добавить игрока в випы
                             2 - Удалить игрока из випов
                             3 - Вернуть всех игроков
                             4 - Вернуть обычных игроков
                             5 - Вернуть вип игроков
                             6 - Добавить случайного игрока в випы
                             7 - Удалить всех игроков
                             >> """))

        if main_asc == 1:
            add_players(vip_players, players)
        elif main_asc == 2:
            remove_players(vip_players, players)
        elif main_asc == 3:
            all_players(vip_players, players)
        elif main_asc == 4:
            return_players(players)
        elif main_asc == 5:
            return_vip_players(vip_players)
        elif main_asc == 6:
            pop_players(vip_players, players)
        elif main_asc == 7:
            vip_players_new, players_new = clear_players(vip_players, players)
            print(f"Списки очищены, копии созданы: {vip_players_new}, {players_new}")
        else:
            break

menu()
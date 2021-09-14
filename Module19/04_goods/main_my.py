goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Лампа - 27 шт, стоимость 1134 руб
# Стол - 54 шт, стоимость 27860 руб
# Диван - 3 шт, стоимость 3550 руб
# Стул - 105 шт, стоимость 10311 руб
sym_dict = dict()
for i_goods in goods:
    print (i_goods,' - ', end ='')      #,goods[i_goods])
    for i_store in store:
        print (store[i_store])
#print(sym_dict)

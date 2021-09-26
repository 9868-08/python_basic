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
'''for i_goods in goods:
    print (i_goods,' - ', end ='')      #,goods[i_goods])
    for i_store in store:
        print (store[i_store]) '''

for merch, code in goods.items():	# merch-'Лампа', code-'12345',
	total_quantity = 0
	total_cost = 0
	for goods in store[code]:
		for i in goods:
			total_quantity += goods['quantity']
			total_cost += goods['price']*goods['quantity']
#			print(goods['quantity'],goods['price'])
	print(merch, ' - ', total_quantity, 'шт, стоимость', total_cost, 'руб')

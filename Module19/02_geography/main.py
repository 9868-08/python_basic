def array_search (array,search):
	for i in array:
		if i == search:
			print('город', search, 'находится в ', "тут нужно выташить из словаря страну")
	return "вернуть страну"


motherland = dict()
country_count = int(input('Кол-во стран: '))
print('Германия Берлин Лейпциг Мюнхен')		# подсказдки,
print('Россия Москва Петербург Новгород')	# чтобы не набирать
for i_country in range(country_count):
    cities_list = input('{} страна: '.format(i_country + 1)).split()
    for j_city in cities_list[1:]:
        motherland[j_city] = cities_list[0]
print('motherland=',motherland)
array_search(motherland,'Новгород')

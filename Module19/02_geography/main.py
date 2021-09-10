motherland = dict()
country_count = int(input('Кол-во стран: '))
print('Германия Берлин Лейпциг Мюнхен')		# подсказдки,
print('Россия Москва Петербург Новгород')	# чтобы не набирать
for i_country in range(country_count):
    cities_list = input('{} страна: '.format(i_country + 1)).split()
    for j_city in cities_list[1:]:
        motherland[j_city] = cities_list[0]
print('motherland=',motherland)

for i_city in range(1, 4):
    city_name = input('{} город: '.format(i_city))
    if city_name in motherland:
        print('Город {} расположен в стране {}'.format(
            city_name, motherland[city_name]))
    else:
        print('По городу {} данных нет.'.format(city_name))

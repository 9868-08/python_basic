# count=int(input('Количество стран N: '))
count_country = 2
print('Количество стран', count_country)
count_city = 3
print('Количество городов', count_city)
import re
data = dict()
for i in range(0,count_country):
	print(i, ' страна:',end=" ")
	mystr = input()
	wordList = re.sub("[^\w]", " ", mystr).split()
	print(wordList)
	data = {wordList(0):wordList}
print(data)

#	print(cities)
inc = {'Россия': ['Москва', 'Петербург', 'Новгород', 'Самара'],
	   'Германия': ['Берлин', 'Лейпциг', 'Мюнхен']}
search_value = 'Самара'
for country in inc:
	#	print('country = ', country)
	for city in inc[country]:
		#		print('city = ', city)
		if city == search_value:
			print('город', search_value, 'находится в', country)

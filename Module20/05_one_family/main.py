database = {'Сидоров Никита': 35, 'Сидорова Алина': 34, 'Сидоров Павел': 10, 'Топтунов Павел': 33}

#searching = 'Сидоров'
searching = input('Введите фамилию: ')
for i in database:
	for j in i.split():
		if searching.lower() in j.lower():
			print(i,database[i])

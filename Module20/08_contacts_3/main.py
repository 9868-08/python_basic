def def_search(searching,database):
	for i in database:
		for j in i.split():
			if searching.lower() in j.lower():
				return (i,database[i])

def def_add(adding,database):
	if def_search(adding,database):
		print('контакт уже есть в базе')
	else:
		database[adding]=input('введите номер телефона: ')
	return database

database = {'Сидоров Никита': '123-123', 'Сидорова Алина': '34-43', 'Сидоров Павел': '10-10'}
while True:
	action = input('add,search? ')
	if action == 'search':
		print(def_search(input('ищем: '),database))
	if action == 'add':
		database = def_add(input('добавить: '),database)
	print("текущая база:", database)
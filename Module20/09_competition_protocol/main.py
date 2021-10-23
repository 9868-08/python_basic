# records_count = input('Сколько записей вносится в протокол? ')
records_count = 2
database_dict = dict()

print('Записи (результат и имя): ')
'''for i in range (1, records_count):
	print(i,' запись:', end=' ')
	inc = input('')
	database_dict[i] = inc.split()'''
database_dict = {1: ['69485', ' Jack'],
				 2: ['95715', ' qwerty'],
				 3: ['95715', 'Alex'],
				 5: ['197128', 'qwerty'],
				 6: ['95715', 'Jack'],
				 7: ['93289', 'Alex']}

for i_key in sorted(database_dict):
	print(i_key, database_dict[i_key])

list_keys = list(database_dict)
list_keys.sort()
for i in list_keys:
	print(i, database_dict)

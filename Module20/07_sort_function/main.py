def sort_func(inc_set):
	for i in inc_set:
		if i != int(i):
			print('Список содержит не целое цисло')
			return inc_set
	return sorted(inc_set)

inc = (1,9.1,2,8,3,7,3,6,4,5)
print(sort_func(inc))


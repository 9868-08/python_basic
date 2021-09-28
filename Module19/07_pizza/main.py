pairs_count = 3		# Введите количество заказов: 2
input_list = []
input_dict = dict()
print ('Иванов Пепперони 1')
for i in range (0, pairs_count):
	print(i+1, 'заказ:', end=' ')
	input_string = input()
	input_list = input_string.split(' ')
#	print('input_dict[input_list[0]]', input_dict[input_list[0]])
	if input_list[0] in input_dict:
		for i in input_dict[input_list[0]]:
			print(i)
			if i == input_list[1]:
				print(i)
#		if input_dict[input_list[1]] ==
#		input_dict[input_list[0]] = [input_list[1], input_list[2]]
		print('Запись уже есть')
	else:
		input_dict[input_list[0]] = [input_list[1], input_list[2]]
#	for i, sublist in enumerate(input_list):
#		input_dict[sublist] = sublist
#	input_dict(enumerate(input_list[1],input_list[2]))
#	input_dict[input_list[0]] = input_list[1]
#	input_dict[input_list[1]] = input_list[0]

#	print(input_list[0],input_list[1],input_list[2])
	print(input_dict)



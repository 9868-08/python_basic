def my_sum(input_list):
	result = 0
	for i_element in input_list:
		if type(i_element) != list:
			print('добавляется', i_element)
			result += i_element
		else:
			for j_element in i_element:
				print('добавляется', j_element)
				result += j_element
	return result


my_sum([[1, 2, [3]], [1], 3])

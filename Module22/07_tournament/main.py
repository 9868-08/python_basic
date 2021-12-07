def sorted_dict (def_dict):
	keys = list(def_dict)
	result_dict = dict()
	i_value_max = keys[0]
	i_value_max_prev = keys[0]
	for j in def_dict:
		for i in def_dict:
			if i > i_value_max and not i == j and not i == i_value_max_prev:
				i_value_max = i
		result_dict[i_value_max] = def_dict[i_value_max]
		i_value_max_prev = i_value_max
		i_value_max = keys[0]
	#		i_value_max_prev = i_value_max
	print(i_value_max, result_dict, i_value_max_prev)
	return result_dict

input_file = open('first_tour.txt', 'r')
output_file = open('second_tour.txt', 'w')
result = ''
k = 0
result = dict()
for i_line in input_file:
	k += 1
	i_line = i_line.split(' ')
	if k == 1:
		continue
	if not result[int(i_line[2])]:
		result[int(i_line[2])] = i_line[1][0] + '.' + i_line[0]

count = 1
tmp = ""
for i_key in sorted(result, reverse=True):
	tmp = count, ')', result[i_key], i_key
	print(tmp)
	output_file.write(str(tmp))
	output_file.write('\n')
	count += 1
#print('sorted_dict=', sorted_dict(result))
input_file.close()

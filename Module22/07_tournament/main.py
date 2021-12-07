def sorted_dict (dict):
	result_dict = dict()
	i_value_max = 0
	for i_key in dict:
		if i_key > i_value_max:
			i_value_max = i_key
		print('i_key=', i_key, 'i_value=', dict[i_key] )
		result_dict[i_key] = dict[i_key]
	print(i_value_max, result_dict)
	return

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
	result[int(i_line[2])] = i_line[1][0] + '.' + i_line[0]

count = 1
tmp = ""
for i_key in sorted(result, reverse=True):
	tmp = count, ')', result[i_key], i_key
	print(tmp)
	output_file.write(str(tmp))
	output_file.write('\n')
	count += 1
print(sorted_dict(result))
input_file.close()

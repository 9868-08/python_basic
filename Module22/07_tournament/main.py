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
	#	print(i_line, i_line[1][0])		#имя сокращено до 1 буквы
	result[int(i_line[2])] = i_line[1][0] + '.' + i_line[0]

#	result[int(i_line[2])] = '1'
#	result = str(k-1) + ') ' + i_line
print('1) V. Petrov 98')
count = 1
tmp = ""
for i_key in sorted(result, reverse=True):
	tmp = count, ')', result[i_key], i_key
	print(tmp)
	output_file.write(str(tmp))
	output_file.write('\n')
	count += 1
input_file.close()

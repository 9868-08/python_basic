input_file = open('first_tour.txt', 'r')
output_file = open('second_tour.txt', 'a')
result = ''
k = 0
result = dict()
for i_line in input_file:
	k += 1
	i_line = i_line.split(' ')
	print(i_line, i_line[0])
	if k == 1:
		continue
#	result[int(i_line[2])] = '1'
#	result = str(k-1) + ') ' + i_line
print(result)
#	output_file.write(result)
input_file.close()

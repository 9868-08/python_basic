import os
input_file = open('zen.txt', 'r')
result = []
for i_line in input_file:
	result.append(i_line)

out_file = open('answer.txt', 'w')
for i in range(1, len(result)+1):
	out_file.write(result[len(result)-i])
	print('i=', i, result[len(result)-i])

input_file.close()
out_file.close()
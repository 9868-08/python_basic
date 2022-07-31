import os
input_file = open('numbers.txt', 'r')
summ = 0
for i_line in input_file:
	for i_num in i_line:
		if i_num != ' ' and i_num != '\n':
			summ += int(i_num)

out_file = open('answer.txt', 'w')
out_file.write(str(summ))
input_file.close()
out_file.close()
def cesar(lines):
	out_lines = []
	for shift, line in enumerate(lines):
		new_line = ""
		for char in line:
			if 'a' <= char.lower() <= 'z':
				new_line += chr((ord(char) + shift + 1) % 256)
		out_lines.append(new_line)

	return out_lines

input_file = open('text.txt', 'r')
output_file = open('cipher_text.txt', 'a')
out_lines = cesar(input_file)
# добавляем разбивку по строчкам как в заданном примере
for i_line in out_lines:
	i_line = i_line + '\n'
	output_file.write(i_line)
#output_file.write(result)
input_file.close()

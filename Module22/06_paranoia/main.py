def ceaser_cipher_def(message, k):
	abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	ceaser_cipher = ''
	for letter in message:
		if letter == " ":
			ceaser_cipher += ' '
		elif letter == "\n":
			return ceaser_cipher
		elif letter == ".":
			ceaser_cipher += '.'
		else:
			index = abc.index(letter)
			new_index = index + k
			#print('index=', index, 'abc[index]=', abc[index], 'abc[new_index]', abc[new_index])
			if new_index > len(abc):
				new_index = new_index - len(abc)
			ceaser_cipher += abc[new_index]
	return ceaser_cipher


input_file = open('text.txt', 'r')
output_file = open('cipher_text.txt', 'a')
result = ''
k = 1  # начальный сдвиг
for i_line in input_file:
	result = ceaser_cipher_def(i_line, k)
	result = result + '\n'
	k += 1
	output_file.write(result)
input_file.close()

def ceaser_cipher_def(message, k):
	abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	count = 1
	ceaser_cipher = ''
	for letter in message:
		print(letter)
		if letter == " ":
			ceaser_cipher += ' '
		else:
			index = abc.index(letter)
			new_index = index + k
			print('index=', index, 'abc[index]=', abc[index], 'abc[new_index]', abc[new_index])
			if new_index > len(abc):
				new_index = new_index - len(abc)
			ceaser_cipher += abc[new_index]
	print('Зашифрованное сообщение: ', ceaser_cipher)
	return ceaser_cipher


import os

input_file = open('zen.txt', 'r')
result = []
k = 1  # начальный сдвиг
for i_line in input_file:
	result.append(ceaser_cipher_def(i_line, k))
	k += 1
input_file.close()

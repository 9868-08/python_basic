input_file = open('zen.txt', 'r')
data = input_file.read()
letter_num = 0
word_num = 0
line_num = 0
'''abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
abc_num_dict = dict ()
for i_sym in abc:
	abc_num_dict[i_sym] = 0
'''
for i_sym in data:
	if i_sym == '\n':
		line_num += 1
	elif i_sym == ' ':
		word_num += 1
	else:
		letter_num += 1

print('В тексте', letter_num, 'символов', word_num, 'слов', line_num, 'строк')
input_file.close()

# Дополнительно: выведите на экран букву, которая встречается в тексте наименьшее количество раз
letters_dict = dict()
for char in data.lower():
	if 'a' <= char <= 'z':
		if char not in letters_dict:
			letters_dict[char] = 0
		letters_dict[char] += 1
print(letters_dict)

keys = list(letters_dict.keys())
char_min = keys[0]
char_min_count = letters_dict[keys[0]]
for i_key in keys:
	if letters_dict[i_key] < char_min_count:
		char_min_count = letters_dict[i_key]
		char_min = i_key
print('буква', char_min, 'встречается наименьшее количество раз - ', char_min_count)

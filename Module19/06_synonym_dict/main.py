def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct

'''dict = {
	'Привет' : 'Здравствуйте',
	'Печально': 'Грустно',
	'Весело' : 'Радостно'
}'''
pairs_count = 1		# Введите количество пар слов: 1
input_list = []
input_dict = dict()
print ('Привет - Здравствуйте')
for i in range (0, pairs_count):
	print(i+1, 'пара:', end=' ')
	input_string = input()
	input_list = input_string.split(' - ')
	print(input_list[0],input_list[1])
	input_dict[input_list[0]] = input_list[1]
	input_dict[input_list[1]] = input_list[0]

while 1 == 1:
	word_input = input ('Введите слово: ')
	#word_input = 'Весело'
	if word_input in input_dict:
		print('синоним слову', word_input, ':',input_dict[word_input])
	else:
		print('Такого слова в словаре нет.')
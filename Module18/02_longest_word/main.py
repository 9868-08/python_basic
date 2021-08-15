text = 'абрашварбакадабра. мой дядя самых честных правил'
# text = input('Введите содержимое файла: ')
words_list = text.split()
print(words_list)

max_len_word = ''
for i in words_list:
    if len(i) > len(max_len_word):
        max_len_word = i
        print('длина слова', i, 'равна', len(i))
print('Самое длииное слово: ', max_len_word, 'его длина ', len(max_len_word))

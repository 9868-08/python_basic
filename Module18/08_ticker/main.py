import re

inc = 'Это задание очень! простое'
list = re.split('' ' |, |\*|!', inc)
out = ''
for word in list:
    reverse_word = ''
    count = 1
    for i in word:
        reverse_word = reverse_word + word[len(word) - count]
        count += 1
    out += reverse_word
    print(out)

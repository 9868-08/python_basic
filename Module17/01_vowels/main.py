vowels_list = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
#input_text='Нужно отнести кольцо в Мордор!'
input_text=input('Введите текст для проверки: ')
input_vovwels=[]

for input_character in input_text:
    for vowel in vowels_list:
        if input_character == vowel:
            input_vovwels.append(vowel)

print('Список гласных букв: ', input_vovwels)
print('Длина списка: ', len(input_vovwels))

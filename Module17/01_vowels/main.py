def check_vowel (sybmol,input_vovwels,flag):
    vowels_list = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
    inp_char_count=0
    for vowel in vowels_list:
        if sybmol == vowel and not flag == 1:
            input_vovwels.append(vowel)
    flag = 1
    return input_vovwels,flag


input_text='Нужно отнести кольцо в Мордор!'
#input_text=input('Введите текст для проверки: ')
input_vovwels=[]
flag=0
input_vovwels=[check_vowel(sybmol,input_vovwels,flag) for sybmol in input_text]


print('Список гласных букв: ', input_vovwels)
print('Длина списка: ', len(input_vovwels))

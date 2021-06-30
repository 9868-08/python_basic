input_text='Нужно отнести кольцо в Мордор!'
#input_text=input('Введите текст для проверки: ')

vowels = [i for i in input_text if i in 'ауоыиэяюёе']

print('Список гласных букв: ', vowels)
print('Длина списка: ', len(vowels))

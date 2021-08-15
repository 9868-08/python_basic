filename = '@example.txt'
# filename=input('Название файла: ')

spec_syms = '@№$%^&*()'
for i in filename:
    if i in spec_syms:
        print('файл: ', filename, 'имеет недопустимый символ в имени')
#if '@' or '№' or '$' or '%' or '^' or '&' or '*' or '(' or ')' in filename:
#    print('файл: ', filename, 'имеет недопустимый символ в имени')
if filename[(len(filename) - 4):] == '.txt' or filename[(len(filename) - 4):] == '.docx':
    print('', end='')
else:
    print('файл: ', filename, 'имеет неправильное расширение', filename[(len(filename) - 4):])

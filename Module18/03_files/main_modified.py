filename='example.txt'
#filename=input('Название файла: ')

if '@' or '№' or '$' or '%' or '^' or '&' or '*' or '(' or ')' in filename:
    print ('файл: ', filename, 'имеет недопустимый символ в имени')
if filename[(len(filename)-4):] == '.txt' or filename[(len(filename)-4):] == '.docx':
    print ('',end='')
else:
    print('файл: ', filename, 'имеет неправильное расширение', filename[(len(filename) - 4):])
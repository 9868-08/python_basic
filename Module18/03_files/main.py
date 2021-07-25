#filename='@example.txt'
filename=input('Название файла: ')

for i in filename:
    if i == '@' or i == '№' or i == '$' or i == '%' or i == '^' or i == '&' or i == '*' or i == '(' or i == ')':
        print ('файл: ', filename, 'имеет недопустимый символ в имени')
if filename[(len(filename)-4):] == '.txt' or filename[(len(filename)-4):] == '.docx':
    print ('',end='')
else:
    print('файл: ', filename, 'имеет неправильное расширение', filename[(len(filename) - 4):])
import os

filename = "calc.txt"
try:
    file = open(filename, 'r')
except FileNotFoundError:
    print('Файл не найден!')

lines = file.readlines()
for i_line in lines:
    try:
        print(i_line[:len(i_line)-1], '=', eval(str(i_line)))
    except SyntaxError:
        print("ошибка синтаксиса в строке: ", i_line, end='')
file.close()

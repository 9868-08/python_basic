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
    except:
        print("что-то не так в строке", i_line, 'хотите исправить? ', end='')
        answer = input()
        if answer == 'да':
            i_line = input()
            print(i_line[:len(i_line) - 1], '=', eval(str(i_line)))
        else:
            True
file.close()

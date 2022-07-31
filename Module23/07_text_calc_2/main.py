def numeric(num1, operation, num2):
#    print('num1=', num1, 'operation=', operation, 'num2=', num2)
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '/':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    return result

import os

filename = "calc.txt"
try:
    file = open(filename, 'r')
except FileNotFoundError:
    print('Файл не найден!')

lines = file.readlines()
for i_line in lines:
    i_line_split = i_line.split()
    try:
        num1 = int(i_line_split[0])
        num2 = int(i_line_split[2])
    except (ValueError, IndexError, SyntaxError ):
        print("SyntaxError в строке", i_line, 'хотите исправить? ', end='')
        answer = input()
        if answer == 'да':
            i_line = input()
            i_line_split = i_line.split()
            num1 = int(i_line_split[0])
            num2 = int(i_line_split[2])
            #            i_line_split = i_line.split()
            print(i_line_split[:len(i_line) - 1], '=', numeric(num1, i_line_split[1], num2))

    else:
        print(i_line, '=', numeric(num1, i_line_split[1], num2))
file.close()

def numeric(num1, operation, num2):
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
    except (ValueError, IndexError):
        print('в строке: ', i_line, 'даны некорректные числовые значения')
    else:
        print(i_line, '=', numeric(num1, i_line_split[1], num2))
file.close()

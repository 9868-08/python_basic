print('Задача 3. Рамка')

# Напишите программу,
# которая рисует с помощью символьной графики прямоугольную рамку.
# Для вертикальных линий используйте символ вертикального штриха “|”,
# а для горизонтальных - дефис “-”. Пусть пользователь вводит ширину и высоту рамки.

#  _ _ _ _ _ _ _ _ _
# |                 |
# |                 |
# |                 |
# |                 |
# |                 |
# |                 |
# |_ _ _ _ _ _ _ _ _|
row = int(input('Введите высоту:'))
col = int(input('Введите ширину:'))
#print(' ', end='')
for a in range(0, row+2):					# a - row (строка)
    for b in range(0, col+2):				# b - col (столбец)
        if a == 0 and b <= col:
            print('-', end='')
        elif a == 0 and b >= col:
            print('-')
        elif b == 0 and (a != 0 or a != row):
            print('|', end='')
        elif b == col+1 and (a != 0 or a != row):
            print('|')
        elif a == row+1 and b <= col:
            print('_', end='')
        elif a == row+1 and b >= col:
            print('_')
        else:
            print(' ',end='')
#        print('a=',a,'b=',b)

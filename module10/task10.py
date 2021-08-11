print('Задача 10. Яма ')


# В одной компьютерной текстовой игре рисуются всяческие элементы ландшафта.
#
# Напишите программу,
# которая получает на вход число N и выводит на экран числа в виде “ямы”:

# Введите число: 5
# 
# 5........5
# 54......45
# 543....345
# 5432..2345
# 5432112345
depth = int(input('введите глубину ямы:'))

for line in range(depth):
    for left_number in range(depth, depth - line - 1, -1):
        print (left_number, end = '')
    point_count = 2 * (depth - line -1)
    print ('.' * point_count, end = '')
    for rigth_number in range(depth-line, depth+1):
        print (rigth_number, end = '')
    print ()
#    for right  in range(depth-line, depth+1):
#        print(right)
#    print()

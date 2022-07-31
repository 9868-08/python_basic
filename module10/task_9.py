print('Задача 9. Пирамидка 2')


# Напишите программу,
# которая получает на вход количество уровней пирамиды и выводит их на экран,

# Пример:
# 
#             1
#          3     5
#       7     9     11
#    13    15    17    19
# 21    23    25    27    29
rows = int(input('введите количество ступенек:'))	# высота пирамиды
new_num = 8
for line in range(rows):		# перебираем строчки
  space_count = rows - line - 1
  print ('   ' * space_count,end = '')
  for number in range(line+1):		# столбцы
      print (new_num,end='    ')
      new_num+=2
  print ()


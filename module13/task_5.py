print('Задача 5. Число Эйлера')
# Напишите программу, которая находит сумму  ряда с точностью до 1e-5.
# P.S: Формулу смотреть на сайте :)
# Пример:
# Точность: 1e-20
# Результат: 2.7182818284590455

import math
precision = 1e-20
result = 0
i = 0
addMember = 1

N=int(input('Введите N: '))

while addMember > precision:
    addMember = 1 / math.factorial(i)
    result += addMember
    i += 1
print ('Результат: ', result)
print  ('Константа: ', math.e)
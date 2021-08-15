print('Задача 9. Сумма ряда')
# Пользователь вводит действительное число
# "х" и точность "precision".
# P.S: Формулу смотреть на сайте :)

# Напишите программу,
# которая по число х вычисляет сумму ряда в точности до precision.
# Операцией возведения в степень и функцией factorial пользоваться нельзя.
# Пример:
# Введите точность: 0.001

# Введите x: 5
# Сумма ряда =  0.2836250150891709

def fact(n):
    factorial = 1
    for i in range(2, n+1):
        factorial*= i
 #   print(factorial)
    return factorial

def grade (x,y):    # число x в степени y
    result=1
    for n in range(1, y + 1):
        result+=result*x
    return result

precision = float(input('введите точность: '))
#precision = 1e-20
result = 0
i = 0
addMember = 1

#N=int(input('Введите N: '))
N=3
while addMember > precision:
    addMember = 1 / fact(i)
    result += addMember
    i += 1
print ('Результат: ', result)
import math
print  ('Константа: ', math.e)

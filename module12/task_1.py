print('Задача 1. Сумма чисел')

# Напишите функцию summa_n,
# которая принимает одно целое положительное число N 
# и выводит сумму всех чисел от 1 до N включительно.
# 
# Пример работы программы:
# Введите число: 5
# 
# Я знаю, что сумма чисел от 1 до 5 равна 15
def summa_n(inc):
    summ=0
    for number in range (1,inc+1):
        summ+=number
    print ('сумма всех чисал от 1 до', inc,'=',summ)
inc=int(input('Введите одно целое положительно число N: '))
summa_n(inc)
print('Задача 7. Наибольшая сумма цифр')

# Вводится N чисел. 
# Среди натуральных чисел, которые были введены, 
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.

N=int(input('введите количество чисел N:'))
N_max=0
for num in range (1,N+1):
    inc=int(input('введите число N:'))
    inc=sum(map(int,str(inc)))
    if inc>N_max:
        N_max=inc

print ('Максимальная сумма у введеных чисел:',N_max)
print('Задача 6. Сумма факториалов')

# Напишите программу,
# которая запрашивает у пользователя число N
# и находит сумму факториалов 1! + 2! + 3! +... + N! 
N=int(input('введите число N:'))
factorial=1
for num in range (1,N+1):
    factorial=factorial*num
print ('factorial number', num, '=',factorial)
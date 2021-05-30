print('Задача 9. Выражение')


#Дано число x.
#Напишите программу для вычисления следующего выражения 

# ((x-1)(x-3)(x-7)…(x-63)/
# ((x-2)(x-4)(x-8)…(x-64)) 

x=int(input('Введите x:'))
dividend=1
divider=1
for num in range (1,7):
  dividend*=x-(2**num-1)
  divider*=x-2**num
print (dividend/divider)

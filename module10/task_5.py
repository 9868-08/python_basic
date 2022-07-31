print('Задача 5. Простые числа')


#Напишите программу,
#которая считает количество простых чисел в заданной последовательности 
#и выводит ответ на экран.
begin=int(input('введите начало последовательности:'))
end=int(input('введите конец последовательности:'))
for num in range(begin,end+1):
#  print (num)
  is_prime = True

  for x in range(2,num):
      if num%x==0:
          print(num, 'equals to', x, '*', num//x)
          is_prime = False
          break

  if is_prime:
      print(num, 'is a prime number')
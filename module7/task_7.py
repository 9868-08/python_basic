print('Задача 7. Отрезок')

# Напишите программу,
# которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль 
# среднее арифметическое всех чисел из отрезка [a; b], которые кратны числу 3.

a=int(input('Введите число (положительное, не равное 0) a:'))
b=int(input('Введите число b:'))
b+=1							# корректируем диапазанон
summ=0							# переменная суммы
X = range(a,b)
for number in X:					# number - число из последовательности (a,b)
  if number%3==0:
    average=0						# average среднее арифметическое числа number
    count=number
    while not count == 0:
      average=average+count
      count-=1
    average=average/number
    print ('среднее арифметическое числа ',number,' равно ',average)
    summ+=number
print ('сумма всех чисел кратных 3:',summ)
    
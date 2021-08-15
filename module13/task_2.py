print('Задача 2. Функция максимума')

# Юра пишет различные полезные функции для Питона, 
# чтобы остальным программистам стало проще работать.

# Он захотел написать функцию, 
# которая будет находить максимум из перечисленных чисел.
# Функция для нахождения максимума из двух чисел у него уже есть.
 
# Юра задумался: может быть, её можно как-то использовать 
# для нахождения максимума уже от трёх чисел?
 
 
# Напишите программу, 
# которая находит максимум из трёх чисел.
# Для этого используйте только функцию нахождения максимума из двух чисел.
def smolest_num(num1,num2):
        biggest=  (num1+num2+abs(num1-num2))/2
        smallest= (num1+num2-abs(num1-num2))/2
        return smallest, biggest
    
num1=int(input('Введите первое число: '))
num2=int(input('Введите второе число: '))
num3=int(input('Введите третье число: '))
#num1=3
#num2=2
#num3=1

task2_min1,task2_max1=smolest_num(num1,num2)
task2_min2,task2_max2=smolest_num(num1,num3)
middle,task2_max=smolest_num(task2_max1,task2_max2)
middle,task2_min=smolest_num(task2_min1,task2_min2)
print ('среди числел: ', num1,num2,num3,'найден максимум:',task2_max)
#smolest_num(num1,num2):
#smolest_num(num1,num2):
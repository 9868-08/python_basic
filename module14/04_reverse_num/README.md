## Задача 4. Число наоборот 3
Пользователь вводит два вещественных числа - N и K. Напишите программу, которая отдельно заменяет сначала целую часть на число, которое получается из исходного записью его цифр в обратном порядке, затем то же самое делает с дробной частью. После этого числа складываются и сумма выводится на экран.

#### Пример:
```
Введите первое число: 102.12
Введите второе число: 123.34

Первое число наоборот: 201.21
Второе число наоборот: 321.43
Сумма: 522.64
```
def num_backward (num):
    count = 1
    digit=""
    out=""
    for digit in str(inc):
        out=digit+out
        print('число наоборот: ', digit,out)
        return(out)
num1=123
print (num_backward(num1))
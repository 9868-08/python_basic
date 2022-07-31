print('Задача 3. Апгрейд калькулятора')


# Степан, как и большая часть населения планеты,
# для расчёта суммы и разности чисел использует калькулятор.
# 
# Однако в работе ему нужно
# делать не только  обычные действия вроде сложения и вычитания,
# а делать что-то вручную он уже устал.
# 
# Поэтому Степан решил немного расширить функциональность своего калькулятора.
# 
# Напишите программу,
# которая спрашивает у пользователя число и действие, 
# которое нужно с ним сделать: 
# вывести сумму его цифр,
# вывести максимальную цифру или вывести минимальную цифру. 
# 
# Каждое действие оформите в виде отдельной функции, 
# а основную программу зациклите.

def summ(inc):
    suma = 0
    while abs(inc) > 0:
        digit = inc % 10
        suma += digit
        inc = inc // 10
    print('сумма всех чисел числа равна ', suma)


def max(inc):
    max_inc = 0
    while abs(inc) > 0:
        digit = inc % 10
        if abs(digit) > max_inc:
            max_inc = digit
        inc = inc // 10
    print('максимальное по модулю число: ', max_inc)


def min(inc):
    min_inc = inc // 10
    while abs(inc) > 0:
        digit = inc % 10
        if abs(digit) < min_inc:
            min_inc = digit
        inc = inc // 10
    print('максимальное по модулю число: ', min_inc)


while True:
    num = int(input('Введите число: '))
    action = int(
        input('Введите действие (1 вывести сумму цифр, 2 вывести максимальную цифру,3 вывести минимальную цифру): '))
    if action == 1:
        summ(num)
    if action == 2:
        max(num)
    if action == 3:
        min(num)
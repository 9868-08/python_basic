def numbers_summ (num):
    out=0
    while num != 0:
        out=out+num % 10
        num = num // 10
    return int(out)
def numbers_quantity(num):
    out=0
    while num != 0:
        out+=1
        num = num // 10
    return int(out)

inc = int(input('введите число: '))
#inc=322
print ('Сумма чисел числа',inc,'равна',numbers_summ(inc))
print ('Количество чисел числа',inc,'равна',numbers_quantity(inc))
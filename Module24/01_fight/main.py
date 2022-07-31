from random import randint

health_unit_1 = 100
health_unit_2 = 100

i = 1
while health_unit_1 > 10 and health_unit_2:
    if randint(0, 1) == 0:
        health_unit_1 -= randint(1, 20)
        print('атаковал 1 воин, у воина 2 осталось', health_unit_2, 'здоровья')
    else:
        health_unit_2 -= randint(1, 20)
        print('атаковал 2 воин, у воина 1 осталось', health_unit_1, 'здоровья')

print(health_unit_1, health_unit_2)
if health_unit_1 > health_unit_2:
    print('победу одержал 1 воин')
else:
    print('победу одержал 2 воин')
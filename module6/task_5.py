
print('Задача 5. Счастливый билетик')

# В старину, когда даже в столице билеты в общественном транспорте выдавали контролёры,
# существовало поверье:
# если на билете сумма первых трёх цифр в номере билета равна сумме последних трёх,
# то это к удаче.
#
# Напишите программу,
# которая получала бы на входе шестизначный номер билета
# и выводила, счастливый это билет или нет.
# К примеру, билеты 666 666 и 252 135 — счастливые,
# а 123 456 — нет.
# Подумайте, нужны ли для решения этой задачи циклы?

#while True:
#  inc = int(input('Введите число: '))
#  print ('Ваше число:', inc)
#  if inc==0:
#    break
a = input('введите номер билета (6 знаков)')
b = list(map(int, str(a)))
if b[0]+b[1]+b[2]==b[3]+b[4]+b[5]:
  print ('вы выянули счастлый билетик')
  

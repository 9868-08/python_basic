print('Задача 2. Должники')

# Должники и законопослушные граждане хранятся в одной базе банка.
# Из этой базы нам выделяются по 10 человек, у каждого из которых есть свой номер.
# Правда, иногда база глючит и выдаёт нам отрицательный номер.
# А ещё по статистике, которую собрал наш МирПрогБанк, 
# каждый второй, кто в этом году брал кредит, не выплатил его вовремя.
# 
# Пользователь вводит 10 чисел.
# Напишите программу,
# которая определяет, сколько из них являются одновременно четными и положительными.

counter=1              													# counter - счетчик номера числа
odd=0                  													# odd - количество четных чисел
sign_count=0           													# sing_count - количество отрицательных чисел
while counter<=10:
  print ('Введите число',counter,'с таблички')
  inp = int(input())					# inp - введеное число
  print ('Ваше число:', inp)
  if inp<0:
    inp=abs(inp)
    sign_count+=1
  if inp%2==0:                                                          # число четное
    odd+=1
  counter+=1

print ('введно',sign_count,'отрицательных чисел', "из них четны:",odd)
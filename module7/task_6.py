print('Задача 6. Успеваемость в классе')

# В классе N человек.
# Каждый из них получил за урок по информатике оценку: 3, 4 или 5, двоек сегодня не было. 
# 
# Напишите программу, 
# которая получает список оценок - N чисел - и выводит на экран сообщение о том, 
# кого сегодня больше: отличников, хорошистов или троечников.
N=int(input('Введите чиcло количество учеников: '))
rating_5=0
rating_4=0
rating_3=0
while not N==0:
  print ('оценка ученика',N,':\r')
  current_rating=int(input())
  if current_rating==5:
    rating_5+=1
  if current_rating==4:
    rating_4+=1
  if current_rating==3:
    rating_3+=1
  N-=1
if rating_5>rating_4 and rating_5>rating_3:
  print ('Сегодня больше всего отличников.')
if rating_4>rating_5 and rating_4>rating_3:
  print ('Сегодня больше всего хорошистов.')
if rating_3>rating_5 and rating_3>rating_4:
  print ('Сегодня больше всего троечников.')

print ('Сегодня было',rating_5,'отличников',rating_4,'хорошистов',rating_3,'троечников')
print('Задача 3. Это будет бомба')

# Мы разрабатываем пошаговую игру по мотивам боевика.
# Игрок - главный герой и должен обезвредить бомбу, которая взорвётся через N секунд.
# Программа спрашивает пользователя хочет ли он обезвредить бомбу сейчас.
# 
# Если ответ “0” (то есть “нет”), то счетчик бомбы уменьшается.
# Если он достиг нуля, то программа выдаёт сообщение “Бомба взорвалась”,
# а если не достиг, то программа вновь переспрашивает,
# не хочет ли игрок обезвредить бомбу, и сообщает, сколько времени осталось до взрыва.. 
# 
# Если ответ “да”, то программа выводит на экран сообщение о том,
# что бомба обезврежена и сколько секунд оставалось до взрыва.
# Используйте цикл for.
timer=int(input('на сколько секунд установлен таймер на бомбе:'))
defuse=0
for time in range (0,timer):
  print ('Время до взрыва',timer-time)
  defuse=int(input("Вы хотите обезвредить бомбу? (0-нет, 1-да) "))
  if defuse==1:
    break
print ('Время вышло')
if defuse==0:
  print ('Бомба взорволась')
else:
  print ('Бомба была обезврежена')
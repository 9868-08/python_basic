print('Задача 7. Обычный день на работе')
print ('Начался 8-часовой рабочий день')
hour=0 # прошло часов с начала рабочего дня
total_tasks=0 # выполнено задач сегодня
store=0 # зайти в магазин по звонку жены
while hour<8:
  print ('прошло', hour+1, 'часов от начала рабочего дня')
  wife_call = int(input('звонок жены, взять трубку? (0,1)'))
  if wife_call == 1:
    store=1
  tasks = int(input('Сколько задач решил Максим?'))
  total_tasks=total_tasks+tasks
  hour=hour+1
print ('Рабочий день закончился. Всего выполнено зачач:', total_tasks)
if store==1:
  print ('Нужно зайти в магазин')

# Максим программирует целый день на работе и вечером идёт домой.
# Каждый час начальство кидает ему несколько задач,
# которые нужно решить до следующего рабочего часа.
# И вдобавок каждый час Максиму звонит супруга.
# Он знает, что если он возьмёт трубку, то жена попросит зайти вечером в магазин.
 
# Напишите программу,
# в которой считается, сколько задач выполнил Максим за день (8 часов).
# Если он хоть раз взял трубку,
# то в конце дополнительно выводите сообщение: «Нужно зайти в магазин».
 
# Пример:
# Начался 8-часовой рабочий день
# 1 час
# Сколько задач решит Максим? 1
# Звонит жена. Взять трубку? 0
 
# 2 час
# Сколько задач решит Максим? 2
# Звонит жена. Взять трубку? 0
 
# 3 час
# Сколько задач решит Максим? 3
# Звонит жена. Взять трубку? 0
 
# 4 час
# Сколько задач решит Максим? 4
# Звонит жена. Взять трубку? 1
 
# 5 час
# Сколько задач решит Максим? 5
# Звонит жена. Взять трубку? 0
 
# 6 час
# Сколько задач решит Максим? 1
# Звонит жена. Взять трубку? 0
 
# 7 час
# Сколько задач решит Максим? 2
# Звонит жена. Взять трубку? 1
 
# 8 час
# Сколько задач решит Максим? 3
# Звонит жена. Взять трубку? 0
 
# Рабочий день закончился. Всего выполнено задач: 21
# Нужно зайти в магазин
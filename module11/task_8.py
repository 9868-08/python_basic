print('Задача 8. Часы')

# С начала суток часовая стрелка повернулась на угол в α градусов.
# Определите на какой угол повернулась минутная стрелка с начала последнего часа. 
# Входные и выходные данные — действительные числа.
# 
# При решении этой задачи нельзя пользоваться условными операторами и циклами.
hour_angle=int(input('на какой укол повернулась часовая стрелка:'))
min_angle=(hour_angle%30)*2.5
print ('Минутная стрелка повернулась на:',min_angle,'градусов')
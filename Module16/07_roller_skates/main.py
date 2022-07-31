from random import randrange

skates = []
# N_count = 10                     #количество коньков
N_count = int(input('Введите количество коньков: '))
for index in range(N_count):
    print('Размер', index, 'пары: ', end='')
    new_skates = int(input())
    skates.append(new_skates)
print('размеры коньков на базе:', skates)

legs = []
# K_count = 7                     #количество человек пришли в прокат
K_count = int(input('количество человек пришли в прокат: '))
for index in range(K_count):
    print('Размер ного', index, 'человека: ', end='')
    new_leg = int(input())
    legs.append(new_leg)
print('размеры ног:', legs)

skating_people = 0
skates_work = []
count_ext = 0
count_int = 0
skates.sort()
legs.sort()

for i_leg in legs:  # перебираем размеры ног людей
    for i_skate in skates:  # перебираем коньки на базе
        if i_leg == i_skate:
            skates.remove(i_skate)
            skates_work.append(i_skate)
            skating_people += 1
            print('человеку с размером ноги', i_leg, 'взял коньки. остатки коньков в базе:', skates)
print('смогут покататься', skating_people, 'неиспользованны коньки размером', skates)

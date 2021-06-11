from random import randrange

skates = []
N_count = 10                     #количество коньков
for index in range(N_count):
    skates.append(randrange(10)+1)
print('размеры коньков на базе:', skates)

legs = []
K_count = 7                     #количество человек пришли в прокат
for index in range(K_count):
    legs.append(randrange(10)+1)
print('размеры ног:', legs)

skating_people=0
skates_work=[]
count_ext = 0
count_int = 0
for i_leg in legs:                 #перебираем размеры ног людей
    for i_skate in skates:             #перебираем коньки на базе
        if i_leg == i_skate:
            skates.remove(i_skate)
            skates_work.append(i_skate)
            skating_people+=1
            print('человеку с размером ноги', i_leg, 'взял коньки. остатки коньков в базе:',skates)
print('смогут покататься',skating_people, 'неиспользованны коньки размером', skates)
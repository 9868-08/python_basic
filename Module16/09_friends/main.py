from random import randrange

#N = 3
N=int(input('Введите количество друзей: '))
friends = set(range(N))
#K = 10
K = int(input('количество расписок: '))

credits = []  # ["кто", "кому" , "сколько"]
list(credits)
for num in set(range(0, K)):
    credits.append([randrange(N), randrange(N), randrange(10)])
print('Изначальный список: \n"кто", "кому" , "сколько"')
for IOU in set(range(0, K)):  # IOU - долговая расписка
    print(credits[IOU])

personal=[0 for _ in range(N)]
for num in range(0,N):
    personal[num]=0

#personal = [set(range(0, N))]
for IOU in set(range(0, K)):  # IOU - долговая расписка
#    print(credits[IOU], credits[IOU][0],credits[IOU][1], credits[IOU][2])
    personal[credits[IOU][1]] = credits[IOU][2]
    personal[credits[IOU][1]] -= credits[IOU][0]

print('Отсортированный список: ')
print (personal)
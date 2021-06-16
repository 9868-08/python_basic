from random import randrange

N = 3
print('Количество друзей:', N)
K = 10
print('# количество расписок:', K)

friends = set(range(N))
credits = []  # ["кто", "кому" , "сколько"]
list(credits)
for num in set(range(0, K)):
    credits.append([randrange(N), randrange(N), randrange(10)])
print(credits)

personal = [set(range(0, N))]
for IOU in set(range(0, K)):  # IOU - долговая расписка
    print(credits[IOU], credits[IOU][0],credits[IOU][1], credits[IOU][2])
#    personal[credits[IOU][1]] = credits[IOU][2]
#    personal[credits[IOU][1]] -= credits[IOU][0]


print (personal)
from random import randrange

N = 3
print('Количество друзей:',N)
K = 10
print('# количество расписок:',K)

friends = set(range(N))
credits = []  # ["кто", "кому" , "сколько"]
list(credits)
for num in set(range(0,K)):
    credits.append([randrange(N), randrange(N), randrange(10)])
print(credits)
personal = []
for num in set(range(0,K)):
#    credits.append([randrange(N), randrange(N), randrange(10)])
    print (credits[num][1],credits[num][2])
    personal(credits[num][1])+=credits[num][2]
print(personal)

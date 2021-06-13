from random import randrange

N = 10  # количество человек в кругу
list = set(range(N))
print('исходный список:', list)
while (not len(list) == 1):
    droped = randrange(len(list))
    print('выбывает позиция', list[droped], 'остались', list)
    list.remove(list[droped])
print(list)

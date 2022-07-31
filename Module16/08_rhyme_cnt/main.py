from random import randrange
#N = 10  # количество человек в кругу
N=int(input('Какое количество человек будет играть? '))
list = list(set(range(N)))
print('исходный список:', list)
while (not len(list) == 1):
#    droped = randrange(len(list))
    droped = int(input('Введите число, которое будет выбывать: '))
    list.remove(droped)
    print('выбывает позиция', droped, 'остались', list)

print('последним остался',list)

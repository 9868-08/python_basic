from random import randrange
#N = 10  # количество человек в кругу
N=int(input('Какое количество человек будет играть? '))
list = list(set(range(N)))
print('исходный список:', list)
while (not len(list) == 1):
    droped = randrange(len(list))
    count=0
    new_list=[]
    print('выбывает позиция', list[droped], 'остались', list)
    list.remove(list[droped])
print('последним остался',list)

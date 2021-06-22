from random import randrange

list1 = []
N = 3
for index in range(N):
    new_i=int(input('введите следующий элемент спиcка: '))
#    list1.append(randrange(10))
    list1.append(new_i)
print('первый список:', list1)

list2 = []
N = 7
for index in range(N):
#    list2.append(randrange(10))
    new_i = int(input('введите следующий элемент спиcка: '))
    list2.append(new_i)

print('второй список:', list2)
new_list=[]
new_list.extend(list1)
new_list.extend(list2)
print('объединенный список:', new_list)

for number in new_list:
    for j in range(new_list.count(number) - 1):
        new_list.remove(number)

print('Тот же список с уникальными элементами: ', new_list)

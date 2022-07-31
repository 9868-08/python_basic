from random import randrange

list = []
N = 5
for _ in range(N):
    list.append(randrange(N))
print('изначальный список:', list)
cell_previos = 0
count_int = 0
for number_in_list in list:
    if count_int >= 0:
        if list[count_int + 1] < list[count_int]:
            print(list[count_int + 1], 'меньше', list[count_int], 'в позиции', count_int)
            tmp=list[count_int+1]
            list[count_int+1]=list[count_int]
            list[count_int]=tmp
    count_int += 1
    if count_int==len(list)-1:
        break
print('Упорядоченный список: ', list)
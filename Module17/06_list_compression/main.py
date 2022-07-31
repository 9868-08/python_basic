from random import randint

list = []
N = 5

list = [randint(0,9) for i in range(N) ]
print('изначальный список:', list)

list1 = [list[i] for i in range(len(list)) if list[i] != 0]
print(list1)
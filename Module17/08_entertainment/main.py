from random import randint
import random

N=10
K=3
list = ['I' for i in range(1,N+1)]
print(list)

exclude_list=[]
for i in range(K):
    L_i = random.randint(1,N-1)
    R_i = random.randint(L_i,N)
    print('Бросок', i,'. Сбиты палки с номера',L_i,'по номер', R_i)
    for i_list in range(len(list)):
        if i_list>L_i and i_list<R_i:
            list[i_list]='.'
print(list)

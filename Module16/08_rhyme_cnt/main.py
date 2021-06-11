from random import randrange
N=10
list=set(range(N))
print(list)
for _ in list:
    drop_out=randrange(N)
    print('выбывает', drop_out)
    list.remove(drop_out)
print(list)

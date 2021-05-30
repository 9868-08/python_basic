from random import randrange
list = []
N = 10
for _ in range(N):
    list.append(randrange(N))
print('изначальный список:',list)

for num_ext in list:
    for num_int in list:
        print(num_ext)
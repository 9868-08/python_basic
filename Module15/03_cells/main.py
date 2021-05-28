from random import randrange
cell_index = []
N = 10
print('Количество клеток: ', N)
for index in range(N):
    cell_index.append(randrange(10))
print ('список с индексами клеток:',cell_index)

count=0
for count_index in range(N):
    if cell_index[count_index] <= count_index:
        print('Проверяю клетку номер: ', count_index+1, 'Показатель эффективности это клетки:', cell_index[count_index] )
count+=1
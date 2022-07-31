from random import randrange
N = 10  # количество элементов в списке
max = 10  # максимальный вес
print('Количество элементов: ', N)
cells = []
for _ in range(N):
    cells.append(randrange(max))
print ('изначальный список:',cells)
slip = randrange(max)
print('Сдвиг:', slip)
count=0
output_cells = []
for cell in range(N):
    if count+slip<N:
        output_cells.append(cells[count+slip])
    else:
        output_cells.append(cells[count + slip - N])
    count += 1
print ('  сдвинутый список:',output_cells)

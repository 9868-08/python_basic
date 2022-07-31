from random import randrange
cells = []
N = 10  # количество контейноров
max=10  # максимальный вес
print('Количество контейнеров: ', N)
for index in range(N):
    cells.append(randrange(max))
print ('вес контейнеров:',cells)

new_cell = randrange(max)
print('масса нового контейнера: ', new_cell)
count=0
flag=0
count=1
output_cells=[]
for cell in cells:
    if cell == new_cell:
        print('совпадение найдено\nНомер, куда встанет новый контейнер: ', count+1)
        output_cells.append(new_cell)
        output_cells.append(new_cell)
    else:
        output_cells.append(cell)
    count+=1
print('итоговый список контейнеров: ', output_cells)
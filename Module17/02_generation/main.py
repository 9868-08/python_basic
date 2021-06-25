#N=10
N=int(input('Введите длину списка: '))
output_list = []
for number in range(N):
    if number%2 == 0:
        output_list.append(number)
    else:
        output_list.append(number%5)

print(output_list)
#N=10
N=int(input('Введите длину списка: '))

output_list = [x for x in range(N) ]
output_list_ods = [(1 if x%2 == 0 else x%5) for x in range(N)]

print(output_list,output_list_ods)
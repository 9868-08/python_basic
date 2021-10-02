N = 4	# максимальная высота
print('Введите количество человек: 9')
#N = int(input('Введите количество человек: '))
geno_set=[]
geno_dict = dict
for i in range(1, N, 1):
	print(i, 'пара', end=': ')
	inc = input()
	geno_set = inc.split()
	geno_dict[i] = geno_set
print(geno_dict)

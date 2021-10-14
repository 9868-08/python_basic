def dict_max(dict_input):
	for i in dict_input:
		i_max = 0
		index_max = 0
		count = 0
		if i_max<i:
			i_max=i
			index_max=count
		count+=1
	return (index_max)


N = 4  # максимальная высота
print('Введите количество поколений: 4')
# N = int(input('Введите количество человек: '))
geno_set = []
geno_dict = {}
'''for i in range(1, N, 1):
	print(i, 'пара', end=': ')
	inc = input()
	geno_set = inc.split()
	geno_dict[i] = geno_set'''
# атоматизация, чтобы не вводить код
geno_dict = {2: ['ee_папа', 'ff_мама'], 1: ['cc_бабушка', 'dd_дедушка'], 3: ['bb_прабабушка',
																			 'aa_прадедушка']}
print('не сортированный список: ', geno_dict)
list_geno = list(geno_dict.items())
geno_sorted = list_geno.sort(key=lambda i: i[1])
print(geno_sorted)

for i_key in sorted(geno_dict):
    print(i_key, geno_dict[i_key])

list_keys = list(geno_dict.keys())
list_keys.sort()
for i in list_keys:
    print(i, geno_dict.get(i))
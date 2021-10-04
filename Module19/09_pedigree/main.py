N = 4  # максимальная высота
print('Введите количество человек: 9')
# N = int(input('Введите количество человек: '))
geno_set = []
geno_dict = {}
'''for i in range(1, N, 1):
	print(i, 'пара', end=': ')
	inc = input()
	geno_set = inc.split()
	geno_dict[i] = geno_set'''
# атоматизация, чтобы не вводить код
geno_dict = {1: ['aa_папа', 'bb_мама'], 2: ['cc_бабушка', 'dd_дедушка'], 3: ['bb_прабабушка',
																			 'aa_прадедушка']}
geno_dict_sorted = sorted(geno_dict)
print('не сортированный список: ', geno_dict)
print('сортированный список: ', geno_dict_sorted)
list_geno = list(geno_dict.items())
geno_sorted = list_geno.sort(key=lambda i: i[1])
print(geno_sorted)

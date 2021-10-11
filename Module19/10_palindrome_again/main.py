input = 'aab'

count_i = 0
count_j = 0
for i in input:
	for j in input:
		if i == j and count_i != count_i:
			print('count_i=',count_i,'count_j',count_j)
		count_j += 1


'''#Этот код вычисляет список уникальных элементов в исходном порядке
seen = set()
uniq = []
for x in input:
    if x not in seen:
        uniq.append(x)
        seen.add(x)
print('seen=',seen,'uniq=',uniq,'len(input)=',len(input), 'len(uniq)=',len(uniq))
if len(uniq)>1:
	print('Нельзя сделать палиндромом')
else:
	print('Можно сделать палиндромом')
'''
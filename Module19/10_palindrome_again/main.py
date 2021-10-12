input = 'abbb'

input_dict = dict()
for i in input:
	if i in input_dict:
		input_dict[i] += 1
	else:
		input_dict[i] = 1
odd = 0
for i in input_dict:
	if input_dict[i] % 2 == 0:	#четное количество символов
		True
	else:
		odd +=1
if odd <= 1:
	print('Можно сделать палиндромом')
else:
	print('Нельзя сделать палиндромом')


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
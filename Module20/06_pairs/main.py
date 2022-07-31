inc = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result = []
temp = []
for i in inc:
	if i%2 == 0:
		temp = (inc[i],inc[i+1])
		result.append(temp)
print('первое решение',result)

result1 = []
for i in range(0,len(inc)):
	result1.append((inc[i],inc[i+1]))
	if i+3 < len(inc):
		i += 1
	else:
		break
print('второе решение',result)


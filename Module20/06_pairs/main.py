inc = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result = []
temp = []
for i in inc:
	if i%2 == 0:
		temp = (inc[i],inc[i+1])
		result.append(temp)
print(result)
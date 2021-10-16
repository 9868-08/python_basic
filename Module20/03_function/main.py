input_set = ['aa','bb','cc','dd','bb','ee']
inputed = 'bb'

def f(f_set,f_inputed):
	output_set = []
	flag = False
	for i in f_set:
		if i == inputed:
			flag = not flag
		if flag == True:
			output_set.append(i)

	return output_set

print(f(input_set,inputed))
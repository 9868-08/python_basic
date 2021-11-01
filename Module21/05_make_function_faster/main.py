def calculating_math_func(data):
	factorial = dict()
	global_factorial = dict()
	result = 1
	for index in range(1, data + 1):
		factorial[index] = result
		result *= index
		global_factorial[index] = result
	result /= data ** 3
	result = result ** 10
	print(factorial)
	return result, global_factorial


global_factorial = dict
print(calculating_math_func(5))

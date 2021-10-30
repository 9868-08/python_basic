def my_zip(def_str1, def_str2):
	last_str = popout(def_str1)
	last_set = popout(def_str2)
	return last_str, last_set

def popout(str):
	n = len(str) - 1
	front = str[n:]
	back = str[:n]
	return front, back

input_sring1 = 'abcd'
input_sring2 = [10, 20, 30, 40]
result_set = []

for i in input_sring1:
	tmp = (my_zip(input_sring1, input_sring2))
	input_sring1 = (tmp[0][1])
	input_sring2 = (tmp[1][1])
	result_set.append((tmp[0][0], tmp[1][0]))
print(result_set)

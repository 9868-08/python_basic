def shotrest_seg_tange(set1, set2):
	return min(len(set1),len(set2))

input_str='abc'
input_tpl = [10, 20, 30, 40]

pairs = ((input_str[i_elem], input_tpl[i_elem])
		for i_elem in range(shotrest_seg_tange(input_str, input_tpl)))
print(pairs)
for i_elem in pairs:
	print(i_elem)

print(zip(input_str, input_tpl))

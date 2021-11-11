def shortest_sequence_range(*args):
    return range(len(sorted(args, key=len)[0]))


def my_zip(first, second):
    ans = ((first[i], second[i]) for i in shortest_sequence_range(first, second))
    return ans


input_sring1 = 'abcd'
input_sring2 = [10, 20, 30, 40]
result_set = my_zip(input_sring1,input_sring2)
print(result_set)


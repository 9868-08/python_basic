def find_in_index_by_value(input_dict, value):
    for i in input_dict:
        if i == value:
            return input_dict[i]


# message = "Здесь что-то написано"
message = input('Введите текст: ')
count = dict()
for i in message:
    count[i] = 0
print(count)
for i in message:
    count[i] += 1
print(count)
print('Оригинальный словарь частот:')
for i in message:
    print(i, ':', count[i])
count_dict = dict()
my_dict = {}
max = 0
for i in message:
    count_dict[i] = 0
for i in message:
    count_dict[i] += 1
for i in message:
    if count_dict[i] > max:
        max = count_dict[i]
result_dict = dict()

for i in range(1, max + 1):
    for letter in count_dict:
        if i == find_in_index_by_value(count_dict, letter):
            result_dict.setdefault(i, []).append(letter)
print('Инвертированный словарь частот:')
print("============================")
for i in result_dict:
    print(i, ':', result_dict[i])

# зачтено

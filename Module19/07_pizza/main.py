pairs_count = 3  # Введите количество заказов: 2
input_list = []
input_dict = dict()
print('Иванов Пепперони 1')
for i in range(0, pairs_count):
    print(i + 1, 'заказ:', end=' ')
    input_string = input()
    input_list = input_string.split(' ')
    #	print('input_dict[input_list[0]]', input_dict[input_list[0]])
    if input_list[0] not in input_dict:  # если покупатель НЕ находится в словаре заказов:
        # в словарь по ключу, который является имя покупателя, заносим словарь, ключ которого имя пиццы, а значение - её количество
        input_dict[input_list[0]] = {input_list[1]: int(input_list[2])}
    else:
        if input_list[1] in input_dict[input_list[0]]:
            input_dict[input_list[0]][input_list[1]] += int(input_list[2])
        else:
            input_dict[input_list[0]].update({input_list[1]: int(input_list[2])})

    print(input_dict)

# зачтено

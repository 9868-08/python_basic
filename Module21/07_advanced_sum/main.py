def my_sum(*args):
    total_sum = 0
    for i_elem in args: # идём циклом по елементам в args
        if isinstance(i_elem, int):  # если объект класса инт - добавляем к сумме
            total_sum += i_elem
        elif isinstance(i_elem, (list, tuple)):  # если тупл - идём циклом по туплу, и к сумме прибавляем то, что вернётся от рекурсивного вызова my_sum
            for x in i_elem:
                total_sum += my_sum(x)
            # Вложенный цикл можно заменить на одну строку кода
            # total_sum += my_sum(*i_elem)

    return total_sum


print(my_sum([[1, 2, [3]], [1], 3]))

def error_fun(arg):
    print(f'[Ошибка] Длинна {arg} строки меньше 3 символов')


try:
    peolpe_file = open('people.txt', 'r')
    line_count = 0
    sym_sum = 0
    for i_line in peolpe_file:
        line_count += 1
        lenght = len(i_line)
        if i_line.endswith('\n'):
            lenght -= 1
        if lenght < 3:
            error_fun(line_count)
        #            raise BaseException
        sym_sum += lenght

except FileNotFoundError:
    print('Файл не найден!')

except BaseException:
    error_fun(line_count)

finally:
    print('Найденная сумма символов:', sym_sum)

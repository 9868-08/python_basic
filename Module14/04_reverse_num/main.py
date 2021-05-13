def reverse_num(inc):
    flag = 0
    out_int = ''
    out_fraction = ''
    for num in str(inc):
        if num == '.':
            flag = 1
        elif flag == 0:
            out_int = num + out_int
        else:
            out_fraction = num + out_fraction
    print(out_int + "." + out_fraction)
    return out_int + "." + out_fraction


# inc = int(input('введите число N: '))
N = 123.456
N_reverse = reverse_num(N)
# inc = int(input('введите число K: '))
K = 456.321
K_reverse = reverse_num(K)
print('Число', N, 'наоборот равно ', N_reverse)
print('Число', K, 'наоборот равно ', K_reverse)
print('Сумма: ', float(N_reverse) + float(N_reverse))

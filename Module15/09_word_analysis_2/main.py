inc = 'мадам'
count = 0
flag = 0
for letter in inc:
    if not letter == inc [len(inc) - count - 1]:
        flag=1
    count += 1
if flag == 0:
    print('слово "',inc,'" является полиндромом')
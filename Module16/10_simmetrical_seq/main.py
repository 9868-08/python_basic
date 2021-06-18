def symmetrical_check(list):
    count=0
    symm_flag=1
    for i in list:
        print('inside def',count,i,len(list))
        if not list(i) == list (len(list)-i):
            symm_flag=0
        count+=1
    return symm_flag

num_count = int(input('Кол-во чисел: '))
list = []
while not num_count == 0:
    num_count -= 1
    new_i = int(input('Число: '))
    list.append(new_i)
print(list)
if symmetrical_check(list) == 1:
    print('Число',list, 'симметричное')
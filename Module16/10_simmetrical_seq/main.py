def symmetrical_check(list):
    count=0
    symm_flag=1
    for i in range(len(list)):
        if not list[i] == list[len(list)-i-1]:
            symm_flag=0
    return symm_flag
def input_list() :
    num_count = int(input('Кол-во значений: '))
    list = []
    while not num_count == 0:
        num_count -= 1
        new_i = input('введите значение: ')
        list.append(new_i)
    return list
#list = ['a','b','c','d','e']
list=input_list()
count=0
while symmetrical_check(list) == 0:
    list.append(list[len(list)-count*2-2])
    count+=1
print('последовательность',list, 'симметричная')

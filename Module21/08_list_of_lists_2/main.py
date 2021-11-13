def list_exposure (list):
    result=[]
    for i_element in list:
        if type(i_element) != list:
            print('добавляется', i_element)
            result.append(i_element)
        else:
            list_exposure(i_element)
    return result


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]
print(list_exposure(nice_list))


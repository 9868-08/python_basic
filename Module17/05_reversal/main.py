input_str='Как упоительны в hРоссииh вечера'
#input_str=input('Введите строку: ')

result = [i for i in range(len(input_str)) if input_str[i] == 'h']
ouput_str = input_str[result[0]+1:result[1]]
print ('Между "h" заключена последовательность символов:\n',ouput_str[::-1])

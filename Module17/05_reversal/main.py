#input_str='Как hупоительны вh России вечера'
input_str=input('Введите строку: ')

result = [i for i in range(len(input_str)) if input_str[i] == 'h'  ]
print ('Между "h" заключена последовательность символов:\n',input_str[result[0]+1:result[1]])

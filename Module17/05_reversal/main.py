input_str='Как упоительны в hРоссииh вечера'
#input_str=input('Введите строку: ')

result = ""
flag = 0

#vowels = [i for i in input_text if i in 'ауоыиэяюёе']
for i in input_str:
    if i == 'h' and flag == 1:
        flag=0
    elif flag==1:
        result=result+i
    elif i == 'h' and flag == 0:
        flag=1


print ('Между "h" заключена последовательность символов:',result)

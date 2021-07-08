input_str='Как упоительны в hРоссииh вечера'
#input_str=input('Введите строку: ')

# result = ""
# flag = 0
# for i in input_str:
#     if i == 'h' and flag == 1:
#         flag=0
#     elif flag==1:
#         result=result+i
#     elif i == 'h' and flag == 0:
#         flag=1
#
# team3 = [team1[i]
#            if team1[i] > team2[i]
#            else team2[i]
#            for i in range(20)]
# print ('Очки участников побед-лей тура: ',team3)

result = [i
            if i == 'h' and flag == 1
            else flag == 0
          for i in input_str]

print ('Между "h" заключена последовательность символов:\n',result)

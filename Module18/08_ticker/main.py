def shifter(str,shift):
    count = 0
    result = ''
    tmp=str+str
    for i in str:
        result+=tmp[count+shift]
        count+=1
    return result

str1='abcdйцук'
str2='cdйцукab'

count=0
for i in str1:
    if shifter(str1,count) == str2:
        print('строка',str1,'равна строке',str2,'со сдвигом',count)
    count+=1
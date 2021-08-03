ABC=''
text = 'aaAAbbсaaaA'
count=0
i_prev=''
out=''
text=text+' '
for i in text:
    print(i,count,i_prev)
    if i == i_prev:
        count+=1
    elif i != i_prev and count>0:
        out+=str(count+1)+i
        count=0
    else:
        out+=i
        count=0
    i_prev = i

print('текст: ',text,'зашифрован: ',out)
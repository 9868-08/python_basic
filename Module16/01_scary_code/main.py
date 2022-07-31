#a = [1, 5, 3]
a = ['a', 'b', 'c']
#b = [1, 5, 1, 5]
b = ['d', 'e', 'f']
c = [1, 3, 1, 5, 3, 3]
a.extend(b)
print('Объединенный список а: ', a, 'длинной: ', len(a))

count = 1
print(len(a)-len(b))
for i in a:
    print('обрабатываю count=',count, 'i=', i, 'count=', count)
    if count > (len(a) - len(b)):
        print('удаляетя count=',count,'i=',i)
        a.remove(i)
#    print(a)
    count += 1
print('а после чистки', a)
#a.extend(c)
#print('второй список', a, 'длинной: ', len(a))

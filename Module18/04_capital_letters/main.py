text = 'я люблю питон'
abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
ABC = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

# S = 'Hello'
# print(text.rfind(' '),'=',text[text.rfind(' ')+1],'=')

out = ''
count = 0
flag = 0
for i in text:
    if i != ' ' and flag != 1:
        out = out + i
    elif i == ' ':
        out = out + ' '
        flag = 1
    elif i != ' ' and flag != 0:
        out = out + ' ' + ABC[abc.rfind(text[count])]
        flag = 0
    count += 1
print(out)

#message='это питон'
message=input('Введите сообщение прописнными буквами: ')
#k = 3
k=int(input('Введите сдвиг: '))

abc='абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
count=1
ceaser_cipher=''
for letter in message:
    if letter==" ":
        new_index=index
        ceaser_cipher+=' '
    else:
        index = abc.index(letter)
        new_index=index+3
        ceaser_cipher+=abc[new_index]
print('Зашифрованное сообщение: ', ceaser_cipher)
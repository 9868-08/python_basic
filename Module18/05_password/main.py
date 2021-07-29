def password_check (text):
    abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    ABC = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    NUM = '1234567890'
    uppercase_flag = 0
    num_flag = 0
    for i in text:
        if not ABC.rfind(i) == -1:
            print(i,'- заглавная буква','ABC.rfind(i)',ABC.rfind(i))
            uppercase_flag +=1
        if not NUM.rfind(i) == -1:
            print(i, '- цифра', 'NUM.rfind(i)', NUM.rfind(i))
            num_flag += 1
    print(uppercase_flag)
    if uppercase_flag > 2 and num_flag != 0 :
        return 0
    else:
        return 1


password = ' '
while password_check(password) != 0:
    password = input ('Придумайте пароль: ')
    print('пароль не удовлетворяет условиям')
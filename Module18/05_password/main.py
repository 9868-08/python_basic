def password_check (text):
    abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    ABC = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    NUM = '1234567890'
    uppercase_flag = 0
    num_flag = 0
    count = 0
    for i in text:
        if i in ABC:
#            print(i,'- заглавная буква','ABC.rfind(i)',ABC.rfind(i))
            uppercase_flag +=1
        elif i in NUM:
#            print(i, '- цифра', 'NUM.rfind(i)', NUM.rfind(i))
            num_flag += 1
        count+=1
    print('В введённом пароле', text,'букв верхнего регистра:', uppercase_flag, 'Цифр: ', num_flag)
    if uppercase_flag > 1 and num_flag > 3 and count > 8 :
        return 1    # 1 - требования выполнены
    else:
        return 0


password = ' '
while password_check(password) == 0:
    password = input ('Придумайте пароль: ')
    print('пароль не удовлетворяет условиям')
def ceaser_cipher (string, user_shift):
    char_list = [(abc[(abc.index(sym) + user_shift) % 33] for sym != ' ' else ' ') in string]
    new_str = ''
    for i_char in char_list:
        new_str += i_char
    return new_str

message = 'это питон'
#message=input('Введите сообщение прописнными буквами: ')
k = 3
#k=int(input('Введите сдвиг: '))
abc='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

output_str = ceaser_cipher(message, k)
print('Зашифрованное сообщение: ', output_str)
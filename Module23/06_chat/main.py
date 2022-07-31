def database_open(filename, open_type):
    try:
        database = open(filename, open_type)
    except FileNotFoundError:
        print('file', filename, 'не найден')
    return database


def chat_list(database):
    database = database_open('chat.txt', 'r')
    for i_line in database:
        print(i_line, end='')
    database.close()
    return


def chat_add(database_name, nickname):
    database = database_open('chat.txt', 'a')
    message = input("> ")
    database.write(nickname + ": " + message + "\n")
    database.close()


nickname = input("имя пользователя: ")
#nickname = 'Рома'
database_name = 'chat.txt'

while True:
    action = input(" 1) Посмотреть текущий текст чата\n 2) Отправить сообщение\n 3) выйти\n")
    if action == "1":
        chat_list(database_name)

    elif action == "2":
        chat_add(database_name, nickname)

    elif action == "3":
        break

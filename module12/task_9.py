print('Задача 9. Недоделка')

# Вы пришли на работу в контору по разработке игр,
# целевая аудитория которых - дети и их родители.
# 
# У прошлого программиста было задание
# сделать две игры в одном приложении, чтобы пользователь мог выбирать одну из них.
# 
# Однако программист, на место которого вы пришл
# и, перед увольнением не успел сделать эту задачу и оставил только небольшой шаблон проекта.
# 
# Используя этот шаблон,
# реализуйте игры «Камень, ножницы, бумага» и «Угадай число».
# 
# Правила игры «Камень, ножницы, бумага»:
# программа запрашивает у пользователя строку
# и выводит победил он или проиграл.
# 
# Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.
# 
# Правила игры “Угадай число”:
# программа запрашивает у пользователя число до тех пор, пока он его не отгадает.


def rock_paper_scissors(inc,my_random_choice):
    #Здесь будет игра "Камень, ножницы, бумага"
    print ('# Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.')
    if inc == 1:
        print ('Вы выбрали камень. \nЯ выбрал бумагу, бумага кроет камень - вы проиграли')
        return (0)
    elif inc == 2:
        print ('Вы выбрали ножницы\nЯ выбрал бумагу, ножницы режут бумагу - я проиграл')
        return (1)
    elif inc == 3:
        print ('Вы выбрали бумагу\nЯ выбрал бумагу - ничья')
        return (0)
    

def guess_the_number():
    #Здесь будет игра "Угадай число"
    if inc == 1:
        print ('Вы выбрали камень. \nЯ выбрал бумагу, бумага кроет камень - вы проиграли')
    elif inc == 2:
        print ('Вы выбрали ножницы\nЯ выбрал бумагу, ножницы режут бумагу - я проиграл')
    elif inc == 3:
        print ('Вы выбрали бумагу\nЯ выбрал бумагу - ничья')
    

def mainMenu():
    #Здесь главное меню игры
    return int(input ('выберите \n1 - камень \n2 - ножницы \n3 - бумага\n'))
    


my_random_choice=3
while True:
    inc=mainMenu()
    result=rock_paper_scissors(inc,my_random_choice)
    if result == 1:
        break
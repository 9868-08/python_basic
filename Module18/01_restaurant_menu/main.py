menu = 'утиное филе;фланк-стейк;банановый пирог;плов'
print ('Доступное меню: ', menu)
new_menu = menu.split(';')
print ('На данный момент в меню есть: ', new_menu)
print ('На данный момент в меню есть: ', end = '')
for i in new_menu:
    print("'",i,"'", end = ' ')

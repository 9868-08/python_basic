print('Задача 10')

# Напишите игру - текстовый квест.
# Игрок находится в квартире, его задача - покинуть ее.
# 
# Игрок свободно перемещается по квартире, пока не покинет ее.
# 
# В квартире есть три комнаты (спальня, кухня, ванна) и коридор.
# В ванну можно попасть из коридора и спальни.
# В спальню можно попасть из ванны и коридора.
# На кухню можно попасть только из коридора.
# Коридор связан со всеми комнатами, но в нем дополнительно есть дверь наружу.
# На кухне открыто окно.
# Если игрок пытается выбраться через него, то разбивается и проигрывает


# Пример:

# Вы в спальне. Куда идем?
# 1 - в ванну
# 2 - в коридор
 
# 2

# Вы в коридоре. Куда идем?
# 1 - в спальню
# 2 - в ванну
# 3 - на кухню
# 4 - в дверь
 
# 2
 
# Вы в ванне. Куда идем?
# 1 - в коридор
# 2 - в спальню
 
# 2
 
# Вы в спальне...
# 1- спальня, 2- кухня, 3- ванна 0- коридор.
location = 0
def print_location (location):
    if location == 0:
        print ('вы в корридоре')
    if location == 1:
        print ('вы в спальне')
    if location == 2:
        print ('вы на кухне')
    if location == 3:
        print ('вы в ванной')

def change_location (location, new_location):
    if location == new_location:
        print ('вы никуда не перешли')
        return location
    if new_location == 0:
        return new_location
    elif new_location == 1:
        if location == 0 or location == 3:
            return (new_location)
    elif new_location == 2:
        if location == 0:
            return new_location
        else:
            print ('Вы не можете пройти в спальню из вашей текущей локации')
            return location
    elif new_location == 3:
        if location == 0:
            return new_location
        else:
            print ('Вы не можете пройти в спальню из вашей текущей локации')
    elif new_location == 4:
        if location == 0 or location == 1:
            return new_location
        else:
            print ('Вы не можете пройти в спальню из вашей текущей локации')
    elif new_location == 5:
        if location == 2:
            return new_location
        else:
            print ('Вы не можете пройти в спальню из вашей текущей локации')
            
    print ("вы никуда не перешли")
    return (location)


print_location (location)        
while True:       
    new_location = int(input ('куда идем: 0 - коридор, 1 - спальня, 2 - кухня, 3 - ванна, 4 - дверь наружу, 5 - окно?   '))
    location = change_location (location, new_location)
    if location == 4:
        print ('Вы вышли из квартиры, игра окончена')
        break
    if location == 5:
        print ('Вы выпали из окна, игра окончена')
        break
    print_location (location)

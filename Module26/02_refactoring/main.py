def createGenerator(def_list1, def_list2, def_to_find):
    for item_1 in def_list1:
        for item_2 in def_list2:
            yield str(item_1) + " " + str(item_2) + " " + str(item_1 * item_2)
            if item_1 * item_2 == def_to_find:
                print('Found!!!')
                return


list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56

can_continue = True
for x in list_1:
    for y in list_2:
        result = x * y
        print(x, y, result)
        if result == to_find:
            print('Found!!!')
            can_continue = False
            break
    if not can_continue:
        break

# провести рефакторинг кода
mygenerator = createGenerator(list_1, list_2, to_find)  # создаём генератор
print(mygenerator)  # mygenerator является объектом!

for i in mygenerator:
    print(i)

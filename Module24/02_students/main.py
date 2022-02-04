#Реализуйте модель с именем Student, содержащую поля: «ФИ», «Номер группы», «Успеваемость» (список из пяти элементов).
#Затем создайте список из десяти студентов (данные о студентах можете придумать свои либо запросить их у пользователя) и
#отсортируйте его по возрастанию среднего балла. Выведите результат на экран.

from random import randint

class Student:
    ФИ = str
    group = str
    progress = set()

group = input('Заполняется ведомость группы: ')
for i_num in range (1,11):
    print('ФИО', i_num, 'студента: ', end='')
    Student.ФИ=input()
    Student.group = group
    for j_num in range(0, 5):
        progress = randint(2, 5)
#        print(randint(2, 5))
        Student.progress.add(progress)
    print(Student.progress)
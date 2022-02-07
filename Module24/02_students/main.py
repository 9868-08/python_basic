# Реализуйте модель с именем Student, содержащую поля: «ФИ», «Номер группы», «Успеваемость» (список из пяти элементов).
# Затем создайте список из десяти студентов (данные о студентах можете придумать свои либо запросить их у пользователя) и
# отсортируйте его по возрастанию среднего балла. Выведите результат на экран.

from random import randint


class Student:
    ФИ = str()
    group = str()
    progress = set()

    def info(self):
        print('{}   {}   {}'.format(self.ФИ, self.group, self.progress))


current_student = Student()  # экземпляр класса Student
# group = input('Заполняется ведомость группы: ')
group = "Группа-1"
students_list = set()
for i_num in range(0, 10):
    current_student.ФИ = "Иванов Иван Иваныч" + str(- i_num)
    current_student.group = group
    for j_num in range(0, 5):
        progress = randint(2, 5)
        print('progress=', progress)
        Student.progress.add(progress)
    students_list.add(current_student)

    print(students_list.pop().info())

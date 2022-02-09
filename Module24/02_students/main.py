
from random import randint


class Student:
    FI = str()
    group = str()
    progress = list()
    average = 0

    def info(self):
        print('{}   {}   {} {}'.format(self.FI, self.group, self.progress, self.average))


def student_sort(student_sort_list):
    def_max = 0
    student_def = list()
    for j_student in student_sort_list:
        for i_student in student_sort_list:
            if i_student.average > def_max and i_student != j_student:
                def_max = i_student.average
                student_def.append(i_student)
            def_max = 0
    return student_def


# group = input('Заполняется ведомость группы: ')
group = "Группа-1"
students_list = list()
# progress = list()

for i_num in range(0, 10):
    current_student = Student()  # экземпляр класса Student
    current_student.progress = []
    current_student.FI = "Иванов Иван Иваныч " + str(- i_num) + "-й"
    current_student.group = group
    average = 0
    for j_num in range(0, 5):
        current_student.progres = []
        progress = randint(2, 5)
        current_student.progress.append(progress)
        average += progress
    current_student.average = average / 5
    students_list.append(current_student)
    current_student.info()
sorted_students  = student_sort(students_list)

for i_student in sorted_students:
    i_student.info()

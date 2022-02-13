from random import randint


class Student:
    def init(self, name, FI, group, progress, averange) -> None:
        self.name = name
        self.FI = str()
        self.group = str()
        self.progress = list()
        self.average = 0

    def info(self):
        print('{}   {}   {} {}'.format(self.FI, self.group, self.progress, self.average))


def student_sort(student_sort_list):
    def_max = 0
    student_def = dict()
    tmp_set = list()
    for j_student in student_sort_list:
        if j_student.average in student_def:
            tmp_set.append(j_student)
            print('найден дубль по среднему баллу', j_student.FI)
            student_def[j_student.average] = tmp_set

        else:
            student_def[j_student.average] = j_student
#    print('student_sort result =', student_def[student_sort_list[0].average])
    return student_def


# group = input('Заполняется ведомость группы: ')
group = "Группа-1"
students_list = list()
# progress = list()

for i_num in range(0, 10):
    current_student = Student()  # экземпляр класса Student
    current_student.progress = []
    current_student.FI = "Иванов Иван Иваныч " + str(i_num) + "-й"
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
sorted_students = student_sort(students_list)

for i_student in sorted_students:
    if type(i_student) != list:
        print(sorted_students[i_student], 'средний бал', i_student, )

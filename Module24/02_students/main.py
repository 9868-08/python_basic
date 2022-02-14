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

'''    def get_average_score(self):
        for i  in range (0,5):
            print (self.progress)'''



def student_sort(students):   #стандартная сортировка по оценкам.
    qty_students = len(students)
    for i in range(1, qty_students):
        fl = False
        for j in range(qty_students - 1):
            if students[j].average > students[j + 1].average:
                students[j], students[j + 1] = students[j + 1], students[j]
                fl = True
        if fl:
            break
    return students



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
        current_student.progress = []
        progress = randint(2, 5)
        current_student.progress.append(progress)
        average += progress
    current_student.average = average / 5
    students_list.append(current_student)
#    current_student.info()
sorted_students = student_sort(students_list)

print("отсортированный скисок:")
for i_student in sorted_students:
    if type(i_student) != list:
        print(i_student.FI, 'средний бал', i_student.average )

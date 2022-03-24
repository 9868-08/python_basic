from random import randint


class Student:
    def __init__(self, full_name="имя студента", group_number="Группа-1", scores=[]):
        self.full_name = full_name
        self.group_number = group_number
        self.scores = scores

    def get_average_score(self):
        if len(self.scores) > 0:
            return sum(self.scores) / len(self.scores)
        return 0

    def get_info_str(self):
        return ' '.join([self.full_name, 'группа:', str(self.group_number)])


def student_sort(students):  # стандартная сортировка по оценкам.
    qty_students = len(students)
    for i in range(1, qty_students):
        fl = False
        for j in range(qty_students - 1):
            if students[j].get_average_score() > students[j + 1].get_average_score():
                students[j], students[j + 1] = students[j + 1], students[j]
                fl = True
        if fl:
            break
    return students


# group = input('Заполняется ведомость группы: ')
group = "Группа-1"
students_list = list()
# scores = list()

for i_num in range(0, 3):       # должно быть for i_num in range(0, 10):
    current_student = Student()  # экземпляр класса Student
    current_student.scores = []
    current_student.FI = "Иванов Иван Иваныч " + str(i_num) + "-й"
    current_student.group = group
    average = 0
    current_student.scores = []
    for j_num in range(0, 1):   # Должно быть  for j_num in range(0, 5):
        scores = randint(2, 5)
        current_student.scores.append(scores)
        average += scores
    current_student.average = average / 5
    students_list.append(current_student)
    print(current_student.get_info_str())
sorted_students = student_sort(students_list)

print("отсортированный список:")
for i_student in sorted_students:
    if type(i_student) != list:
        print(i_student.FI, 'средний бал', i_student.get_average_score())

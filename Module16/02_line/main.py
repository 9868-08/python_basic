inp_class_a = range (160,176,2)
class_a = []
for i in inp_class_a:
    class_a.append(int(i))
print('Класс 1:', class_a)
inp_class_b = range (162,180,3)
class_b = []
for i in inp_class_b:
    class_b.append(int(i))
print('Класс 2:', class_b)

class_ab=class_a+class_b
print('Классы смешались:', class_ab)
print('Классы отсортированы:', sorted(class_ab))

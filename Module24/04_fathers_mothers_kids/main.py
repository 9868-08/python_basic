class Parent:
    name = "Иван Иванов"
    aged = 40
    childrens = ['Аня', 'Ваня']

    def info(self):
        print('Родителя зовут {}.\nРодителю {} лет.\n{} - дети родителя'. format(self.name, self.aged, self.childrens))

    def calm(self, def_child):         # успокоить
        def_child.calmed = False
        return def_child

    def feed(self, def_child):         # покормить
        def_child.hungry = False
        return def_child


class Child:
    name = "Саша"
    aged = 40
    childrens = ['Аня', 'Ваня']
    calmed = True
    hungry = True

    def info(self):
        print('меня зовут {}\nМне {} лет\nЯ возбужден - {}\nЯ голоден - {}'. format(self.name, self.aged, self.calmed, self.hungry))




me=Parent()
#current_student = Student()  # экземпляр класса Student

me = Parent()
sun = Child()
if not sun.aged < me.aged - 16:
    print("возраст ребенка должен быть меньше возраста родителя хотя бы на 16 лет")
sun.calmed = True

print("=========== исходные данные ===========")
me.info()
sun.info()

print("=========== после помощи родтеля ===========")
sun = me.calm(sun)
sun = me.feed(sun)
sun.info()
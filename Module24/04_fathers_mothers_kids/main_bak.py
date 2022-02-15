class Parent:
    name = "имя родителя"
    aged = 20
    tasks = ['купить еды', 'приготовить обед']

    def info(self):
#        print('Hello, {}'.format(self.name))
#        print('меня зовут {}'.format(self.name))
        print('меня зовут {}\nМне {} лет\nМне нужно дела {}'. format(self.name, self.aged, self.tasks))

class child:
    name = str
    aged = int

me=Parent()
#current_student = Student()  # экземпляр класса Student

me = Parent()

me.info()
#current_student.info()

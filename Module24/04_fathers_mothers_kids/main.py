class Parent:
    name = "имя родителя"
    aged = 20
    tasks = ['купить еды', 'приготовить обед']
    def info(self):
        print('меня зовут {}/nМне {} лет/n дела {}', format(self.name, self.aged,self.tasks))
class child:
    name = str
    aged = int

me=Parent
me.info(self=)
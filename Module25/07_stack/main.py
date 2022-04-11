from random import randint


class Stack:
    def __init__(self):
        self.def_list = list()

    def __str__(self):
#        return [str(item) for item in self.def_list]
        return "".join(str(self.def_list))

    def add_item(self, new_item):
        self.def_list.insert(0, new_item)


    def del_item(self):
        self.def_list.pop(0)


    def list2stack(self, input_list):
        for item in reversed(input_list):
            self.def_list.append(item)
        return


my_list = ["one", "two", 1, 2]
my_stack = Stack()

print("исходные данные:", my_list)
my_stack.list2stack(my_list)
print("конвертируем список в стек: " , my_stack)

my_stack.add_item("test")
print("добавили стеку значнеие - ", my_stack)

my_stack.del_item()
print("убрали из стека значение - ", my_stack)
from random import randint


class Stack:
    def __init__(self):
        self.def_list = list()

    def __str__(self):
        return '; '.join(str(self.def_list))


    def add_item(self, new_item):
        self.def_list.insert(0, new_item)

    def del_item(self):
        self.def_list.pop(0)

    def list2stack(self, input_list):
        for item in reversed(input_list):
            self.def_list.append(item)
        return


class TaskManager:
    def __init__(self):
        self.task = dict()

    def __str__(self):
        display = []
        if self.task:
            for i_priority in sorted(self.task.keys()):
                display.append('{prior} {task}\n'.format(
                    prior=str(i_priority),
                    task=self.task[i_priority]
                )
            )
        return ''.join(display)


    def new_task(self, task, priority):
        if priority not in self.task:
            self.task[priority] = task

        pass


my_list = ["one", "two", 1, 2]
my_stack = Stack()

print("исходные данные:", my_list)
my_stack.list2stack(my_list)
print("конвертируем список в стек: ", my_stack)

my_stack.add_item("test")
print("добавили стеку значение - ", my_stack)

my_stack.del_item()
print("убрали из стека значение - ", my_stack)

manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)

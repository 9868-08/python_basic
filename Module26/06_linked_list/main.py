class LinkedList:
    def __init__(self):
        self.internal = [1, 2, "one", "two"]

    def __str__(self):
        print("[", end="")
        for item in self.internal:
            print(item, " ", end="")
        print("]", end="")
        return ""

    def append(self, new_item):
        pass

    def get(self, index):
        counter = 0
        for item in self.internal:
            if counter == index:
                return item
            counter += 1

    def remove(self, index):
        counter = 0
        result = []
        for item in self.internal:
            if counter != index:
                result.append(item)
            counter += 1
        self.internal = result



my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)

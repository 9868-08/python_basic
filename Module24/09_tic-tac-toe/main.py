class Field:
    #    satiety = 50            # сытость (вместо hungry)

    def __init__(self, size=3):
        self.tmp = []
        self.result = []
        for i in range(0, size):
            self.tmp.append(0)
        for i in range(0, size):
            self.result.append(self.tmp)
        return

    def info(self):
        print('сосед {}  '.format(self.result))


my_field = Field(3)
my_field.info()

while True:
    raw_input = input("ваш ход: ")
    input_x, input_y = raw_input().split(' ')

    print(input_x, input_y)

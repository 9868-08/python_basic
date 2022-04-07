class Automobile:
    def __init__(self):
        self._x = 0
        self._y = 0
        self._angle = 0
        return

    def __str__(self):
        print("текущие координаты автомобиля:            ({},{})\n"
              "текущее направление движения автомобиля:  {}".format(self._x, self._y, self._angle))
        return


    def set__postion(self, def_x, def_y):
        self._x = def_x
        self._y = def_y
        return


    def set__angle(self, def_angle):
        self._angle = def_angle
        return

    def change_direction(self):
        while True:
            try:
                X, Y = map(int, input('начальные координаты автомобиля: ').split(' '))
            except ValueError:
                print("Недопустимые значения")
                continue
            if X > 10 or Y > 10:
                print("Размер поля должен быть не более 10х10")
                continue
            break

        while True:
            try:
                angle = int(input("угол направления движения:"))
            except ValueError:
                print("Недопустимые значения")
                continue
            if not (0 <= angle or angle <= 360):
                print("направление движения должно быть от 0 до 360 градусов")
                continue
            break

        self.set__postion(X, Y)
        self.set__angle(angle)
        return


class Bus(Automobile):
    def __init__(self):
        self.passengers = 0
        self.money = 0
        return

    def __str__(self):
        print("в салоне автобуса               {} пассажиров,\n".format(self.passengers),
              "водитель собрал с них за проезд {} монет".format(self.money))
        return


    def passanger_incoming(self, new_passengers):
        self.passengers += new_passengers
        return

    def passanger_outcoming(self, out_passengers):
        self.passengers -= out_passengers
        return

    def move(self, moved):
        self.money += self.passengers * moved
        return




my_car = Automobile()
my_car = Automobile()
my_car.__str__()
my_car.change_direction()
my_car.__str__()
my_bus = Bus()
my_bus.__str__()
print("автобус остановился, вошло 5 пассажиров")
my_bus.passanger_incoming(5)
my_bus.__str__()
print("автобус остановился, вышло 3 пассажира")
my_bus.passanger_outcoming(3)
my_bus.__str__()
print("автобус проехал 4 остановки")
my_bus.move(4)
my_bus.__str__()

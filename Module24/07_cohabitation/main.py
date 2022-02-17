from random import randrange


class Man():
    hungry = 50

    def __init__(self, name):
        self.name = name
        self.__hungry = 50

    def init(self, name="Имя по-умолчанию", hungry=50) -> None:
        self.name = "name"
        self.__hungry = 50

    def info(self):
        print('сосед: {} голодный: {} '.format(self.name, self.hungry))

    def def_eat(self, def_man, def_house):
        def_man.hungry += 10
        def_house.fridge -= 10
        return def_man, def_house

    def def_work(self, def_man, def_house):
        def_man.hungry -= 10
        def_house.nightstand_with_money += 20
        return def_man, def_house

    def def_game(self, def_man):
        def_neighbor.hungry -= 10
        return def_man

class House:
    fridge = 50
    nightstand_with_money = 0

    def init(self, fridge, nightstand_with_money) -> None:
        self.fridge = 50
        self.nightstand_with_money = 0

    def info(self):
        print('{}   {}'.format(self.fridge, self.nightstand_with_money))



neighbor1 = Man("Артем")
neighbor2 = Man("Сережа")
my_house = House()

day = 0
while day < 365:
    action = (randrange(6))
#    print("action=", action)
    if neighbor1.hungry < 20:
        print("на {0} день {1} (первый сосед) покушал так как проголодался".format(day,neighbor1.name))
        neighbor1, my_house = neighbor1.def_eat(neighbor1, my_house)
    elif neighbor2.hungry < 20:
        print("на {0} день {1} (второй сосед) покушал так как проголодался".format(day,neighbor2.name))
        neighbor2, my_house = neighbor2.def_eat(neighbor2, my_house)
    elif my_house.fridge < 10:
        print("на {0} день они пошли в магазин".format(day))
        neighbor1, my_house = neighbor1.def_eat(neighbor1, my_house)
        neighbor2, my_house = neighbor2.def_eat(neighbor2, my_house)
    elif my_house.nightstand_with_money < 50:
        print("на {0} день они пошли работать так как кончились деньги".format(day))
        neighbor1, my_house = neighbor1.def_work(neighbor1, my_house)
        neighbor2, my_house = neighbor2.def_work(neighbor2, my_house)
    elif action == 1:
        print("на {0} день они пошли работать".format(day))
        neighbor1.def_work(neighbor1, my_house)
        neighbor2.def_work(neighbor2, my_house)
    elif action == 2:
        print("на {0} день они поели".format(day))
        neighbor1.def_eat(neighbor1, my_house)
        neighbor2.def_eat(neighbor2, my_house)

    neighbor1.info()
    neighbor2.info()
    day += 1
print("========= на {0} программа закончила работу =========".format(day))
neighbor1.info()
neighbor2.info()
